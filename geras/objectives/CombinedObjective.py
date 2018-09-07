import numpy as np


class CombinedObjective:

	def __init__(self, objectives):
		self.objectives = objectives

	def score(self, pool):
		scores = sum(np.array([o.score(pool) for o in self.objectives])) / len(self.objectives)  # type: np.ndarray
		return scores.tolist()

	def reached_perfect_solution(self, fitness_scores, perfect_solution_score_threshold):
		return False
