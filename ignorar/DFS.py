
time = 0
searchedForest = []
searchingTree = []

def initialize(graph):
  global time, searchedForest,searchingTree
  time = 0
  searchedForest.clear()
  searchingTree.clear()

  for vertex in graph:
    vertex.color = "WHITE";
    vertex.parent = None;


def DFSvisit(vertex): #visit function
  global searchingTree, time
  time += 1
  vertex.color = "GRAY"
  vertex.firstTimestamp = time

  searchingTree.append(vertex)

  for v in vertex.adj:
    if v.color == "WHITE":
      v.parent = vertex;
      DFSvisit(v)
  
  vertex.color = "BLACK"
  time +=1
  vertex.secondTimestamp = time


def depthFirstSearch(graph, returnTree = False):
  global searchedForest, searchingTree
  initialize(graph)
  
  #DFS
  for vertex in graph:
    if vertex.color == "WHITE":
      DFSvisit(vertex);
    if len(searchingTree) > 0:
      searchedForest.append(searchingTree)
      searchingTree = []

  if returnTree: return searchedForest