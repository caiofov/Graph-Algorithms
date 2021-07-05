from .structs import *

#Figure 22.2
S = Vertice("S");
R = Vertice("R");
T = Vertice("T");
U = Vertice("U");
V = Vertice("V");
W = Vertice("W");
X = Vertice("X");
Y = Vertice("Y");
S.setAdj([R,W])
R.setAdj([S,V])
T.setAdj([S,W,X])
U.setAdj([T,X,Y])
V.setAdj([R])
W.setAdj([S,T,X])
X.setAdj([W,Y,T,U])
Y.setAdj([X,U])
g222 = Graph(name="Figure 22.2", vertexList = [S,R,T,U,V,W,X,Y])

#Figure 22.4
U = Vertice("U")
V = Vertice("V")
W = Vertice("W")
X = Vertice("X")
Y = Vertice("Y")
Z = Vertice("Z")
U.setAdj([V,X])
V.setAdj([Y])
W.setAdj([Y,Z])
X.setAdj([V])
Y.setAdj([X])
Z.setAdj([Z])
g224 = Graph(name = "Figure 22.4", vertexList = [U,V,W,X,Y,Z])


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

