import sys



class ResultSink:
	pass




class ClassificationSink(ResultSink):
	"""Result sink that collects classification statistics"""
	def __init__(self, labels=[]):
		self.total = 0
		self.correct = 0
		self.tags = dict([(l,1) for l in labels])
		self.correct_by_tag = {}
		self.pred_by_tag = {}
		self.total_by_tag = {}
		self.matrix = {}
		self.model_predictions = []
		return

	def set_labels(self, labels):
		self.tags = dict([(l,1) for l in labels])
		return

	def update(self,gold_cl,pred_cl, score):
		self.total += 1
		self.total_by_tag[gold_cl] = self.total_by_tag.get(gold_cl,0) + 1
		self.pred_by_tag[pred_cl] = self.pred_by_tag.get(pred_cl,0) + 1
		if (gold_cl == pred_cl):
			self.correct += 1
			self.correct_by_tag[pred_cl] = self.correct_by_tag.get(pred_cl,0) + 1
		self.tags[gold_cl] = 1
		self.matrix[(gold_cl,pred_cl)] = self.matrix.get((gold_cl,pred_cl),0) + 1
		self.model_predictions.append((gold_cl,pred_cl, score))
		return

	def accuracy(self):
		"""Print overall accuracy"""
		correct = self.correct
		total = self.total
		acc = self._accuracy(correct, total)
		print "====== ACC: %s (%s/%s) ======" %(round(acc,2),correct,total)
		return

	def _accuracy(self, correct, total, rounding=4 ):
		"""Returns accuracy so far"""
		try:
			acc = correct / float(total)
			acc = round( acc, rounding)
		except ZeroDivisionError:
			acc = 0.0
		return acc

	def confusion(self):
		"""Print confusion matrix"""
		print "====== Confusion matrix ======"
		print '\tas'
		print 'is\t',"\t".join(self.tags.keys())
		for tag1 in self.tags.keys():
			print tag1,'\t',
			for tag2 in self.tags.keys():
				print self.matrix.get((tag1,tag2),0),'\t',
			print
		return

	def predictions(self):
		truth_and_predicted = [str(x)+"\t"+y for (x,y,_) in self.model_predictions]
		print "====== Model predictions on test data ======"
		print "True\tPredicted"
		print "\n".join(truth_and_predicted)
		print "============================================"

	def rpf(self):
		"""Print R-P-F scores by class labels"""
		print "====== Recall/Precision/F1 by class labels ======"
		print "-"*80
		print "%10s | %10s %10s %10s | %10s %10s %10s" %("Label", "Recall", "Precison", "F1", "Correct", "Predicted", "Gold")
		print "-"*80
		for tag in self.tags:
			corr = self.correct_by_tag.get(tag,0)
			pred = self.pred_by_tag.get(tag,0)
			total = self.total_by_tag.get(tag,0)
			r = corr/float(total)
			p = 0.0
			if pred:
				p = corr/float(pred)
			f = 0.0
			if r+p:
				f = (2*r*p)/(r+p)
			print "%10s | %10s %10s %10s | %10s %10s %10s" %(tag, round(r,3), round(p,3), round(f,3), corr, pred, total)
		print "-"*80
		return

	def print_report(self, verbose=False):
		self.accuracy()
		self.rpf()
#		self.confusion()
		if verbose:
			self.predictions()
		return

	def print_prediction(self, filename):
		f_pred = open(filename, 'w')
		for (gold_cl,pred_cl,score) in self.model_predictions:
			f_pred.write(pred_cl+"\t"+str(score)+"\n")
		return


class RankingSink(ResultSink):
	"""Result sink that collects ranking statistics"""

	def __init__(self):
		self.total = 0
		self.correct = 0
		self.model_predictions = []
		return

	def update(self,gold_idx_list,pred_idx):
		self.total += 1
		if (pred_idx in gold_idx_list):
			self.correct += 1
		self.model_predictions.append((gold_idx_list,pred_idx))
		return

	def accuracy(self):
		"""Print overall accuracy"""
		correct = self.correct
		total = self.total
		acc = self._accuracy(correct, total)
		print "====== ACC: %s (%s/%s) ======" %(round(acc,2),correct,total)
		return

	def _accuracy(self, correct, total, rounding=4 ):
		"""Returns accuracy so far"""
		try:
			acc = correct / float(total)
			acc = round( acc, rounding)
		except ZeroDivisionError:
			acc = 0.0
		return acc

	def predictions(self):
		predicted_and_truth = [str(y)+"\t"+str(x) for (x,y) in self.model_predictions]
		print "====== Model predictions on test data ======"
		print "True\tPredicted"
		print "\n".join(predicted_and_truth)
		print "============================================"

	def print_report(self, verbose=False):
		self.accuracy()
		if verbose:
			self.predictions()
		return
