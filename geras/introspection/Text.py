class Text:
	def __init__(self):
		pass

	def apply(self, pool, scores):
		generation_best = max(scores)
		generation_best_idx = scores.index(generation_best)
		generation_best_individual = pool[generation_best_idx]

		return {'best_individual': generation_best_individual,  #
		        'best_score': generation_best,  #
		        'pool_size': len(pool)}
