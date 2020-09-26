from vertice import Vertice


class ListaAdjacencias():
    def __init__(self, V, E):
        self.V = [Vertice(v) for v in V]
        self.E = E
        self.lista = [[] for x in range(len(V))]
        for e in E:
            self.lista[e[0]].append(e[1])
            self.lista[e[1]].append(e[0])

    def vizinhanca(self, u):
        return [self.V[v] for v in self.lista[u.valor]]

    def constroi_caminho(self, s, v):
        '''algoritmo 23.4'''
        L = []
        if v.visitado == 0:
            return L
        atual = v
        while(atual.valor != s.valor):
            L.append(atual)
            atual = atual.predecessor
        L.append(s)
        return L

    def busca_largura(self, s):
        ''' algoritmo 23.5'''
        s.visitado = 1
        fila = []
        fila.append(s)
        while(len(fila) > 0):
            u = fila[0]  # desenfileirar
            fila = fila[1:]
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.predecessor = u
                    fila.append(v)

    def busca_largura_distancia(self, s):
        ''' algoritmo 23.6'''
        s.visitado = 1
        fila = []
        fila.append(s)
        while(len(fila) > 0):
            u = fila[0]  # desenfileirar
            fila = fila[1:]
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.distancia = u.distancia + 1
                    v.predecessor = u
                    fila.append(v)

    def busca_prof_iterativa(self, s):
        '''algoritmo 23.7'''
        s.visitado = 1
        pilha = []
        pilha.append(s)
        while (len(pilha) > 0):
            u = pilha[-1]  # consulta
            visitados = True
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.predecessor = u
                    pilha.append(v)
                    visitados = False
                    break
            # desempilha quando todos vizinhos forem visitados
            if visitados:
                pilha = pilha[:-1]

    def busca_prof_recursiva(self, s):
        '''algoritmo 23.8'''
        s.visitado = 1
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                v.predecessor = s
                self.busca_prof_recursiva(v)
