from graphAlgorithms import *


graph = samples.g231



mst = graph.kruskalMinimumSpanningTree()

print()
mst.displayEdges()
mst.display()


print(len(mst.edgesList))

