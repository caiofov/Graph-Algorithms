import Graph as gp
import DFS

isSemiconnected = True


a = gp.Vertex("a")
b = gp.Vertex("b")
c = gp.Vertex("c")
b.setAdj([a])
c.setAdj([b])
graph = [a,b,c]

def initialize(graph):
  for vertex in graph:
    vertex.color = "WHITE";
    vertex.parent = None;

#DFS
for vertex in graph:
  if vertex.color == "WHITE":
    initialize(graph)
    DFS.DFSvisit(vertex);

for v in graph:
  if v.color =="WHITE":
    isSemiconnected = False

print(isSemiconnected)