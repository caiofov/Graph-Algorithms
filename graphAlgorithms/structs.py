import copy


class Graph:
  def __init__(self, name = None, vertexList = []):
    self.name = name
    self.vertexList = vertexList
  

  def setVertex(self, list):
    self.vertexList = list
  
 
  def appendVertice(self, vertice):
    self.vertexList.append(vertice)

 
  def topologicalSort(self):
    return sorted(self.vertexList, reverse=True,key=lambda x: x.secondTimestamp)
    

  def initializeVertex(self):
    for vertice in self.vertexList:
      vertice.color = "WHITE";
      vertice.parent = None;
      vertice.distance = None


  def setVertexDegrees(self):
    for vertice in self.vertexList:
      for ad in vertice.adj:
        vertice.outDegree +=1
        ad.inDegree +=1
  

  def transposed(self, transposedName = None):
    transposedGraph = Graph(name = self.name + "transposed")

    if transposedName:
      transposedGraph.name = transposedName

    for vertice in self.vertexList:
      newVertice = copy.deepcopy(vertice)
      newVertice.setAdj([])
      transposedGraph.append(newVertice)

    for v in self.vertexList:
      for i in v.adj:
        idx = self.vertexList.index(i)
        transposedGraph.vertexList[idx].appendAdjacentVertice(v)

    return transposedGraph


  def stronglyConnectedComponents(self):
    self.depthFirstSearch()
    Gt = self.getTransposed()
    Gt_sorted = Gt.topologicalSort()
  
    return Gt_sorted.depthFirstSearch(returnTree=True)
  

  def breadthFirstSearch(self, returnTree = False):
    self.initializeVertex()
    queue = []
    tree = []
    
    S = self.vertexList[0]
    S.distance = 0
    S.color = "GRAY"
    queue.append(S)


    while len(queue)>0:
      u = queue[0];
      queue = queue[1:];
      tree.append(u)

      for v in u.adj:
      
        if v.color == "WHITE":
          v.parent = u;

          v.distance = u.distance + 1

          v.color = "GRAY"
          queue.append(v)

        u.color = "BLACK"

    if returnTree:
      return tree


  def depthFirstSearch(self, returnTree = False):
    time = 0
    searchedForest = []
    searchingTree = []
    self.initializeVertex()
    
    for vertice in self.vertexList:
      if vertice.color == "WHITE":
        searchingTree, time = DFSvisit(vertice,searchingTree,time);
      
      if len(searchingTree) > 0:
        searchedForest.append(searchingTree)
        searchingTree = []

    if returnTree: return searchedForest


  def display(self, name = True, color = True, inDegree = True,outDegree = True, distance = True, firstTimestamp = True, secondTimestamp = True):

		
		for v in self.vertexList:
    	if name:
        print("Name:", v.name, end=' ')
      if color:
        print("|Color:", v.color, end=' ')
      if outDegree:
        print("|Out-degree:", v.outDegree, end=' ')
      if inDegree:
        print("| In-degree:", v.inDegree, end=' ')
      if distance:
        print("| Distance from the source:",v.distance, end=' ')
      if firstTimestamp:
        print("| 1st Timestamp:",v.firstTimestamp, end=' ')
      if secondTimestamp:
        print("| 2nd Timestamp:", v.secondTimestamp, end=' ')
      print("\n")
    



def DFSvisit(vertice,searchingTree, time): #visit function
  time += 1
  vertice.color = "GRAY"
  vertice.firstTimestamp = time

  searchingTree.append(vertice)

  for v in vertice.adj:
    if v.color == "WHITE":
      v.parent = vertice;
      searchingTree, time = DFSvisit(v,searchingTree, time)
  
  vertice.color = "BLACK"
  time +=1
  vertice.secondTimestamp = time

  return searchingTree, time



class Vertice:
  def __init__(self, name = None, adj = []):
    self.color = "WHITE";
    self.parent = None;
    self.adj = adj;
    self.distance = 0;
    self.outDegree = 0;
    self.inDegree = 0;
    self.name = name;
    self.firstTimestamp = 0;
    self.secondTimestamp = 0;

  def setAdj(self, adj):
    self.adj = adj;
  
  def appendAdjacentVertice(self, vertice):
    self.adj.append(vertice)