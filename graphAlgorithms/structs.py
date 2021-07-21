import copy

def DFSvisit(vertice,searchingTree, time): #visit function
    time += 1
    vertice.color = "GRAY"
    vertice.firstTimestamp = time

    searchingTree.appendVertice(vertice)

    for v in vertice.adj:
      if v.color == "WHITE":
        v.parent = vertice;
        searchingTree, time = DFSvisit(v,searchingTree, time)

    vertice.color = "BLACK"
    time += 1
    vertice.secondTimestamp = time

    return searchingTree, time

def union(graph1, graph2, edge, directed = False):#union function
  v1,v2 = edge

  v1.appendAdjacentVertice(v2)
  if not directed:
    v2.appendAdjacentVertice(v1)
  
  name = graph1.name + " U " + graph2.name
  vertexList = graph1.vertexList + graph2.vertexList


  newGraph = Graph(name, vertexList, directed)
  newGraph.addEdge(edge)

  
  return newGraph

class Graph:
  def __init__(self, name = None, vertexList = [], edgeList = [], directed = None):
    self.name = name #string
    self.vertexList = vertexList #list
    self.edgesList = edgeList #list
    self.directed = directed #boolean

    self.initializeAll()

  def initializeAll(self):
    self.initializeVertex()
    self.initializeEdges()
    self.setVertexDegrees()
 

  def setVertex(self, list):
    self.vertexList = list
  def setEdges(self, list):
    self.edgesList = list
  def appendVertice(self, vertice):
    self.vertexList.append(vertice)
  
  def initializeVertex(self):
    for vertice in self.vertexList:
      vertice.color = "WHITE";
      vertice.parent = None;
      vertice.distance = None
      vertice.inDegree = 0
      vertice.outDegree = 0
      vertice.initializeVertexWeight()
    
    
  def setVertexDegrees(self):
    for vertice in self.vertexList:
      vertice.setDegrees()
  def addEdge(self,edge):
    self.edgesList.append(edge)
    u,v = edge.endpoints

    if not u in self.vertexList:
      self.vertexList.append(u)
    if not v in self.vertexList:
        self.vertexList.append(u)
    
    if not u in v.adj:
      v.appendAdjacentVertice(u)
      v.adjWeight.append(edge.weight)

    if not u in v.adj and not edge.directed:
      v.appendAdjacentVertice(u)
      v.adjWeight.append(edge.weight)
      
  

  def initializeEdges(self):
    self.edgesList = []

    for vertex in self.vertexList:
      idx = 0

      for adj in vertex.adj:
       
        if not any(edge.endpoints == [vertex, adj] or edge.endpoints == [adj,vertex] for edge in self.edgesList):
          self.edgesList.append(Edge([vertex, adj], vertex.adjWeight[idx], self.directed))
      
        

        idx += 1

  def topologicalSort(self):
    return sorted(self.vertexList, reverse=True,key=lambda x: x.secondTimestamp)

  def getTransposed(self, transposedName = None):
    transposedGraph = Graph(name = self.name + " transposed")

    if transposedName:
      transposedGraph.name = transposedName

    for vertice in self.vertexList:
      newVertice = copy.deepcopy(vertice)
      newVertice.setAdj([])
      transposedGraph.appendVertice(newVertice)

    for v in self.vertexList:
      for i in v.adj:
        idxi = self.vertexList.index(i)
        idxv = self.vertexList.index(v)
        transposedV = transposedGraph.vertexList[idxv]
       
        transposedGraph.vertexList[idxi].appendAdjacentVertice(transposedV)

    return transposedGraph


  def stronglyConnectedComponents(self):
    self.depthFirstSearch()
    Gt = self.getTransposed()
    Gt_sorted = Graph(name= Gt.name + " topological sorted", vertexList = Gt.topologicalSort())

    return Gt_sorted.depthFirstSearch(returnTree=True)

  def getComponents(self):
    return self.depthFirstSearch(returnTree = True);

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
    searchingTree = Graph("Searching tree")
    self.initializeVertex()
    
    for vertice in self.vertexList:
      if vertice.color == "WHITE":
        searchingTree, time = DFSvisit(vertice,searchingTree,time);
      
      if len(searchingTree.vertexList) > 0:
        searchedForest.append(searchingTree)
        searchingTree = Graph("Searching tree")

    if returnTree:
      return searchedForest


  def display(self, name = True, color = False, inDegree = False,outDegree = False, distance = False, firstTimestamp = False, secondTimestamp = False):
    print("Graph: ", self.name)
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

  def componentForEachVertice(self, components):
    for component in components:
      for vertex in component.vertexList:
        vertex.setSet(component)

  def kruskalMinimumSpanningTree(self):
    components = self.getComponents()
    self.componentForEachVertice(components)

    if len(self.edgesList) == 0:
      self.initializeEdges()
    self.edgesList = sorted(self.edgesList, key=lambda x: x.weight)

    A = Graph("Subset",directed = self.directed)
    
    numEgdes = len(self.edgesList)
    numVertices = len(self.vertexList)
    i = 0

    while i <= numEgdes and len(A.vertexList) < numVertices - 1:
      edge = self.edgesList[i].endpoints
      u,v = edge

      if u.set != v.set:
        A.addEdge(edge)
        newComponent = union(u.set,v.set, edge, self.directed, returnGraph = False)

        u.setSet(newComponent)
        v.setSet(newComponent)

      i+=1

    return A
  
    




class Vertice:
  def __init__(self, name = None, adj = [], weight = []):
    self.color = "WHITE"; #string
    self.parent = None; #vertice
    self.adj = adj; #list
    self.adjWeight = weight; #list
    self.distance = 0; #int
    self.outDegree = 0; #int
    self.inDegree = 0; #int
    self.name = name; #string
    self.firstTimestamp = 0; #int
    self.secondTimestamp = 0; #Int
    self.set = [] #list

  def setAdj(self, adj, weight = None):
    self.adj = adj;
    if weight:
      self.setAdjWeight(weight)
  def setAdjWeight (self, weight):
    self.adjWeight = weight;
  def setSet(self, component):
    self.set = component

  def appendAdjacentVertice(self, vertice):
    self.adj.append(vertice)
  
  def initializeVertexWeight(self):
    for i in range(len(self.adj) - len(self.adjWeight)):
      self.adjWeight.append(1)
  
  def setDegrees(self):
    for vertice in self.adj:
      self.outDegree +=1
      vertice.inDegree +=1

  

class Edge:
  def __init__(self, endpoints = [], weight = 1, directed = False):
    self.endpoints = endpoints #tuple of vertices
    self.weight = weight #int
    self.directed = directed #boolean

  def setEndpoints(self, endpoints):
    self.endpoints = endpoints
  
  def setWeight(self, weight):
    self.weight = weight
  
  def setdirected(self, directed):
    self.directed = directed
  
  def getEndpoints(self):
    return self.endpoints


