import grafos as gf


#criar os vertices
um = gf.Vertice("um")
dois = gf.Vertice("dois")
tres = gf.Vertice("tres")
quatro = gf.Vertice("quatro")
cinco = gf.Vertice("cinco")

#definir as adjacencias
um.setAdj([0,0,0,0,0])
dois.setAdj([1,0,1,0,0])
tres.setAdj([1,0,0,1,0])
quatro.setAdj([1,0,0,0,1])
cinco.setAdj([1,1,0,0,0])

#todos os vertices do grafo
todos = [um,dois,tres,quatro,cinco]
sink = gf.Vertice("não achado");

#inicializando
fila_Q = []
dois.d = 0
dois.cor = "cinza"
fila_Q.append(dois)
index = 0

while len(fila_Q)>0:
  u = fila_Q[0]; #pega o primeiro elemento
  fila_Q = fila_Q[1:]; #remove o primeiro elemento
  index = 0 #zera o index
  isSink = True

  for v in u.adj:
    if v==1: #se houver uma ligação
      isSink = False #não é o sink, já que tem 1
      vertice = todos[index]
    
      if vertice.cor == "branca":
        vertice.pai = u; #setta o pai
        vertice.d = u.d + 1 #setta a distancia
        vertice.cor = "cinza" #setta a  cor

        fila_Q.append(vertice)
    
      u.cor = "preta"
    index +=1

    
  if isSink:
    sink = u
    break
    

print("O sink é ", sink.nome);