'''
Instance.
'''

from feature_vector import FeatureVector as FV
from numpy import zeros
from polka.common.alphabet import POS_LAB, NEG_LAB




class Instance( object ):
	""" An abstract learning instance"""
	pass




class BinaryClassificationInstance( object ):
	""" Classification Instance """
	def __init__( self, index, target_label, input, feature_alphabet ):
		self._index = index
		assert target_label in [POS_LAB, NEG_LAB]
		self._target_label = target_label
		self._input = input
		self._feature_alphabet = feature_alphabet
		self._fv =  FV( input, feature_alphabet ).get_numpy_array()
		return

	def set_target_label( self, label ):
		if label not in [POS_LAB, NEG_LAB]:
			raise Exception("ClassificationInstance Error: illegal label '%s' (not in alphabet)." %label)
		self._target_label = label
		return

	def get_input( self ):
		return self._input

	def get_target_label( self ):
		""" return instance gold label """
		if self._target_label == None:
			raise Exception("ClassificationInstance Error: missing target label.")
		return self._target_label

	def get_index( self ):
		""" return instance index within sample"""
		if self._index == None:
			raise Exception("ClassificationInstance Error: missing index.")
		return self._index

	def get_fv( self ):
		""" return feature vector corresponding to target label """
		return self._fv

	def __str__(self):
		return "u%s: u%s" %(self._target_label,self._fv)




