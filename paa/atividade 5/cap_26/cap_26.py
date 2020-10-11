from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo

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
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Dijkstra (26.1) <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.dijkstra(G.V[2])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Dijkstra com Heap (26.2) <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.dijkstra_heap(G.V[5])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Bellman-Ford (26.3) <<<<<<<<<<<<<<<<<<<<<<<<<")
    E = [[2, 1, 8], [2, 7, -3], [3, 5, -4], [4, 1, -10], [4, 8, 2], [5, 1, -9], [5, 4, 5], [5, 6, 11],
         [6, 3, 2], [6, 8, 3], [6, 9, 4], [7, 3, 0], [7, 5, 1], [8, 5, -6], [8, 9, 0]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.bellman_ford(G.V[5])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Bellman-Ford com ciclo (26.3) <<<<<<<<<<<<<<<<<<<<<<<<<")
    # add ciclo negativo no digrafo e verificando se o algoritmo consegue detectar
    E = [[2, 1, 8], [2, 7, -3], [3, 5, -4], [4, 1, -10], [4, 8, -2], [5, 1, -9], [5, 4, 5], [5, 6, 11],
         [6, 3, 2], [6, 8, 3], [6, 9, 4], [7, 3, 0], [7, 5, 1], [8, 5, -6], [8, 9, 0]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.bellman_ford(G.V[5])
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Caminho (26.4) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    i, j = 1, 5
    print("Custo mímino para {}-{} caminho: {}".format(
        i, j, G.caminho(i, j, [x.valor for x in G.V[1:] if x.valor != i and x.valor != j])))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Top Down (26.5) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.floyd_warshall_top_down()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j[-1]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Bottom Up (26.7) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.floyd_warshall_bottom_up()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j[-1]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Floyd Warshall Melhorado (26.8) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.floyd_warshall_melhorado()
    for _n, i in enumerate(G.W[1:]):
        print("Custos para o vértice {}".format(_n+1))
        for _m, j in enumerate(i[1:]):
            print("Menor custo para sair de {} para {}: {}".format(
                _n+1, _m+1, j))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Resolve Caminhos Entre Todos Pares (26.9) sem ciclo negativo   <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    ciclo = G.resolve_caminhos_todos_pares()
    print("Há ciclo de peso total negativo no digrafo") if ciclo is None else print(
        "Não há ciclo de peso total negativo no digrafo")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Resolve Caminhos Entre Todos Pares (26.9) com ciclo negativo  <<<<<<<<<<<<<<<<<<<<<<<<<")
    # add ciclo negativo
    _V = [x for x in range(6)]
    _E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
          [3, 4, -6], [3, 5, 2], [4, 2, -8], [5, 4, -4]]
    _G = MatrizAdjacenciasDigrafo(_V, _E)
    ciclo = _G.resolve_caminhos_todos_pares()
    print("Há ciclo de peso total negativo no digrafo") if ciclo is None else print(
        "Não há ciclo de peso total negativo no digrafo")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Constrói Caminho (26.10) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.resolve_caminhos_todos_pares()
    s, v = G.V[5], G.V[1]
    print("{}-{} caminho: {}".format(s.valor, v.valor,
                                     [v.valor for v in G.constroi_caminho(s, v)]))
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>> Johnson (26.11) <<<<<<<<<<<<<<<<<<<<<<<<<")
    V = [x for x in range(6)]
    E = [[1, 2, 6], [2, 3, 4], [2, 4, -2], [3, 1, 2],
         [3, 4, -6], [3, 5, 2], [4, 2, 8], [5, 4, -4]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.johnson()
    if not G.ciclo_negativo:
        for v in G.V[1:]:
            print("Custos para o vértice {}".format(v.valor))
            for _m, j in enumerate(v.distancias[1:]):
                print("Menor custo para sair de {} para {}: {}".format(
                    v.valor, _m+1, j))
