while len(fila_Q)>0:
  u = fila_Q[0];
  fila_Q = fila_Q[1:];

  for v in u.adj:
    u.out_degree +=1
    v.in_degree +=1
   
    if v.cor == "branca":
      v.pai = u;

      v.d = u.d + 1
      v.cor = "cinza"
      fila_Q.append(v)

    u.cor = "preta"