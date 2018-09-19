import random


def flip_string_bit(s):
	return str(int(not (bool(int(s)))))


def random_index(o):
	return random.randint(0, len(o) - 1)


def mutate_individual(individual):
	idx = random_index(individual)
	l = list(individual)
	l[idx] = flip_string_bit(individual[idx])
	return ''.join(l)


def mutate_pool(pool, rate):
	return [mutate_individual(individual) if rate > random.uniform(0, 1) else individual for individual in pool]


class Mutation:
	def __init__(self, p=0.25):
		self.mutation_rate = p
		pass

	def call(self, _, new_pool, __):
		return mutate_pool(new_pool, self.mutation_rate)

	def summary(self):
		print 'Mutation'
