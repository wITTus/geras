import random
import sys

from tqdm import tqdm


def create_random_individual(n_genes):
	return ''.join([str(random.randint(0, 1)) for _ in range(n_genes)])


def create_random_individuals(n, n_genes):
	return [create_random_individual(n_genes) for _ in range(n)]


class Pool:
	layers = []

	def __init__(self, n_genes, size=250, initializer="random"):

		if initializer == 'random':
			self.pool = create_random_individuals(size, n_genes)
		elif initializer == 'zero':
			self.pool = ['0' * n_genes] * size
		elif initializer == 'one':
			self.pool = ['1' * n_genes] * size

		self.objective_scores = []
		self.iterations_done = 0
		self.objective = None
		self.metrics = None

	def add(self, layer):
		self.layers.append(layer)

	def compile(self, objective, metrics):
		self.objective = objective
		self.metrics = metrics

	def summary(self):
		line_length = 65
		print '_' * line_length
		print 'Layer (type)'
		print '=' * line_length
		for i, layer in enumerate(self.layers):
			layer.summary()
			if i != len(self.layers) - 1:
				print '_' * line_length
		print '=' * line_length

	def fit(self, iterations=1000000, perfect_solution_score_threshold=1.0, new_best_callback_fn=None):

		print('\nEvolving for {} iterations or max score of {}'.format(iterations, perfect_solution_score_threshold))
		print

		dynasty_best = 0

		for _ in tqdm(range(iterations), unit=' Generations', file=sys.stdout):
			self.objective_scores = self.objective.score(self.pool)

			generation_best = max(self.objective_scores)

			if new_best_callback_fn is not None and generation_best > dynasty_best:
				dynasty_best = generation_best
				new_best_callback_fn(self.metrics.apply(self.pool, self.objective_scores))

			if self.objective.reached_perfect_solution(self.objective_scores, perfect_solution_score_threshold):
				break

			new_pool = []
			for layer in self.layers:
				new_pool = layer.call(self.pool, new_pool, self.objective_scores)

			assert len(self.pool) == len(new_pool)
			self.pool = new_pool
			self.iterations_done += 1

		print

	def evaluate(self):
		best_score = max(self.objective_scores)
		best_idx = self.objective_scores.index(best_score)
		best_individual = self.pool[best_idx]

		return {  #
			'best_score': best_score,  #
			'best_individual': best_individual,  #
			'iterations_done': self.iterations_done,  #
			'pool': self.pool,  #
			'scores': self.objective_scores  #
		}  #
