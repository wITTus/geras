from functools import partial


class FitnessObjective:
	def __init__(self, fitness_fn, cached=True):
		if cached:
			self.cache = {}
			self.scoring_fn = partial(self.__score_individual_cached, fitness_fn)
		else:
			self.cache = None
			self.scoring_fn = fitness_fn

	def score(self, pool):
		return map(self.scoring_fn, pool)

	def reached_perfect_solution(self, fitness_scores, perfect_solution_score_threshold):
		return max(fitness_scores) >= perfect_solution_score_threshold

	def __score_individual_cached(self, fitness_fn, individual):
		if individual in self.cache:
			score = self.cache[individual]
		else:
			score = fitness_fn(individual)
			self.cache[individual] = score
		return score
