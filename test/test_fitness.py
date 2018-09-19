import unittest

from geras.layers import Mutation, Crossover
from geras.models import Pool
from geras.objectives import FitnessObjective

solution = '10101010101010101010'


def calculate_fitness(individual):
	"""Simulate a fitness landscape which puts some pressure to the solution"""
	return float(sum(map(int, [a == b for (a, b) in zip(individual, solution)]))) / len(solution)


class Fitness(unittest.TestCase):
	model = Pool(len(solution), size=100, initializer="zero")

	def setUp(self):
		fitness_objective = FitnessObjective(calculate_fitness)

		self.model.add(Crossover())
		self.model.add(Mutation(p=0.25))
		self.model.compile(objective=fitness_objective, metrics=['best_individual', 'best_score', 'iterations_done'])

	def test_fit(self):
		iterations = 100
		self.model.fit(iterations=iterations, perfect_solution_score_threshold=0.99999999)
		result = self.model.evaluate()

		self.assertIn(solution, result['pool'])
		self.assertIn(1.0, result['scores'])
		self.assertAlmostEqual(1.0, result['best_score'], delta='0.0001')
		self.assertGreater(iterations, result['iterations_done'])
