"""
Feature vector.
"""

import sys
from numpy import zeros, dot
import sys



class FeatureVector:
	""" Feature vector representation based on input datum and feature
	alphabet."""
	def __init__(self, input, alphabet):
		self._input = input
		self._alphabet = alphabet
		self._fv = zeros( alphabet.size() )
		self._lookup()
		return

	def _lookup(self):
		""" lookup input feature indices in alphabet and fill vector
		with feature values"""
		fv = self._fv
		alphabet = self._alphabet
		for feat,val in self._input:
			try:
				pos = self._alphabet[feat]
			except KeyError:
				# unknow feature (at test)
				continue
			try:
				self._fv[pos] = float(val)
			except ValueError:
				sys.exit("FeatureVector Error: non float value found!")
		return

	def get_input(self):
		""" return input """
		return self._input

	def get_numpy_array(self):
		""" return numpy array corresponding to feature vector"""
		return self._fv

	def size(self):
		""" return size of the feature vector"""
		return self._fv.size

	def __str__(self):
		return "%s => %s" %(self._input,self._fv)




class SequenceFeatureVector( FeatureVector ):
	def __init__(self, input_list, output_list, feat_alphabet, tag_alphabet):
		self._input_list = input_list
		self._output_list = output_list
		self._feat_alphabet = feat_alphabet
		self._tag_alphabet = tag_alphabet
		self._fv = zeros( feat_alphabet.size() )
		self._lookup()
		return


	def _feature_generator(self, index): # TODO: add options + refactoring with datasource.py
		in_seq = self._input_list
		out_seq = self._output_list
		tag = out_seq[index]
		token = in_seq[index]
		if index > 0:
			prev_tag = out_seq[index-1]
		else:
			prev_tag = "<s>"
		return [(token,tag),(prev_tag,tag)] 


	def _lookup(self):
		fv = self._fv
		in_seq = self._input_list
		out_seq = self._output_list
		alphabet = self._feat_alphabet
		for i in xrange(len(in_seq)):
			feats = self._feature_generator(i)
			for f in feats:
				try:
					pos = alphabet[f]
					fv[pos] += 1
				except KeyError:
					# unknow feature (at test)
					continue
		return


	def extend(self, index, item, tag):
		in_seq = self._input_list 
		out_seq = self._output_list
		in_seq.append( item )
		assert tag in self._tag_alphabet # TODO: depends on status of alphabet
		out_seq.append( tag )
		fv = self._fv
		alphabet = self._feat_alphabet
		new_feats = self._feature_generator(index)
		for f in new_feats: # REFACTOR
			try:
				pos = alphabet[f]
				fv[pos] += 1
			except KeyError:
				# unknow feature (at test)
				continue
		return

	def __str__(self):
		return "%s => %s" %(self._input_list,self._fv)
	

	# ...
