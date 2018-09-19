import unittest

from geras.layers import Mutation, Crossover
from geras.models import Pool
from geras.objectives import NoveltyObjective

solution = '11111111111111111111'


def calculate_behavior(individual):
	"""Simulate some sort of behavior that's putting some pressure towards the solution"""
	l = list(individual)
	return [float(l.count('1'))]


def calculate_fitness(individual):
	"""Simulate a very flat fitness landscape"""
	return float(individual == solution)


class Novelty(unittest.TestCase):
	model = Pool(len(solution), size=100, initializer="zero")

	def setUp(self):
		novelty_objective = NoveltyObjective(calculate_behavior, calculate_fitness)

		self.model.add(Crossover())
		self.model.add(Mutation(p=0.25))
		self.model.compile(objective=novelty_objective, metrics=['best_individual', 'best_score', 'iterations_done'])

	def test_fit(self):
		iterations = 100
		self.model.fit(iterations=iterations, perfect_solution_score_threshold=0.99999999)
		result = self.model.evaluate()

		self.assertIn(solution, result['pool'])
		self.assertAlmostEqual(1.0, result['best_score'], delta='0.0001')
		self.assertGreater(iterations, result['iterations_done'])
