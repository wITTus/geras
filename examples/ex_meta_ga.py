#!/usr/bin/env python
from geras.introspection import Matplotlib
from geras.layers import Crossover, Mutation
from geras.layers.EliteSelection import EliteSelection
from geras.models import Pool
from geras.objectives import FitnessObjective

solution = '10' * 20


def calculate_fitness_solution(individual):
	return float(sum(map(int, [a == b for (a, b) in zip(individual, solution)]))) / len(solution)


def calculate_fitness(individual):
	worst_score = 0.0

	# pool size, 10 bits
	# initializer, 2 bits
	# n_elites, 10 bits
	# mutation, 10 bits

	pool_size = int(individual[:10], 2)
	initializer = int(individual[10:12], 2)
	n_elites = int(individual[12:22], 2)
	mutation = int(individual[22:32], 2)

	if initializer == 0:
		initializer_s = 'random'
	elif initializer == 1:
		initializer_s = 'one'
	elif initializer == 2:
		initializer_s = 'zero'
	else:
		return worst_score

	max_pool_size = 1000
	max_iterations = 100

	if pool_size < 10 or pool_size % 2 != 0 or pool_size > max_pool_size:
		return worst_score

	if mutation > 1000:
		return worst_score

	if n_elites >= pool_size or n_elites % 2 != 0:
		return worst_score

	fitness_objective = FitnessObjective(calculate_fitness_solution)
	model = Pool(len(solution), size=pool_size, initializer=initializer_s)
	model.add(EliteSelection(n_elites=n_elites))
	model.add(Crossover())
	model.add(Mutation(p=float(mutation) / 1000.0))
	model.compile(objective=fitness_objective)
	model.fit(iterations=max_iterations, perfect_solution_score_threshold=0.99999999)
	result = model.evaluate()

	score = (float(result['iterations_done']) * pool_size) / float(max_pool_size * max_iterations)

	return 1.0 - score


def calculate_behavior(individual):
	l = list(individual)
	return [float(l.count('0')) / 800.0, float(l.count('1')) / 800.0]


def my_callback(metrics):
	pass


def main():
	fitness_objective = FitnessObjective(calculate_fitness)

	model = Pool(32, size=50, initializer="random")
	model.add(EliteSelection(n_elites=4))
	model.add(Crossover())
	model.add(Mutation(p=0.2))
	model.compile(objective=fitness_objective, metrics=Matplotlib())
	model.summary()
	model.fit(iterations=200, perfect_solution_score_threshold=0.99999999, periodic_callback_fn=my_callback,
	          verbose=True)
	result = model.evaluate()

	print(result)


if __name__ == "__main__":
	main()
