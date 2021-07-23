from graphAlgorithms import *


graph = samples.g231


kruskal = graph.kruskalMinimumSpanningTree()
kruskal.displayEdges()

prim = graph.primMinimumSpanningTree()
prim.displayEdges()