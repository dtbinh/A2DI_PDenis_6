'''
Prediction.

'''

from operator import itemgetter
from polka.common.alphabet import POS_LAB, NEG_LAB


class Prediction( object ):
	pass




class ClassificationPrediction( Prediction ):
	""" A classification prediction: list of label-classification
	score pairs."""
	def __init__( self, scored_labels):
		self._scored_labels = sorted( scored_labels, key=itemgetter(1) ) # sort by scores
		self._labels, self._scores = map(list,zip(*self._scored_labels))
		return

	def get_labels(self):
		return self._labels

	def get_scores(self):
		return self._scores

	def get_max_label(self):
		return self._labels[-1]

	def get_max_score(self):
		return self._scores[-1]

	def get_label_by_rank(self, rank):
		return self._labels[-rank]

	def get_score_by_rank(self, rank):
		return self._scores[-rank]

	def get_max_pred(self):
		return (self._labels[-1],self._scores[-1])

	def get_pred_by_rank(self, rank):
		return (self._labels[-rank],self._scores[-rank])

	def get_label_score(self, label):
		idx = self._labels.index(label)
		return self._scores[idx]

	def get_scored_labels(self):
		return self._scored_labels

	def get_n_best(self, n, exclusion=[]):
		n_scored_labels = []
		for label, score in reversed(self._scored_labels):
			if not label in exclusion:
				n_scored_labels.append( (label, score) )
		return n_scored_labels[0:n]

	def __str__(self):
		return str(zip(self._labels,self._scores))




class BinaryPrediction( ClassificationPrediction ):
	""" An binary prediction: a score and its label from {-1, 1}."""
	def __init__( self, score):
		self._score = score
		if score > 0:
			self._label = POS_LAB
			self._scored_labels = [(NEG_LAB, -score), (POS_LAB, score)]
		else:
			self._label = NEG_LAB
			self._scored_labels = [(POS_LAB, score), (NEG_LAB, -score)]
		self._labels, self._scores = map(list,zip(*self._scored_labels))
		return

	def get_label(self):
		return self._label

	def get_score(self):
		return self._score

	def get_pred(self):
		return (self._label,self._score)

	def __str__(self):
		return str((self._label,self._score))




class OrderingPrediction( Prediction ):
	""" An ordering prediction: a score and its associated rank."""
	def __init__( self, scored_label):
		self._label = scored_label[0]
		self._score = scored_label[1]
		return

	def get_label(self):
		return self._label

	def get_score(self):
		return self._score

	def get_pred(self):
		return (self._label,self._score)

	def __str__(self):
		return str((self._label,self._score))




class RankingPrediction( Prediction ):
	""" A ranker prediction: list of candidates sorted by ranker
	score."""
	def __init__( self, scored_candidates): # (index,fv,score)
		self._scored_candidates = scored_candidates
		self._ranked_candidates = sorted( scored_candidates, key=itemgetter(2) )
		self._indices, self._fvs, self._scores = map(list,zip(*self._ranked_candidates))
		return

	def get_scores(self):
		return self._scores

	def get_indices(self):
		return self._indices

	def get_max_index(self):
		return self._indices[-1]

	def get_max_score(self):
		return self._scores[-1]

	def get_max_fv(self):
		return self._fvs[-1]

	def get_min_candidate(self, id_filter=[]):
		if id_filter == []:
			return self._ranked_candidates[0]
		candidates = self._scored_candidates
		id0 = id_filter[0]
		min_cand = candidates[id0]
		for idx in id_filter[1:]:
			cand = candidates[idx]
			if cand[2] < min_cand[2]:
				min_cand = cand
		return min_cand

	def get_max_candidate(self, exclusion=[]): # None if all relevant
		if exclusion == []:
			return self._ranked_candidates[-1]
		for idx in reversed(self._indices):
			if not idx in exclusion:
				return self._scored_candidates[idx]

	def get_candidate_by_rank(self, rank):
		return self._ranked_candidates[-rank]

	def get_candidate(self, idx):
		return self._scored_candidates[idx]

	def get_candidate_score(self, idx):
		return self._scored_candidates[idx][2]

	def get_n_best_candidates(self, n, exclusion=[]):
		n_candidates = []
		for idx in reversed(self._indices):
			if not idx in exclusion:
				n_candidates.append(self._scored_candidates[idx])
		return n_candidates[0:n]

	def __str__(self):
		return str(zip(self._indices,self._scores))




class SequencePrediction( Prediction ):
	""" A sequence prediction: list of sorted k-best output
	sequence structures along with associated features vectors and
	scores: i.e., list of (tag sequence, fv, score) tuples sorted
	by score"""
	def __init__( self, k_best_sequences):
		self._k_best_sequences = k_best_sequences # sorted(k_best_sequences,key=itemgetter(2))
		self._labels, self._fvs, self._scores = map(list,zip(*self._k_best_sequences))
		return

	def get_labels(self):
		return self._labels

	def get_scores(self):
		return self._scores

	def get_fvs(self):
		return self._fvs

	def get_max_label(self):
		return self._labels[-1]

	def get_max_score(self):
		return self._scores[-1]

	def get_max_fv(self):
		return self._fvs[-1]

	def get_label_by_rank(self, rank):
		return self._labels[-rank]

	def get_score_by_rank(self, rank):
		return self._scores[-rank]

	def get_fv_by_rank(self, rank):
		return self._fvs[-rank]

	def get_max_pred(self):
		return (self._labels[-1],self._fvs[-1],self._scores[-1])

	def get_pred_by_rank(self, rank):
		return (self._labels[-rank],self._fvs[-rank],self._scores[-rank])
	def __str__(self):
		return str(zip(self._labels,self._fvs,self._scores))

