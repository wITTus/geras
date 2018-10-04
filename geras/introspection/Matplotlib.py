import matplotlib.pyplot as plt
import numpy as np


class Matplotlib:
	def __init__(self):
		self.historical_scores_max = []
		self.historical_scores_avg = []

	def apply(self, pool, scores):
		plt.clf()
		plt.subplots_adjust(hspace=0.5)

		# Pool Fitness Landscape
		plt.subplot(2, 1, 1)
		plt.title('Pool Fitness Landscape')
		plt.xlabel('Individual')
		plt.ylabel('Fitness')
		plt.ylim(0, 1.0)
		plt.plot(scores)

		# Learning Curve
		plt.subplot(2, 1, 2)
		plt.title('Learning Curve')
		plt.xlabel('(Plotting) Iteration')
		plt.ylabel('Fitness')
		plt.ylim(0, 1.0)
		plt.plot(self.historical_scores_max, label='max')
		plt.plot(self.historical_scores_avg, label='avg')
		plt.legend()

		plt.pause(1e-17)

		generation_best = max(scores)
		generation_best_idx = scores.index(generation_best)
		generation_best_individual = pool[generation_best_idx]
		generation_avg = np.mean(scores)

		self.historical_scores_max.append(generation_best)
		self.historical_scores_avg.append(generation_avg)

		print
		print '================'
		print 'Best Individual:', generation_best_individual
		print 'Best Score:', generation_best
		print '================'

		return plt
