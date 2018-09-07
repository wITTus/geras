from random import choice

import numpy as np


class NoveltyObjective:
	archive = []
	archive_scores = []

	def __init__(self, behavior_fn, fitness_fn, K=100, min_sparseness=0.0001):
		self.behavior_fn = behavior_fn
		self.fitness_fn = fitness_fn
		self.min_sparseness = min_sparseness
		self.K = K

	def score(self, pool):
		scores = []

		behaviors = np.array(map(self.behavior_fn, pool))

		for i, behavior in enumerate(behaviors):
			sparseness = self.__calculate_sparseness(behavior, pool)

			if sparseness >= self.min_sparseness:
				self.archive.append(behavior)
				self.archive_scores.append(self.fitness_fn(pool[i]))

			scores.append(sparseness)

		return scores

	def reached_perfect_solution(self, fitness_scores, perfect_solution_score_threshold):
		return max(self.archive_scores) >= perfect_solution_score_threshold

	def __calculate_sparseness(self, behavior, pool):
		if self.archive:
			distances = [np.linalg.norm(behavior - old_behavior) for old_behavior in choice(self.archive)[:self.K]]
			if distances:
				return sum(distances) / len(self.archive)

		return self.min_sparseness
