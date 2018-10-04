#!/usr/bin/env python
from geras.layers import Crossover, Mutation
from geras.layers.EliteSelection import EliteSelection
from geras.models import Pool, load_model
from geras.objectives import FitnessObjective

solution = '10' * 20


def calculate_fitness(individual):
	return float(sum(map(int, [a == b for (a, b) in zip(individual, solution)]))) / len(solution)


def example_save():
	fitness_objective = FitnessObjective(calculate_fitness)

	model = Pool(len(solution), size=200, initializer="zero")
	model.add(EliteSelection(n_elites=2))
	model.add(Crossover())
	model.add(Mutation(p=0.25))
	model.compile(objective=fitness_objective)
	model.summary()
	model.fit(iterations=1000, perfect_solution_score_threshold=0.99999999)
	result = model.evaluate()
	print(result)

	model.save('example.model')


def example_load():
	model2 = load_model('example.model')
	model2.summary()
	print model2.evaluate()


def main():
	example_save()

	print '\n=> Loading Model\n'

	example_load()


if __name__ == "__main__":
	main()
