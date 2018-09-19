import heapq


class EliteSelection:
	def __init__(self, n_elites=4):
		self.n_elites = n_elites

	def call(self, pool, new_pool, scores):
		elite_pool = [pool[idx] for idx in map(scores.index, heapq.nlargest(self.n_elites, scores))]
		new_pool.extend(elite_pool)
		return new_pool

	def summary(self):
		print 'EliteSelection'
