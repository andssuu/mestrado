from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo
# from lista_adjacencias import ListaAdjacencias, ListaAdjacenciasDigrafo

if __name__ == "__main__":
    print('''
    #############################################

        Implementações com Matriz de Adjacências

    #############################################
    ''')
    V = [x for x in range(10)]
    E = [[2, 1, 8], [2, 7, 3], [3, 5, 8], [4, 1, 1], [4, 8, 2], [5, 1, 9], [5, 4, 5], [5, 6, 1],
         [6, 3, 2], [6, 8, 3], [6, 9, 7], [7, 3, 0], [7, 5, 1], [8, 5, 1], [8, 9, 3]]
    G = MatrizAdjacenciasDigrafo(V, E)
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Dijkstra <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.dijkstra(G.V[6])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Dijkstra com Heap <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.dijkstra_heap(G.V[6])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Bellman-Ford <<<<<<<<<<<<<<<<<<<<<<<<<")
    E = [[2, 1, 8], [2, 7, -3], [3, 5, -4], [4, 1, -10], [4, 8, 2], [5, 1, -9], [5, 4, 5], [5, 6, 11],
         [6, 3, 2], [6, 8, 3], [6, 9, 4], [7, 3, 0], [7, 5, 1], [8, 5, -6], [8, 9, 0]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.bellman_ford(G.V[6])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Bellman-Ford com ciclo <<<<<<<<<<<<<<<<<<<<<<<<<")
    # add ciclo negativo no digrafo e verificando se o algoritmo consegue detectar
    E = [[2, 1, 8], [2, 7, -3], [3, 5, -4], [4, 1, -10], [4, 8, -2], [5, 1, -9], [5, 4, 5], [5, 6, 11],
         [6, 3, 2], [6, 8, 3], [6, 9, 4], [7, 3, 0], [7, 5, 1], [8, 5, -6], [8, 9, 0]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.bellman_ford(G.V[6])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Caminho <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 3], [2, 3, 2], [2, 4, -1], [3, 1, 1],
         [3, 4, -3], [3, 5, 1], [4, 2, 4], [5, 4, -2]]
    G = MatrizAdjacenciasDigrafo(V, E)
    i, j = 3, 2
    print("Custo mímino para {}-{} caminho: {}".format(
        i, j, G.caminho(i, j, [x.valor for x in G.V[1:] if x.valor != i and x.valor != j])))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Top Down <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.floyd_warshall_top_down()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j[-1]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Bottom Up <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.floyd_warshall_bottom_up()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j[-1]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Melhorado <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.floyd_warshall_melhorado()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Resolve Caminhos Entre Todos Pares sem ciclo negativo  <<<<<<<<<<<<<<<<<<<<<<<<<")
    ciclo = G.resolve_caminhos_todos_pares()
    if ciclo is None:
        print("Há ciclo negativo no digrafo")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Resolve Caminhos Entre Todos Pares com ciclo negativo  <<<<<<<<<<<<<<<<<<<<<<<<<")
    # add ciclo negativo
    _V = [x for x in range(6)]
    _E = [[1, 2, 3], [2, 3, 2], [2, 4, -1], [3, 1, 1],
          [3, 4, -3], [3, 5, 1], [4, 2, -4], [5, 4, -2]]
    _G = MatrizAdjacenciasDigrafo(_V, _E)
    ciclo = _G.resolve_caminhos_todos_pares()
    if ciclo is None:
        print("Há ciclo negativo no digrafo")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Constrói Caminho <<<<<<<<<<<<<<<<<<<<<<<<<")
    # construindo sv-caminho
    G = MatrizAdjacenciasDigrafo(V, E)
    G.floyd_warshall_melhorado()
    s, v = G.V[5], G.V[1]
    print("{}-{} caminho:".format(s.valor, v.valor), end=" ")
    [print(v.valor, end=" ") for v in G.constroi_caminho(s, v)]
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>> Johnson  <<<<<<<<<<<<<<<<<<<<<<<<<")
    G = MatrizAdjacenciasDigrafo(V, E)
    G.johnson()
    if not G.ciclo_negativo:
        for v in G.V[1:]:
            print("Custos para o vértice {}".format(v.valor))
            for _m, j in enumerate(v.distancias[1:]):
                print("Menor custo para sair de {} para {}: {}".format(
                    v.valor, _m+1, j))
