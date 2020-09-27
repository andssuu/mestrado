from vertice import Vertice


class MatrizAdjacencias():
    def __init__(self, V, E):
        self.V = [Vertice(v) for v in V]
        self.E = E
        self.matriz = [[0 for x in range(len(V))] for y in range(len(V))]
        for e in self.E:
            self.matriz[e[0]][e[1]], self.matriz[e[1]][e[0]] = 1, 1
        self.pre_ordem, self.pos_ordem, self.pos_ordem_reversa = [], [], []

    def vizinhanca(self, u):
        return [self.V[n] for n, l in enumerate(self.matriz[u.valor]) if l]

    def chama_busca(self, s=None, tipo_busca=''):
        '''algoritmo 23.2'''
        for v in self.V:
            v.visitado = 0
            v.predecessor = None
        if tipo_busca == 'largura':
            self.busca_largura(s)
        elif tipo_busca == 'largura_distancia':
            self.busca_largura_distancia(s)
        elif(tipo_busca == 'profundidade'):
            self.busca_profundidade(s)
        elif(tipo_busca == 'profundidade_iterativa'):
            self.busca_prof_iterativa(s)
        elif(tipo_busca == 'profundidade_recursiva'):
            self.busca_prof_recursiva(s)
        elif(tipo_busca == 'componentes'):
            return self.busca_componentes()
        else:
            print('Tipo de busca inválido')

    def constroi_caminho(self, s, v):
        '''algoritmo 23.4'''
        L = []
        if v.visitado == 0:
            return L
        atual = v
        while(atual.valor != s.valor):
            L = [atual] + L
            atual = atual.predecessor
        L = [s]+L
        return L

    def busca_largura(self, s):
        '''algoritmo 23.5 e 23.11'''
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
        '''algoritmo 23.6'''
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

    def busca_profundidade(self, s):
        '''algoritmo 23.9 e 23.12'''
        self.pre_ordem.append(s)
        s.visitado = 1
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                v.predecessor = s
                v.componente = s.componente
                self.busca_profundidade(v)
        self.pos_ordem.append(s)
        self.pos_ordem_reversa = [s] + self.pos_ordem_reversa

    def busca_componentes(self):
        '''algoritmo 23.10'''
        for v in self.V[1:]:
            v.visitado = 0
            v.predecessor = None
        qtd_componentes = 0
        for s in self.V[1:]:
            if s.visitado == 0:
                s.visitado = 1
                s.componente = s.valor
                qtd_componentes += 1
                self.busca_profundidade(s)
        return qtd_componentes


class MatrizAdjacenciasDigrafo(MatrizAdjacencias):
    def __init__(self, V, E):
        self.V = [Vertice(v) for v in V[:]]
        self.E = E[:]
        self.matriz = [[0 for x in range(len(V))] for y in range(len(V))]
        for e in E:
            self.matriz[e[0]][e[1]] = 1
        self.pre_ordem, self.pos_ordem, self.pos_ordem_reversa = [], [], []

    @staticmethod
    def reverso(G):
        from copy import deepcopy
        E = deepcopy(G.E)
        for e in E:
            e[0], e[1] = e[1], e[0]
        return MatrizAdjacenciasDigrafo([v.valor for v in G.V], E)

    def componentes_fortemente_conexas(self):
        '''algoritmo 23.13'''
        for v in self.V[1:]:
            v.visitado = 0
            v.predecessor = None
        inverso = self.reverso(self)
        inverso.busca_componentes()
        for v in inverso.V[1:]:
            v.visitado = 0
        for u in inverso.pos_ordem_reversa:
            if self.V[u.valor].visitado == 0:
                self.V[u.valor].componente = u.valor
                self.busca_profundidade(self.V[u.valor])

    def ordenacao_topologica(self):
        '''algoritmo 23.14'''
        self.busca_componentes()
        f = []
        for atual in self.pos_ordem_reversa:
            f.append(atual)
        return f
