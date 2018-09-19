import matplotlib.pyplot as plt

class Matplotlib:
	def __init__(self):
		pass

	def apply(self, pool, scores):

		# Pool Fitness Landscape
		plt.clf()
		plt.ylim(0, 1.0)
		plt.plot(scores)
		plt.pause(1e-17)
