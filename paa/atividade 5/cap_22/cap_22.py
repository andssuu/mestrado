class MatrizAdjacencias():
    def __init__(self, V, E):
        self.matriz = [[0 for x in range(len(V)+1)] for y in range(len(V)+1)]
        for e in E:
            self.matriz[e[0]][e[1]], self.matriz[e[1]][e[0]] = 1, 1

    def grau_maximo(self):
        ''' Algoritmo 22.2 '''
        max = 0
        for x in range(1, len(self.matriz)):
            grau_x = 0
            for y in range(1, len(self.matriz)):
                if self.matriz[x][y] == 1:
                    grau_x += 1
            if grau_x > max:
                max = grau_x
        return max


class ListaAdjacencias():
    def __init__(self, V, E):
        self.lista = [[] for x in range(len(V)+1)]
        for e in E:
            self.lista[e[0]].append(e[1])
            self.lista[e[1]].append(e[0])

    def grau_maximo(self):
        '''Algoritmo 22.3'''
        n = len(self.lista)
        max = 0
        for x in range(1, n):
            grau_x = 0
            for atual in self.lista[x]:
                grau_x += 1
            if grau_x > max:
                max = grau_x
        return max


if __name__ == "__main__":
    V = [1, 2, 3, 4, 5, 6, 7]
    E = [[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [6, 7]]
    print('''
    #############################################
    
        Implementações com Matriz de Adjacências
    
    #############################################
    ''')
    # Matriz adjacencias
    matriz_adjacencias = MatrizAdjacencias(V, E)
    print("Matriz de adjacencias: ")
    [print(x[1:]) for x in matriz_adjacencias.matriz[1:]]
    print("Grau Máximo: ", matriz_adjacencias.grau_maximo())
    print('''
    #############################################
    
        Implementações com Lista de Adjacências
    
    #############################################
    ''')
    # Lista de adjacencias
    lista_adjacencias = ListaAdjacencias(V, E)
    print("Lista de adjacencias: ")
    [print('Vertice {}: {}'.format(n+1, x))
     for n, x in enumerate(lista_adjacencias.lista[1:])]
    print("Grau Máximo: ", lista_adjacencias.grau_maximo())
