'''
Alphabet.
'''

POS_LAB = "1"
NEG_LAB = "-1"



class Alphabet( object ):
	""" Naive implementation of two-sided object-integer dictionary
	with persistent entries."""
	def __init__(self, locked=False):
		self.__locked = locked
		self.__map = {}
		self.__reverse_map = {}
		return

	def entries(self):
		return self.__map.keys()

	def locked(self):
		return self.__locked

	def unlock(self):
		self.__locked = False
		return

	def lock(self):
		self.__locked = True
		return

	def size(self):
		return len(self.__map)

	def empty(self):
		return self.size() == 0

	def reset(self):
		self.__map = {}
		self.__reverse_map = {}

	def add(self, entry):
		if self.locked():
			raise Exception("Alphabet Error: entry cannot be added to locked alphabet.")
		if entry not in self.__map:
			idx = self.size()
			self.__map[entry] = idx
			self.__reverse_map[idx] = entry
			return idx

	def add_list(self, entry_list):
		for entry in entry_list:
			self.add( entry )
		return

	def update(self, alphabet):
		self.__map.update(alphabet._map)
		self.__reverse_map.update(alphabet._reverse_map)
		return

	def contains(self, entry):
		return entry in self.__map

	def __getitem__(self, entry):
		idx = self.__map.get(entry,None)
		if idx == None:
			raise KeyError("Alphabet Error: entry not indexed.")
		return idx

	def get_index(self, entry):
		return self[entry]

	def get_indices(self, entries):
		return [self[e] for e in entries]

	def get_entry(self, idx):
		entry = self.__reverse_map.get(idx,None)
		if entry == None:
			raise KeyError("Alphabet Error: no entry corresponding to index '%s'." %idx)
		return entry

	def __iter__(self):
		""" return iterator on map keys """
		for k in self.__map:
			yield k

	def __repr__(self):
		return "Alphabet: %s" %repr(self.__map.items())
