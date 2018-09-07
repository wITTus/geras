#!/usr/bin/env python

from geras.layers import Crossover, Mutation
from geras.models import Pool
from geras.objectives import FitnessObjective

solution = '10' * 20


def calculate_fitness(individual):
	return float(sum(map(int, [a == b for (a, b) in zip(individual, solution)]))) / len(solution)


def calculate_behavior(individual):
	l = list(individual)
	return [float(l.count('0')) / 800.0, float(l.count('1')) / 800.0]


def new_best_callback(individual, score):
	print 'New best individual:', score, calculate_fitness(individual), individual


def main():
	fitness_objective = FitnessObjective(calculate_fitness)

	model = Pool(len(solution), size=20, initializer="zero")
	model.add(Mutation(p=0.25))
	model.add(Crossover(n_elites=4))
	model.compile(objective=fitness_objective, metrics=['best_individual', 'best_score', 'iterations_done'])
	model.summary()
	model.fit(iterations=1000, perfect_solution_score_threshold=0.99999999, new_best_callback_fn=new_best_callback)
	result = model.evaluate()

	print(result)


if __name__ == "__main__":
	main()
