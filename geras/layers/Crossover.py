import heapq
import random


def roulette_wheel_selection(scores):
	r_pos = random.uniform(0, sum(scores))
	c_pos = 0
	for idx, score in enumerate(scores):
		c_pos += score
		if r_pos <= c_pos:
			return idx


def roulette_wheel_selection2(scores):
	idx1 = roulette_wheel_selection(scores)
	idx2 = roulette_wheel_selection(scores)

	return idx1, idx2


def crossover(individual1, individual2):
	assert len(individual1) == len(individual2)
	assert len(individual1) % 2 == 0
	assert len(individual1) > 1 and len(individual2) > 1

	genes_first_half = random.randint(1, len(individual1) - 2)

	new1 = individual1[:genes_first_half] + individual2[genes_first_half:]
	new2 = individual2[:genes_first_half] + individual1[genes_first_half:]

	return new1, new2


def crossover_pool(pool, scores, new_pool_size):
	assert new_pool_size % 2 == 0

	new_pool = []
	for _ in range(new_pool_size / 2):
		idx1, idx2 = roulette_wheel_selection2(scores)
		new1, new2 = crossover(pool[idx1], pool[idx2])
		new_pool.append(new1)
		new_pool.append(new2)
	return new_pool


class Crossover:
	def __init__(self, n_elites=4):
		self.n_elites = n_elites

	def call(self, pool, scores):
		pool_size = len(pool)
		elite_pool = [pool[idx] for idx in map(scores.index, heapq.nlargest(self.n_elites, scores))]
		new_pool = elite_pool + crossover_pool(pool, scores, pool_size - self.n_elites)

		return new_pool

	def summary(self):
		print 'Crossover'
