import samples


#vertex inputs
v1,v2 = input("Insira os vértices: ").split()
allPaths =[]
newPath = ""

def DFSvisit(vertex):
  global v2, v1, newPath, allPaths
  newPath += vertex.name

  for v in vertex.adj:
    if v.name == v2:
      allPaths.append(newPath+v2)

    else:
      DFSvisit(v)
  
  newPath = newPath[:-1]


vertexList = samples.g228


for vertex in vertexList:
  if vertex.name == v1:
    DFSvisit(vertex);
  

print(len(allPaths),"caminhos. São eles:")
print(str(allPaths)[1:-1])
