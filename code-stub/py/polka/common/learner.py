'''
Learner.

'''

import sys
import time, datetime
from polka.common.alphabet import POS_LAB, NEG_LAB
from polka.common.prediction import ClassificationPrediction as Prediction
from numpy.linalg import norm


class Learner( object ):
	pass




class OnlineLearner( Learner ):
	""" Online learner """
	def __init__(self, model):
		self._model = model
		return

	def learn(self, instances, epochs, start_iter=0, write_every_iter=False, modelpath=None, forget_first=False):
		""" update model parameter vector in a round-like fashion
		based on comparison between the outcome predicted by current
		parameter vector and true outcome"""
		start_time = time.time()
		model = self._model
		print >> sys.stderr, "-"*100
		print >> sys.stderr, "Training..."
		for n in range(start_iter, start_iter+epochs):
			print >> sys.stderr, "it. %3s \t" %n,
			loss = 0.0
			t0 = time.time()
			inst_ct = 0
			for instance in instances:
				inst_ct += 1
				sys.stderr.write("%s" %"\b"*len(str(inst_ct))+str(inst_ct))
				prediction = model.decode( instance )
				loss += model.update( instance, prediction )
			# print >> sys.stderr, inst_ct,
			avg_loss = loss / float(inst_ct)
			t1 = time.time()
			print >> sys.stderr, "\tavg loss = %-7s" %round(avg_loss,6),
			print >> sys.stderr, "\ttime = %-4s" %str(datetime.timedelta(seconds=int(t1-t0)))
			instances.rewind()
			instances.lock_alphabet()
			if write_every_iter and modelpath != None:
				print >> sys.stderr, "\tWriting model at iter %d" %(n+1)
				model.dump_model(modelpath+"_iter_"+str(n+1))
			if forget_first and n == start_iter:
				print >> sys.stderr, "---------- FORGETTING AVERAGED WEIGHTS OF FIRST ITERATION!"
				self._model.reset_avg_weights()
		instances.close()
		if modelpath != None:
			print >> sys.stderr, "\tWriting final model"
			model.dump_model(modelpath)
		elapsed_time = t1-start_time
		print >> sys.stderr, "done in %s" %str(datetime.timedelta(seconds=int(elapsed_time)))
		return
