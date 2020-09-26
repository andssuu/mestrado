from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo
from lista_adjacencias import ListaAdjacencias

if __name__ == "__main__":
    V = [x for x in range(0, 8)]
    E = [[1, 2], [2, 3], [2, 4], [4, 5], [5, 6], [3, 7]]
    # Matriz adjacencias
    G = MatrizAdjacencias(V, E)
    print("Matriz de adjacencias: ")
    [print(x) for x in G.matriz[1:]]
    s, v = 2, 7
    G.busca_largura(G.V[s])
    print("Caminho v-s: ", [
          l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    # Distancia para grafo nao ponderado com matriz de adjacencias
    G = MatrizAdjacencias(V[:], E[:])  # resetanto grafo
    G.busca_largura_distancia(G.V[s])
    print("Caminho com distancia entre vertices v-s: ",
          [[l.valor, l.distancia] for l in G.constroi_caminho(G.V[s], G.V[v])])
    V = [x for x in range(0, 10)]
    E = [[8, 6], [8, 3], [8, 1], [8, 7], [8, 5], [6, 9], [6, 2],
         [6, 3], [2, 1], [2, 5], [1, 5], [5, 4], [4, 3]]
    G = MatrizAdjacencias(V, E)
    s, v = 8, 9
    G.busca_prof_iterativa(G.V[s])
    print("Busca profundidade iterativa : ",
          [l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    G = MatrizAdjacencias(V[:], E[:])
    G.busca_prof_recursiva(G.V[s])
    print("Busca profundidade recursiva : ",
          [l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    G = MatrizAdjacencias(V, E)
    G.busca_profundidade(G.V[s])
    print("Ordem de descoberta:")
    print("\tLista pre-ordem: ", [g.valor for g in G.pre_ordem])
    print("\tLista pos-ordem: ", [g.valor for g in G.pos_ordem])
    print("\tLista pos-ordem reversa: ",
          [g.valor for g in G.pos_ordem_reversa])
    G = MatrizAdjacencias(V, E)
    print("Numero de componentes: ", G.busca_componente())
    # busca em digrafos
    V = [x for x in range(0, 7)]
    E = [[1, 2], [2, 3], [2, 4], [3, 5], [3, 6]]
    G_digrafo = MatrizAdjacenciasDigrafo(V, E)
    s, v = 2, 6
    print("Matriz de adjacencias digrafo: ")
    [print(x) for x in G_digrafo.matriz[1:]]
    G_digrafo.busca_largura(G_digrafo.V[s])
    print("Busca largura em digrafo : ",
          [l.valor for l in G_digrafo.constroi_caminho(G_digrafo.V[s],
                                                       G_digrafo.V[v])])
    G_digrafo = MatrizAdjacenciasDigrafo(V, E)
    G_digrafo.busca_profundidade(G_digrafo.V[s])
    print("Busca profundidade em digrafo : ",
          [l.valor for l in G_digrafo.constroi_caminho(G_digrafo.V[s],
                                                       G_digrafo.V[v])])
    G_digrafo = MatrizAdjacenciasDigrafo(V, E)
    print("Matriz de adjacencias digrafo: ")
    [print(x) for x in G_digrafo.matriz[1:]]
    # print(G_digrafo.E)
    G_digrafo_reverso = MatrizAdjacenciasDigrafo.reverso(G_digrafo)
    print("Matriz de adjacencias digrafo reverso: ")
    [print(x) for x in G_digrafo_reverso.matriz[1:]]
    # print(G_digrafo_reverso.E)

    G_digrafo = MatrizAdjacenciasDigrafo(V, E)
    G_digrafo.componentes_fortemente_conexas()
    [print(x.componente) for x in G_digrafo.V]
#    print("Ordenacao topologica : ", [
#          n.valor for n in G_digrafo.ordenacao_topologica()])

# Lista de adjacencias
# G = ListaAdjacencias(V[:], E[:])
# print(G.lista[1:])
# G.busca_largura(G.V[2])
# print([l.valor for l in G.constroi_caminho(G.V[2], G.V[7])])
# # Distancia para grafo nao ponderado com matriz de adjacencias
# G = ListaAdjacencias(V[:], E[:])
# G.busca_largura_distancia(G.V[2])
# print([[l.valor, l.distancia] for l in G.constroi_caminho(G.V[2], G.V[7])])
