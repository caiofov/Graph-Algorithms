from graphAlgorithms import *


graph = samples.g224


stro = graph.stronglyConnectedComponents()

for i in stro:
	for t in i:
		print(t.name, end='')
	print()

