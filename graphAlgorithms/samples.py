from .structs import *


S = Vertice.Vertice("S");
R = Vertice.Vertice("R");
T = Vertice.Vertice("T");
U = Vertice.Vertice("U");
V = Vertice.Vertice("V");
W = Vertice.Vertice("W");
X = Vertice.Vertice("X");
Y = Vertice.Vertice("Y");

S.setAdj([R,W])
R.setAdj([S,V])
T.setAdj([S,W,X])
U.setAdj([T,X,Y])
V.setAdj([R])
W.setAdj([S,T,X])
X.setAdj([W,Y,T,U])
Y.setAdj([X,U])

g1 = [S,R,T,U,V,W,X,Y]



um = Vertice.Vertice("1");
dois = Vertice.Vertice("2");
tres = Vertice.Vertice("3");
quatro = Vertice.Vertice("4");
cinco = Vertice.Vertice("5");
seis = Vertice.Vertice("6");

um.setAdj([dois,tres])
dois.setAdj([cinco])
tres.setAdj([cinco,seis])
quatro.setAdj([dois])
cinco.setAdj([quatro])
seis.setAdj([seis])

g2 = [um, dois, tres, quatro, cinco, seis]


#figure 22.6
Q226 = Vertice.Vertice("Q");
R226 = Vertice.Vertice("R");
S226 = Vertice.Vertice("S");
T226 = Vertice.Vertice("T");
U226 = Vertice.Vertice("U");
V226 = Vertice.Vertice("V");
W226 = Vertice.Vertice("W");
X226 = Vertice.Vertice("X");
Y226 = Vertice.Vertice("Y");
Z226 = Vertice.Vertice("Z");

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

g226 = [Q226,R226,S226,T226,U226,V226,W226,X226,Y226,Z226]


#figure 22.8
M228 = Vertice.Vertice("M");
N228 = Vertice.Vertice("N");
O228 = Vertice.Vertice("O");
P228 = Vertice.Vertice("P");
Q228 = Vertice.Vertice("Q");
R228 = Vertice.Vertice("R");
S228 = Vertice.Vertice("S");
T228 = Vertice.Vertice("T");
U228 = Vertice.Vertice("U");
V228 = Vertice.Vertice("V");
W228 = Vertice.Vertice("W");
X228 = Vertice.Vertice("X");
Y228 = Vertice.Vertice("Y");
Z228 = Vertice.Vertice("Z");

M228.setAdj([Q228,R228,T228])
N228.setAdj([O228,Q228,U228])
O228.setAdj([R228, S228, V228])
P228.setAdj([O228,S228,Z228])
Q228.setAdj([T228])
R228.setAdj([U228,Y228])
S228.setAdj([R228])
T228.setAdj([])
U228.setAdj([T228])
V228.setAdj([W228,X228])
W228.setAdj([Z228])
X228.setAdj([])
Y228.setAdj([V228])
Z228.setAdj([])

g228 = [M228,N228,O228,P228,Q228,R228,S228,T228,U228,V228,W228,X228,Y228,Z228]
