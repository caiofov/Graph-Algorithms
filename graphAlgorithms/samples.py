from .structs import *

#Figure 22.2
S222 = Vertice("S");
R222 = Vertice("R");
T222 = Vertice("T");
U222 = Vertice("U");
V222 = Vertice("V");
W222 = Vertice("W");
X222 = Vertice("X");
Y222 = Vertice("Y");
S222.setAdj([R222,W222])
R222.setAdj([S222,V222])
T222.setAdj([S222,W222,X222])
U222.setAdj([T222,X222,Y222])
V222.setAdj([R222])
W222.setAdj([S222,T222,X222])
X222.setAdj([W222,Y222,T222,U222])
Y222.setAdj([X222,U222])
g222 = Graph(name="Figure 22.2", vertexList = [S222,R222,T222,U222,V222,W222,X222,Y222])
g222.initializeEdges()

#Figure 22.4
U224 = Vertice("U")
V224 = Vertice("V")
W224 = Vertice("W")
X224 = Vertice("X")
Y224 = Vertice("Y")
Z224 = Vertice("Z")
U224.setAdj([V224,X224])
V224.setAdj([Y224])
W224.setAdj([Y224,Z224])
X224.setAdj([V224])
Y224.setAdj([X224])
Z224.setAdj([Z224])
g224 = Graph(name = "Figure 22.4", vertexList = [U224,V224,W224,X224,Y224,Z224])


#figure 22.6
Q226 = Vertice("Q");
R226 = Vertice("R");
S226 = Vertice("S");
T226 = Vertice("T");
U226 = Vertice("U");
V226 = Vertice("V");
W226 = Vertice("W");
X226 = Vertice("X");
Y226 = Vertice("Y");
Z226 = Vertice("Z");
Q226.setAdj([S226,W226, T226])
R226.setAdj([U226,Y226])
S226.setAdj([V226])
T226.setAdj([X226, Y226])
U226.setAdj([Y226])
V226.setAdj([W226])
W226.setAdj([S226])
X226.setAdj([Z226])
Y226.setAdj([Q226])
Z226.setAdj([X226])
g226 = Graph(name="Figure 22.6",vertexList=[Q226,R226,S226,T226,U226,V226,W226,X226,Y226,Z226])


#figure 22.8
M228 = Vertice("M");
N228 = Vertice("N");
O228 = Vertice("O");
P228 = Vertice("P");
Q228 = Vertice("Q");
R228 = Vertice("R");
S228 = Vertice("S");
T228 = Vertice("T");
U228 = Vertice("U");
V228 = Vertice("V");
W228 = Vertice("W");
X228 = Vertice("X");
Y228 = Vertice("Y");
Z228 = Vertice("Z");
M228.setAdj([Q228,R228,T228])
N228.setAdj([O228,Q228,U228])
O228.setAdj([R228, S228, V228])
P228.setAdj([O228,S228,Z228])
Q228.setAdj([T228])
R228.setAdj([U228,Y228])
S228.setAdj([R228])
U228.setAdj([T228])
V228.setAdj([W228,X228])
W228.setAdj([Z228])
Y228.setAdj([V228])
g228 = Graph(name = "Figure 22.8", vertexList = [M228,N228,O228,P228,Q228,R228,S228,T228,U228,V228,W228,X228,Y228,Z228])

#Figure 22.9 - NOT FINISHED
A229 = Vertice("A")
B229 = Vertice("B")
C229 = Vertice("C")
D229 = Vertice("D")
E229 = Vertice("E")
F229 = Vertice("F")
G229 = Vertice("G")
H229 = Vertice("H")

g229 = Graph(name="Figure 22.9",vertexList =[A229,B229,C229,D229,E229,F229,G229,H229])