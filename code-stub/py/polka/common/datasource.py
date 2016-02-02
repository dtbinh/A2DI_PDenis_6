"""
Data Source
"""



import sys
import codecs
import numpy
from collections import Iterable
from alphabet import Alphabet, POS_LAB, NEG_LAB
from polka.common.instance import BinaryClassificationInstance




class Source( object ):
	""" Abstract Class for data Source """
	def __init__( self, data, encoding="utf-8" ):
		if isinstance(data,str):
			self._stream = codecs.open( data, 'r', encoding=encoding)
			self._stream_type = "file"
		elif isinstance(data,list):
			self._stream = data
			self._stream_type = "list"
		elif callable(data): 
			""" to be used when interfacing Polka using generators
				generator() is instance iteratable
				iterated object have the following methods:
					get_label(): returns instance label
					get_featsval(): returns (feature,value) list """
			self._generator = data
			self._stream = self._generator()
			self._stream_type = "generator"
		return

	def _parse( self, sep=None ):
		raise NotImplementedError

	def rewind( self ):
		if self._stream_type == "file":
			self._stream.seek(0)
		elif self._stream_type == "generator":
			self._stream = self._generator()
		return

	def close( self ):
		if self._stream_type == "file":
			self._stream.close()
		return





class BinarySource( Source ):
	""" Source for binary classification data in following format:
	one example per line with feature-value pair separated by
	separator symbol (' ' by default). E.g.:

	1	f1:1.0 f2:1.0 f3:1.0
	-1	f2:1.0 f3:1.0 f8:1.0
	-1	f1:1.0 f2:1.0
	1	f8:1.0 f9:1.0 f10:1.0
	"""
	def __init__( self, data, encoding="utf-8", feature_alphabet=None, alphabet_pop=True, alphabet_lock=True, sep=":", bias=False, bias_prefix="@@BIAS@@" ):
		Source.__init__(self, data, encoding=encoding)
		self._Instance = BinaryClassificationInstance
		if feature_alphabet != None:
			self._feature_alphabet = feature_alphabet
		else:
			self._feature_alphabet = Alphabet(locked=False)
		self._sep = sep
		self._bias = bias
		self._bias_prefix = bias_prefix
		if alphabet_pop:
			self._populate_alphabet()
		if alphabet_lock:
			self.lock_alphabet()
		else:
			self.unlock_alphabet()
		return

	def _parse( self ):
		""" return parsed line """
		sep = self._sep
		for line in self._stream:
			line = line.rstrip()
			items = line.split()
			cl = items[0]
			assert cl in [POS_LAB, NEG_LAB]
			feats = []
			if self._bias:
				feats.append( (self._bias_prefix, 1.0) ) # implicit bias
			for s in items[1:]:
				try:
					f,v = s.rsplit(sep, 1)
					v = float(v)
					feats.append( (f,v) )
				except ValueError:
					sys.exit("Datasource error: make sure you use the right datasource format.")
			yield ( cl, feats )

	def _populate_alphabet( self ):
		print >> sys.stderr, "Populating feature alphabet...             ",
		self.unlock_alphabet()
		if self._stream_type == "generator":
			for i, gen_inst in enumerate(self._stream): # read stream directly
				sys.stderr.write("%s" %"\b"*len(str(i))+str(i))	
				featvals = gen_inst.get_featvals()
				for (f,_) in featvals:
					self._feature_alphabet.add(f)
		else:
			try:
				for tag,feats in self._parse():
					for f,_ in feats:
						self._feature_alphabet.add( f )
			except ValueError:
				sys.exit("Datasource error: make sure you use the right data format.")
			# rewind stream
		try:
			self.rewind()
		except TypeError:
			sys.exit("TypeError: make sure rewind() is used only on files.")
		print >> sys.stderr, " done."
		print >> sys.stderr, "Number of features: %s" %self._feature_alphabet.size()
		return

	def unlock_alphabet( self ):
		self._feature_alphabet.unlock()
		return

	def lock_alphabet( self ):
		self._feature_alphabet.lock()
		return

	def set_alphabet( self, feature_alphabet ):
		self._feature_alphabet = feature_alphabet
		return

	def get_alphabet( self ):
		return self._feature_alphabet

	def get_input( self ):
		for label,feats in self._parse():
			yield label, feats

	def __iter__( self ):
		""" instance generator """
		feature_alphabet = self._feature_alphabet
		assert not (feature_alphabet.empty() and feature_alphabet.locked()), "Feature alphabet is empty!"
		if self._stream_type in ["file","list"]:
			for idx,(label,feats) in enumerate(self._parse()):
				if not feature_alphabet.locked(): # dynamic feature alphabet
					for (f,_) in feats:
						feature_alphabet.add(f)
				instance =  self._Instance(idx, label, feats, feature_alphabet)
				yield instance
		elif self._stream_type == "generator":
			for idx, gen_inst in enumerate(self._stream): # read stream directly
				featvals = gen_inst.get_featvals()
				label = gen_inst.get_label()
				if not feature_alphabet.locked(): # dynamic feature alphabet
					for (f,_) in featvals:
						feature_alphabet.add(f)
				instance = self._Instance(idx, label, featvals, label_alphabet, feature_alphabet)
				yield instance

	def size( self ):
		s = len(list(self._stream))
		self.rewind()
		return s








# basic "test" methods
def test_class_source( arg ):
	source = BinarySource( arg, alphabet_lock=False )
	print "Features:", source.get_alphabet()
	for inst in source:
		print inst.get_target_label(), inst.get_fv()
	source.close()
	return





if __name__ == '__main__':
	import sys
	test_class_source( sys.argv[1] )
	
