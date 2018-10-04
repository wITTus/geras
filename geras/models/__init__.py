from Pool import *


def load_model(filepath):
	import dill
	with open(filepath, 'r') as fd:
		return dill.load(fd)
