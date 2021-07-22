from graphAlgorithms import *


graph = samples.g231

# for edge in graph.edgesList:
#   v,u = edge.endpoints
#   print(v.name, " - ", u.name, "|", edge.weight)


mst = graph.kruskalMinimumSpanningTree()
<<<<<<< HEAD

print()
mst.displayEdges()
mst.display()


print(len(mst.edgesList))
=======
>>>>>>> origin/master


for edge in mst.edgesList:
  v,u = edge.endpoints
  print(v.name, " - ", u.name, "|", edge.weight)