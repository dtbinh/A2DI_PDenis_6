"""
Online learner for binary classification.
"""

from math import pow
import sys, os
from numpy import zeros, dot, inf, add, sqrt, resize, identity, double, array, matrix, append
from numpy.linalg import norm
import time
from polka.common.datasource import BinarySource as Source
from polka.common.alphabet import Alphabet, POS_LAB, NEG_LAB
from polka.common.prediction import BinaryPrediction as Prediction
from polka.common.learner import OnlineLearner
from polka.common.function import ltqnorm

import codecs



class Binary( object ):
	""" Abstract linear classifier (in primal form) for binary problems."""
	def __init__( self, feature_alphabet=None, bias=False ):
		self._feature_alphabet = feature_alphabet
		if self._feature_alphabet == None:
			self._feature_alphabet = Alphabet()
		self._weights = None
		self._init_model()
		self._bias = bias
		return

	def _init_model(self):
		""" initialize weights to 0 """
		m = self._feature_alphabet.size()
		self._weights = zeros( m, 'd' )
		return

	def set_alphabet(self, feature_alphabet ):
		""" set alphabet and (re-)initialize weights
		accordingly"""
		m = feature_alphabet.size()
		assert m >= 1 or not feature_alphabet.locked(), "Feature alphabet has %s size." %m
		self._feature_alphabet = feature_alphabet
		self._init_model()
		return

	def get_alphabet(self):
		return self._feature_alphabet

	def get_model(self):
		""" return current model """
		return self._get_model()

	def _get_model(self):
		w = self._weights
		return w

	def set_model( self, weight_dict ):
		""" set model weights from dictionaries"""
		self._set_weights( weight_dict )
		return

	def _set_weights( self, weight_dict ):
		""" set model weight vectors from weight dictionary"""
		assert isinstance(weight_dict,dict)
		weights = self._weights
		feat_alpha = self._feature_alphabet
		for f in weight_dict:
			fidx = feat_alpha[f]
			weights[fidx] = weight_dict[f]
		return

	def learn( self, train_sample, epochs ):
		raise NotImplementedError

	def _get_train_stream( self, data ):
		""" returns training instances stream from data file name or
		data source"""
		feature_alphabet = self._feature_alphabet
		if isinstance(data,str):
			stream = Source(data, feature_alphabet=feature_alphabet, alphabet_lock=False, alphabet_pop=False, bias=self._bias)
		elif isinstance(data,Source):
			stream = data
		elif callable(data):
			stream = Source(data, feature_alphabet=feature_alphabet, alphabet_lock=False, alphabet_pop=False, bias=self._bias)
		else:
			raise Exception("Error: data is either string for file name or ClassificationSource!")
		# set alphabet from data
		self.set_alphabet( stream.get_alphabet() )
		return stream

	def _get_test_stream( self, data ):
		""" returns test instances stream from data file name or
		data source"""
		if isinstance(data,str):
			stream = Source( data, alphabet_lock=True,\
					 alphabet_pop=False, bias=self._bias )
		elif isinstance(data,Source):
			stream = data
		else:
			raise Exception("Error: data is either string for file name or ClassificationSource!")
		# use model alphabet
		stream.set_alphabet( self.get_alphabet() )
		return stream

	def resize_weights(self, instance):
		if len(self._weights) != self._feature_alphabet.size():
			self._weights.resize(self._feature_alphabet.size())
		return

	def update( self, instance, prediction, rate=1.0 ):
		raise NotImplementedError

	def _decode( self, instance, weights ):
		""" return prediction in {-1, 1}
		for current instance based on linear combination of given
		weight parameters """
		fv = instance.get_fv()
		score = dot( weights, fv )
		return Prediction( score )

	def decode( self, instance ):
		""" return prediction for instance given current model"""
		if not self._feature_alphabet.locked():
			self.resize_weights(instance)
		return self._decode( instance, self.get_model() )

	def predict( self, instance ):
		""" return prediction (scored labels) for instance """
		ws = self._get_model()
		prediction = self._decode( instance, ws )
		return prediction

	def classify( self, instance ):
		""" return highest-scoring outcome along with its score for
		instance according to current weight vectors."""
		ws = self._get_model()
		prediction = self._decode( instance, ws )
		return prediction.get_pred() # (label,score)

	def test( self, test_sample, sink ):
		""" evaluate classifier on test sample """
		start_time = time.time()
		sink.set_labels = [POS_LAB,NEG_LAB]
		# read in data
		stream = self._get_test_stream( test_sample )
		print >> sys.stderr, "-"*100
		print >> sys.stderr, "Testing...",
		# make predictions on test sample
		for inst in stream:
			true_label = inst.get_target_label()
			pred_label, score = self.classify( inst )
			# store label pair
			sink.update( true_label, pred_label, score )
		stream.close()
		elapsed_time = time.time()-start_time
		print >> sys.stderr, "done in %s sec." %(round(elapsed_time,3))
		return




class PerceptronBinary( Binary ):
	""" Linear classifier with online learning and perceptron update
	(in primal form)"""
	def __init__( self, bias=False ):
		Binary.__init__(self, bias=bias )
		self._learner = OnlineLearner(self)
		return

	def learn( self, data, epochs=1, start_iter=0, write_every_iter=False, modelpath=None, forget_first=False):
		instances = self._get_train_stream( data )
		self._learner.learn( instances, epochs, start_iter, write_every_iter, modelpath, forget_first )
		return

	def update( self, instance, prediction ):
		""" perceptron update rule:
		NOOOOOP!!! -> w = w + (y - y^) * x
		"""
		w = self._weights
		# x_t
		fv = instance.get_fv()
		# y_t
		t_lab = int(instance.get_target_label())
		# predict y_t
		p_lab = int(prediction.get_label())
		error = (p_lab != t_lab)

		if error:
			self._weights += t_lab * fv

		return error

class PerceptronABinary( Binary ):
	""" Linear classifier with online learning and perceptron update
	(in primal form)"""
	def __init__( self, bias=False ):
		Binary.__init__(self, bias=bias )
		self._learner = OnlineLearner(self)
		self._w_average = self._weights

	def _decode( self, instance, weights ):
		""" return prediction in {-1, 1}
		for current instance based on linear combination of given
		weight parameters """
		fv = instance.get_fv()
		score = dot( self._w_average, fv )
		return Prediction( score )

	def resize_weights(self, instance):
		if len(self._weights) != self._feature_alphabet.size():
			self._weights.resize(self._feature_alphabet.size())
			self._w_average.resize(self._feature_alphabet.size())
		return

	def learn( self, data, epochs=1, start_iter=0, write_every_iter=False, modelpath=None, forget_first=False):
		instances = self._get_train_stream( data )
		self._learner.learn( instances, epochs, start_iter, write_every_iter, modelpath, forget_first )
		return

	def update( self, instance, prediction ):
		""" perceptron update rule:
		NOOOOOP!!! -> w = w + (y - y^) * x
		"""
		w = self._weights
		self._w_average += w
		# x_t
		fv = instance.get_fv()
		# y_t
		t_lab = int(instance.get_target_label())
		# predict y_t
		p_lab = int(prediction.get_label())
		error = (p_lab != t_lab)

		if error:
			self._weights += t_lab * fv

		return error

class PABinary( PerceptronBinary ):
	""" Passive Aggressive (PA) classifier in primal form. PA has a
	margin-based update rule: each update yields at least a margin of
	one (see defails below). Specifically, we implement PA-I rule for
	the binary setting (see Crammer et. al 2006)."""
	def __init__( self, bias=False, C=inf ):
		PerceptronBinary.__init__( self, bias=bias )
		self._C = C # aggressiveness parameter
		return

	def update( self, instance, prediction ):
		"""
		w = w + t * y * x
		where: t = min {C, loss / ||x||**2}
			 loss = 0  if margin >= 1.0
			   1.0 - margin  o.w.
			   margin =  y (w . x)
		"""
		w = self._weights
		fv = instance.get_fv()
		t_lab = int(instance.get_target_label())
		score = prediction.get_score()

		loss = max(0, 1 - dot(t_lab, score))

		t = min(self._C, loss / pow(norm(fv), 2))

		self._weights += dot((t * t_lab), fv)

		return loss

class PAABinary( PerceptronBinary ):
	""" Passive Aggressive (PA) classifier in primal form. PA has a
	margin-based update rule: each update yields at least a margin of
	one (see defails below). Specifically, we implement PA-I rule for
	the binary setting (see Crammer et. al 2006)."""
	def __init__( self, bias=False, C=inf ):
		PerceptronBinary.__init__( self, bias=bias )
		self._C = C # aggressiveness parameter
		self._w_average = self._weights
		return

	def _decode( self, instance, weights ):
		""" return prediction in {-1, 1}
		for current instance based on linear combination of given
		weight parameters """
		fv = instance.get_fv()
		score = dot( self._w_average, fv )
		return Prediction( score )

	def resize_weights(self, instance):
		if len(self._weights) != self._feature_alphabet.size():
			self._weights.resize(self._feature_alphabet.size())
			self._w_average.resize(self._feature_alphabet.size())
		return

	def update( self, instance, prediction ):
		"""
		w = w + t * y * x
		where: t = min {C, loss / ||x||**2}
			 loss = 0  if margin >= 1.0
			   1.0 - margin  o.w.
			   margin =  y (w . x)
		"""
		w = self._weights
		self._w_average += w
		fv = instance.get_fv()
		t_lab = int(instance.get_target_label())
		score = prediction.get_score()

		margin = t_lab * dot(w, fv)
		loss = 0 if margin >= 1.0 else 1.0 - margin
		t = min(self._C, loss / pow(norm(fv), 2))

		self._weights += dot((t * t_lab), fv)

		return loss

if __name__ == "__main__":
	import sys
	import optparse
	from polka.common.result_sink import ClassificationSink
	parser = optparse.OptionParser()
	parser.add_option("-u", "--update", \
					choices=['perc', 'pa', 'paa', 'perca'], \
					default='pa', \
					help="'perc' (perceptron),'pa' (passive-aggressive),'paa' (passive-aggressive-aver),'perca' (perceptron-aver)")
	parser.add_option("-b", "--bias", \
					action="store_true", \
					default=False, \
					help="use biases (default: False)")
	parser.add_option("-C", "--aggressiveness", \
					action="store", \
					default=inf, \
					type=float, \
					help="aggressiveness parameter for PA (default: inf)")
	parser.add_option("-d", "--train", \
					action="store", \
					default='', \
					help="read training data from file")
	parser.add_option("-t", "--test", \
					action="store", \
					default='', \
					help="read test data from file")
	parser.add_option("-i", "--iterations", \
					action="store",\
					default=10, \
					type=int, \
					help="number of iterations (default: 10)")
	parser.add_option("-o", "--output", \
					action="store", \
					default='', \
					help="output predicted labels in file")
	(options, args) = parser.parse_args()
	# check options
	update = options.update
	train = options.train
	test = options.test
	output = options.output
	if not train:
		sys.exit("Please provide train data file (-d).")
	if not test:
		sys.exit("Please provide test data file (-t).")
	print >> sys.stderr, "Binary Classification model: %s" %update
	C = options.aggressiveness
	bias = options.bias
	# init model
	if options.update == 'perc':
		classifier = PerceptronBinary( bias=bias )
	elif options.update == 'pa':
		classifier = PABinary( bias=bias, C=C )
	elif options.update == 'paa':
		classifier = PAABinary( bias=bias, C=C )
	elif options.update == 'perca':
		classifier = PerceptronABinary( bias=bias )

	if train:
		print >> sys.stderr, "Training on data in '%s'." %train
		classifier.learn( train, epochs=options.iterations )
		print >> sys.stderr, "done."
	if test:
		sink = ClassificationSink()
		classifier.test( test, sink )
		sink.print_report()
	if output:
		sink.print_prediction(output)
