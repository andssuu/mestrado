from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo


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
    G = MatrizAdjacencias(V, E)
    print("Matriz de adjacencias: ")
    [print(x[1:]) for x in G.matriz[1:]]
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Kruskal (24.1) <<<<<<<<<<<<<<<<<<<<<<<<<")
    F = G.kruskal()
    print("Lista de arestas da árvore geradora mínima")
    [print("Aresta {}-{} com peso {}".format(x[0], x[1], x[2])) for x in F]
    arvore_minima = MatrizAdjacencias(V, F)
    print("Matriz de adjacencias (Árvore Geradora Mínima):")
    [print(x[1:]) for x in arvore_minima.matriz[1:]]
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Kruskal Union Find (24.2) <<<<<<<<<<<<<<<<<<<<<<<<<")
    F = G.kruskal_union_find()
    print("Lista de arestas da árvore geradora mínima")
    [print("Aresta {}-{} com peso {}".format(x[0], x[1], x[2])) for x in F]
    arvore_minima = MatrizAdjacencias(V, F)
    print("Matriz de adjacencias (Árvore Geradora Mínima):")
    [print(x[1:]) for x in arvore_minima.matriz[1:]]
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Prim (24.3) <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.prim()
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Prim Heap (24.4) <<<<<<<<<<<<<<<<<<<<<<<<<")
    G.prim_heap()
