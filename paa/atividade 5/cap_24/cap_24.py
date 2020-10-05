from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo
from lista_adjacencias import ListaAdjacencias, ListaAdjacenciasDigrafo

if __name__ == "__main__":
    print('''
    #############################################

        Implementações com Matriz de Adjacências

    #############################################
    ''')
    V = [x for x in range(12)]
    # conjunto E de arestas com o seus repectivos pesos
    E = [[1, 2, 2], [1, 3, 5], [2, 3, 8], [2, 4, 1], [2, 8, 9], [2, 11, 8],
         [3, 4, 5], [3, 5, 3], [4, 7, 4], [4, 8, 2], [4, 9, 6], [5, 6, 3],
         [6, 9, 4], [7, 10, 3], [7, 11, 1], [9, 11, 9], [10, 11, 2]]
    # Matriz adjacencias
    G = MatrizAdjacencias(V, E)
    print("Matriz de adjacencias: ")
    [print(x[1:]) for x in G.matriz[1:]]
    # F = G.kruskal()
    # [print(x) for x in F]
    # arvore_minima = MatrizAdjacencias(V, F)
    # print("Matriz de adjacencias (Árvore Mínima): ")
    # [print(x[1:]) for x in arvore_minima.matriz[1:]]
    # F = G.kruskal_union_find()
    # [print(x) for x in F]
    # G.prim()
    # G.prim_heap()
    # G.prim_heap()

    V = [x for x in range(9)]
    E = [[1, 2], [1, 4], [2, 5], [3, 1], [3, 5], [4, 5], [5, 1],
         [5, 3], [5, 6], [6, 3], [6, 7], [7, 6], [7, 8], [8, 7]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.fleury(G.V[3]
    # print('''
    # #############################################

    #     Implementações com Lista de Adjacências

    # #############################################
    # ''')

    # V = [x for x in range(10)]
    # E = [[1, 2], [1, 5], [1, 8], [2, 5], [2, 6], [3, 4], [3, 6],
    #      [3, 8], [4, 5], [5, 8], [6, 8], [6, 9], [7, 8]]
    # # Lista de adjacencias
    # G = ListaAdjacencias(V, E)
    # print("Lista de adjacencias: ")
    # [print('Vertice {}: {}'.format(n+1, x)) for n, x in enumerate(G.lista[1:])]
    # s, v = 8, 9
    # G.chama_busca(G.V[s], tipo_busca='largura')
    # print("Caminho s-v: ", [
    #       l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    # # Distancia para grafo nao ponderado com matriz de adjacencias
    # G.chama_busca(G.V[s], tipo_busca='largura_distancia')
    # print("Caminho com distancia entre vertices s-v: ",
    #       [[l.valor, l.distancia] for l in G.constroi_caminho(G.V[s], G.V[v])])
    # G.chama_busca(G.V[s], tipo_busca='profundidade_iterativa')
    # print("Busca profundidade iterativa : ",
    #       [l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    # G.chama_busca(G.V[s], tipo_busca='profundidade_recursiva')
    # print("Busca profundidade recursiva : ",
    #       [l.valor for l in G.constroi_caminho(G.V[s], G.V[v])])
    # G.chama_busca(G.V[s], tipo_busca='profundidade')
    # print("Ordem de descoberta:")
    # print("\tLista pre-ordem: ", [g.valor for g in G.pre_ordem])
    # print("\tLista pos-ordem: ", [g.valor for g in G.pos_ordem])
    # print("\tLista pos-ordem reversa: ",
    #       [g.valor for g in G.pos_ordem_reversa])
    # print("Numero de componentes: ", G.chama_busca(tipo_busca='componentes'))
    # # busca em digrafos
    # V = [x for x in range(9)]
    # E = [[1, 2], [1, 4], [2, 4], [2, 5], [3, 1], [3, 5], [4, 5],
    #      [5, 1], [6, 3], [6, 7], [7, 8], [8, 7]]
    # G_digrafo = ListaAdjacenciasDigrafo(V, E)
    # s, v = 3, 1
    # print("Lista de adjacencias digrafo: ")
    # [print('Vertice {}: {}'.format(n+1, x))
    #  for n, x in enumerate(G_digrafo.lista[1:])]
    # G_digrafo.chama_busca(G_digrafo.V[s], tipo_busca='largura')
    # print("Busca largura em digrafo : ",
    #       [l.valor for l in G_digrafo.constroi_caminho(G_digrafo.V[s],
    #                                                    G_digrafo.V[v])])
    # G_digrafo = ListaAdjacenciasDigrafo(V, E)
    # G_digrafo.chama_busca(G_digrafo.V[s], tipo_busca='profundidade')
    # print("Busca profundidade em digrafo : ",
    #       [l.valor for l in G_digrafo.constroi_caminho(G_digrafo.V[s],
    #                                                    G_digrafo.V[v])])
    # G_digrafo_reverso = ListaAdjacenciasDigrafo.reverso(G_digrafo)
    # print("Lista de adjacencias digrafo reverso: ")
    # [print('Vertice {}: {}'.format(n+1, x))
    #  for n, x in enumerate(G_digrafo_reverso.lista[1:])]
    # G_digrafo.componentes_fortemente_conexas()
    # [print("Vertice {} -> Componente {}".format(x.valor, x.componente))
    #  for x in G_digrafo.V[1:]]
    # V = [x for x in range(12)]
    # E = [[1, 2], [1, 5], [2, 3], [2, 6], [2, 8], [4, 8],
    #      [5, 2], [5, 6], [5, 9], [6, 3], [6, 11], [7, 4], [7, 6], [7, 8], [8, 11], [9, 10]]
    # G_digrafo = ListaAdjacenciasDigrafo(V, E)
    # print("Ordenacao topologica : ",
    #       [n.valor for n in G_digrafo.ordenacao_topologica()])
