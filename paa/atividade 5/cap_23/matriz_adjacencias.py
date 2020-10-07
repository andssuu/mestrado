from copy import deepcopy

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
        print("Começando com o vértice {}".format(s.valor))
        print("Estado da fila: {}".format([f.valor for f in fila]))
        _iter = 1
        while(len(fila) > 0):
            print("Iteração: {}".format(_iter))
            print("\tEstado da fila: {}".format([f.valor for f in fila]))
            u = fila[0]  # desenfileirar
            print("\tRemovendo o {} da fila".format(u.valor))
            fila = fila[1:]
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.predecessor = u
                    print("\tAdicionando vizinho {} na fila".format(v.valor))
                    fila.append(v)
            _iter += 1

    def busca_largura_distancia(self, s):
        '''algoritmo 23.6'''
        s.visitado = 1
        fila = []
        fila.append(s)
        _iter = 1
        print("Começando com o vértice {}".format(s.valor))
        print("Estado da fila: {}".format([f.valor for f in fila]))
        while(len(fila) > 0):
            print("Iteração: {}".format(_iter))
            print("\tEstado da fila: {}".format([f.valor for f in fila]))
            u = fila[0]  # desenfileirar
            print("\tRemovendo o {} da fila".format(u.valor))
            fila = fila[1:]
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.distancia = u.distancia + 1
                    v.predecessor = u
                    print("\tAdicionando vizinho {} na fila com distância {}".format(
                        v.valor, v.distancia))
                    fila.append(v)

    def busca_prof_iterativa(self, s):
        '''algoritmo 23.7'''
        s.visitado = 1
        pilha = []
        pilha.append(s)
        _iter = 1
        print("Começando com o vértice {}".format(s.valor))
        print("Estado da pilha: {}".format([f.valor for f in pilha]))
        while (len(pilha) > 0):
            print("Iteração: {}".format(_iter))
            print("\tEstado da pilha: {}".format([f.valor for f in pilha]))
            u = pilha[-1]  # consulta
            visitados = True
            for v in self.vizinhanca(u):
                if v.visitado == 0:
                    v.visitado = 1
                    v.predecessor = u
                    pilha.append(v)
                    print("\tAdicionando vizinho {} na pilha com o predecessor {}".format(
                        v.valor, u.valor))
                    visitados = False
                    break
            # desempilha quando todos vizinhos forem visitados
            if visitados:
                print("\tDesempilhando {} da pilha".format(pilha[-1].valor))
                pilha = pilha[:-1]
            _iter += 1

    def busca_prof_recursiva(self, s):
        '''algoritmo 23.8'''
        s.visitado = 1
        print("Visitando o vértice {}".format(s.valor))
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                v.predecessor = s
                print("\tChamada para o vizinho {} na pilha com o predecessor {}".format(
                    v.valor, s.valor))
                self.busca_prof_recursiva(v)

    def busca_profundidade(self, s):
        '''algoritmo 23.9 e 23.12'''
        self.pre_ordem.append(s)
        s.visitado = 1
        print("Adicionando o vértice {} na lista de pré-ordem".format(s.valor))
        print("Estado atual da lista de pré-ordem: {}".format(
            [v.valor for v in self.pre_ordem]))
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                v.predecessor = s
                v.componente = s.componente
                print("Chamada para o vizinho {} com o predecessor {}".format(
                    v.valor, s.valor))
                self.busca_profundidade(v)
        self.pos_ordem.append(s)
        self.pos_ordem_reversa = [s] + self.pos_ordem_reversa
        print("Estado atual da lista de pós-ordem: {}".format(
            [v.valor for v in self.pos_ordem]))
        print("Estado atual da lista de pós-ordem reversa: {}".format(
            [v.valor for v in self.pos_ordem_reversa]))

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
        print("Iniciando com a busca de componentes")
        inverso.busca_componentes()
        print("Fim da busca de componentes")
        for v in inverso.V[1:]:
            v.visitado = 0
        print("Estado da pós-ordem reversa: {}".format(
            [i.valor for i in inverso.pos_ordem_reversa]))
        _iter = 1
        for u in inverso.pos_ordem_reversa:
            print("Iteração: {}".format(_iter))
            if self.V[u.valor].visitado == 0:
                print("\tAcessando o vértice {}".format(u.valor))
                print("\tAdicionando o vértice {} na componente {}".format(
                    u.valor, u.valor))
                self.V[u.valor].componente = u.valor
                print("\tChamando busca em profundidade para o vértice {}".format(
                    u.valor))
                self.busca_profundidade(self.V[u.valor])
            else:
                print("\tVértice {} já visitado. Está na componente {}".format(
                    u.valor, u.componente))
            _iter += 1

    def ordenacao_topologica(self):
        '''algoritmo 23.14'''
        print("Fazendo a chamada para para busca de componentes")
        self.busca_componentes()
        print("Fim da busca de componentes")
        f = []
        print("Estado da lista de pós-ordem reversa: {}".format(
            [v.valor for v in self.pos_ordem_reversa]))
        _iter = 1
        for atual in self.pos_ordem_reversa:
            print("Iteração {}: Adicionando o vértice {} na lista".format(
                _iter, atual.valor))
            f.append(atual)
            _iter += 1
        return f
