class Vertice:
  def __init__(self, name = None):
    self.color = "WHITE";
    self.parent = None;
    self.adj = [];
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