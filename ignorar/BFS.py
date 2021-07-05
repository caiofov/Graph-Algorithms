import Graph as gp
#inicializando
graph = []
fila_Q = []
S = graph.pop()
S.distance = 0
S.color = "GRAY"
fila_Q.append(S)


while len(fila_Q)>0:
  u = fila_Q[0];
  fila_Q = fila_Q[1:];

  for v in u.adj:
    u.out_degree +=1
    v.in_degree +=1
   
    if v.color == "WHITE":
      v.parent = u;

      v.distance = u.distance + 1

      v.color = "GRAY"
      fila_Q.append(v)

    u.cor = "BLACK"
