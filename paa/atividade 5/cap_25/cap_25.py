from matriz_adjacencias import MatrizAdjacencias, MatrizAdjacenciasDigrafo
# from lista_adjacencias import ListaAdjacencias, ListaAdjacenciasDigrafo

if __name__ == "__main__":
    print('''
    #############################################

        Implementações com Matriz de Adjacências

    #############################################
    ''')
    V = [x for x in range(9)]
    E = [[1, 2], [1, 4], [2, 5], [3, 1], [3, 5], [4, 5], [5, 1],
         [5, 3], [5, 6], [6, 3], [6, 7], [7, 6], [7, 8], [8, 7]]
    G = MatrizAdjacenciasDigrafo(V, E)
    G.fleury(G.V[3])