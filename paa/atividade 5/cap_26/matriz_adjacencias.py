from math import inf
from copy import deepcopy


from vertice import Vertice
from heap import insere_heap, remove_heap, altera_heap, consulta_heap


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

    def nao_vizinhanca(self, u):
        return [self.V[n] for n, l in enumerate(self.matriz[u.valor])
                if l == 0 and n != u.valor][1:]

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


class MatrizAdjacenciasDigrafo(MatrizAdjacencias):
    def __init__(self, V, E):
        self.V = [Vertice(v) for v in V[:]]
        self.E = E[:]
        self.matriz = [[0 for x in range(len(V))] for y in range(len(V))]
        for e in E:
            self.matriz[e[0]][e[1]] = 1
        self.pre_ordem, self.pos_ordem, self.pos_ordem_reversa = [], [], []
        self.ciclo_negativo = False
        self.W = None  # tabela custo dos caminhos
        # funcao de distancias entre vertices
        self.w = [[0 for x in range(len(self.V))] for y in range(len(self.V))]
        for e in self.E:
            self.w[e[0]][e[1]] = e[2]
        # iniciando lista de predecessores
        for v in self.V:
            v.predecessores = [None for i in self.V]
            v.distancias = [None for i in self.V]

    def _arco(self, s, v):
        self.matriz[s.valor][v.valor] = 0
        self.chama_busca(v, tipo_busca='profundidade')
        if self.V[s.valor].visitado:
            self.matriz[s.valor][v.valor] = 1
            return True
        else:
            self.matriz[s.valor][v.valor] = 1
            return False

    def fleury(self, s):
        '''algoritmo 25.1'''
        W = [None for v in range(len(self.E)+2)]
        W[1] = s
        i = 1
        vizinhos = self.vizinhanca(W[i])
        while(len(vizinhos) >= 1):
            print("Acessando o vértice {}".format(W[i].valor))
            print("Vizinhos: {}".format(
                [vizinho.valor for vizinho in vizinhos]))
            seguro = False
            for y in vizinhos:
                if (self._arco(W[i], y)):  # seguro
                    seguro = True
                    break
            if seguro:
                print("Há arco seguro entre {} e {}".format(
                    W[i].valor, y.valor))
                W[i+1] = y
            else:
                print(
                    "Não há arco seguro saindo do vértice {}".format(W[i].valor))
                W[i+1] = vizinhos[0]
            # remove aresta em D
            self.matriz[W[i].valor][W[i+1].valor] = 0
            i += 1
            vizinhos = self.vizinhanca(W[i])
        [print(w.valor, end=" ") for w in W[1:]]
        print()
        return W

    def dijkstra(self, s):
        '''algoritmo 26.1'''
        for v in self.V:
            v.predecessor = None
            v.distancia = inf
            v.visitado = 0
        s.distancia = 0
        _iter = 1
        while(len([1 for u in self.V if u.visitado == 0 and u.distancia != inf]) > 0):
            print("Iteração {}".format(_iter))
            _vertices = sorted(self.V, key=lambda e: e.distancia)
            x = [v for v in _vertices if v.visitado == 0][0]
            x.visitado = 1
            print("\tVisitando o vértice {}".format(x.valor))
            # print("Vizinhos: {}".format(
            #     [_x.valor for _x in self.vizinhanca(x)]))
            relaxamento = False
            for y in self.vizinhanca(x):
                if y.visitado == 0:
                    if x.distancia+self.w[x.valor][y.valor] < y.distancia:
                        relaxamento = True
                        print("\tRelaxando arco {}-{}. Distância do vértice {} alterada de {} para {}".format(
                            x.valor, y.valor, y.valor, y.distancia, x.distancia+self.w[x.valor][y.valor]))
                        y.distancia = x.distancia+self.w[x.valor][y.valor]
                        y.predecessor = x
            if not relaxamento:
                print("\tSem arcos para relaxar")
            _iter += 1

    def dijkstra_heap(self, s):
        '''algoritmo 26.2'''
        H = []
        for v in self.V:
            v.predecessor = None
            v.prioridade = -inf
            v.visitado = 0
            insere_heap(H, v)
        altera_heap(H, s.indice, 0)
        print("Iniciando Heap. Apenas o Vértice {} com prioridade {}".format(
            s.valor, s.prioridade))
        _iter = 1
        while(len(H) > 0 and consulta_heap(h=H).prioridade != -inf):
            print("Iteração {}".format(_iter))
            x, H = remove_heap(H)
            print("\tRemove da heap o vértice {}".format(x.valor))
            x.visitado = 1
            # print("Visitando o vértice {}".format(x.valor))
            # print("Vizinhos: {}".format(
            #    [_x.valor for _x in self.vizinhanca(x)]))
            relaxamento = False
            for y in self.vizinhanca(x):
                if y.visitado == 0:
                    if x.prioridade-self.w[x.valor][y.valor] > y.prioridade:
                        relaxamento = True
                        print("\tRelaxando arco {}-{}. Distância do vértice {} alterada de {} para {}".format(
                            x.valor, y.valor, y.valor, y.prioridade, x.prioridade-self.w[x.valor][y.valor]))
                        altera_heap(H, y.indice,
                                    x.prioridade-self.w[x.valor][y.valor])
                        y.predecessor = x
            if not relaxamento:
                print("\tSem arcos para relaxar")
            _iter += 1

    def bellman_ford(self, s):
        '''algoritmo 26.3'''
        for v in self.V:
            v.distancia = inf
            v.predecessor = None
        s.distancia = 0
        for i in range(1, len(self.V[1:])):
            for e in self.E:
                x, y = self.V[e[0]], self.V[e[1]]
                if y.distancia > x.distancia+self.w[x.valor][y.valor]:
                    y.distancia = x.distancia+self.w[x.valor][y.valor]
                    y.predecessor = x
            print("Após iteração i = {}".format(i))
            for v in self.V[1:]:
                if v.predecessor is None:
                    predecessor = "null"
                else:
                    predecessor = v.predecessor.valor
                print("Vertice {}: distância {}, predecessor: {} ".format(
                    v.valor, v.distancia, predecessor))
        for e in self.E:
            x, y = self.V[e[0]], self.V[e[1]]
            if y.distancia > x.distancia+self.w[x.valor][y.valor]:
                self.ciclo_negativo = True
        if self.ciclo_negativo:
            print("Há ciclo negativo no digrafo")
        else:
            print("Não há ciclo negativo no digrafo")

    def caminho(self, i, j, X):
        '''algoritmo 26.4'''
        print('Chamada ({}, {}, {})'.format(i, j, X))
        if len(X) == 0:
            if self.matriz[i][j]:
                return self.w[i][j]
            elif i == j:
                return 0
            return inf
        k = X[0]
        print('Chamada não usa {} ({}, {}, {})'.format(k, i, j, X[1:]))
        nao_usa_k = self.caminho(i, j, X[1:])
        print('Chamada usa {} ({}, {}, {})'.format(k, i, j, X[1:]))
        usa_k = self.caminho(i, k, X[1:])+self.caminho(k, j, X[1:])
        return min(nao_usa_k, usa_k)

    def floyd_warshall_top_down(self):
        '''algoritmo 26.5'''
        self.W = [[[inf for k in self.V] for j in self.V] for i in self.V]
        for i in self.V[1:]:
            for j in self.V[1:]:
                self.W[i.valor][j.valor][len(self.V[1:])] = self.floyd_warshall_rec_top_down(
                    self.w, len(self.V[1:]), i, j)
        return self.W

    def floyd_warshall_rec_top_down(self, w, k, i, j):
        '''algoritmo 26.6'''
        if self.W[i.valor][j.valor][k] == inf:
            if k == 0:
                if i.valor == j.valor:
                    self.W[i.valor][j.valor][0] = 0
                    j.predecessores[i.valor] = i
                elif self.matriz[i.valor][j.valor]:
                    self.W[i.valor][j.valor][0] = w[i.valor][j.valor]
                    j.predecessores[i.valor] = j
                else:
                    self.W[i.valor][j.valor][0] = inf
                    j.predecessores[i.valor] = None
            else:
                nao_usa_k = self.floyd_warshall_rec_top_down(w, k-1, i, j)
                usa_k = self.floyd_warshall_rec_top_down(w, k-1, i, self.V[k]) +\
                    self.floyd_warshall_rec_top_down(w, k-1, self.V[k], j)
                if nao_usa_k < usa_k:
                    self.W[i.valor][j.valor][k] = nao_usa_k
                else:
                    self.W[i.valor][j.valor][k] = usa_k
                    j.predecessores[i.valor] = j.predecessores[k]
        return self.W[i.valor][j.valor][k]

    def floyd_warshall_bottom_up(self):
        '''algoritmo 26.7'''
        self.W = [[[inf for k in self.V] for j in self.V] for i in self.V]
        for i in self.V[1:]:
            for j in self.V[1:]:
                if (i.valor == j.valor):
                    self.W[i.valor][j.valor][0] = 0
                    j.predecessores[i.valor] = i
                elif self.matriz[i.valor][j.valor]:
                    self.W[i.valor][j.valor][0] = self.w[i.valor][j.valor]
                    j.predecessores[i.valor] = i
                else:
                    self.W[i.valor][j.valor][0] = inf
                    j.predecessores[i.valor] = None
        for k in self.V[1:]:
            for i in self.V[1:]:
                for j in self.V[1:]:
                    nao_usa_k = self.W[i.valor][j.valor][k.valor-1]
                    usa_k = self.W[i.valor][k.valor][k.valor-1] + \
                        self.W[k.valor][j.valor][k.valor-1]
                    if nao_usa_k < usa_k:
                        self.W[i.valor][j.valor][k.valor] = nao_usa_k
                    else:
                        self.W[i.valor][j.valor][k.valor] = usa_k
                        j.predecessores[i.valor] = j.predecessores[k.valor]
        return self.W

    def floyd_warshall_melhorado(self):
        '''algoritmo 26.8'''
        self.W = [[inf for j in self.V] for i in self.V]
        _iter = 0
        for i in self.V[1:]:
            for j in self.V[1:]:
                print("Iteração {}: par de vértice ({}, {})".format(
                    _iter, i.valor, j.valor))
                if (i.valor == j.valor):
                    print("\tMesmo vértice. Distância = 0")
                    self.W[i.valor][j.valor] = 0
                    j.predecessores[i.valor] = i
                elif self.matriz[i.valor][j.valor]:
                    print("\tExiste aresta entre os vértices. Distância = {}".format(
                        self.w[i.valor][j.valor]))
                    self.W[i.valor][j.valor] = self.w[i.valor][j.valor]
                    j.predecessores[i.valor] = i
                else:
                    print("\tNão existe aresta entre os vértices. Distância = inf")
                    self.W[i.valor][j.valor] = inf
                    j.predecessores[i.valor] = None
        for k in self.V[1:]:
            for i in self.V[1:]:
                for j in self.V[1:]:
                    if self.W[i.valor][j.valor] > self.W[i.valor][k.valor]+self.W[k.valor][j.valor]:
                        self.W[i.valor][j.valor] = self.W[i.valor][k.valor] + \
                            self.W[k.valor][j.valor]
                        j.predecessores[i.valor] = j.predecessores[k.valor]
        return self.W

    def resolve_caminhos_todos_pares(self):
        '''algoritmo 26.9'''
        self.floyd_warshall_bottom_up()
        # verificando ciclos negativos
        _iter = 1
        for i in self.V[1:]:
            print("Iteração {}".format(_iter))
            if self.W[i.valor][i.valor][-1] < 0:
                return None
            print("Custo para {}-{}: {}".format(
                i.valor, i.valor, self.W[i.valor][i.valor][-1]))
            _iter += 1
        return self.W

    def constroi_caminho(self, i, j):
        '''algoritmo 26.10'''
        L = []
        atual = j
        while(atual.valor != i.valor):
            L = [atual]+L
            atual = atual.predecessores[i.valor]
        L = [i]+L
        return L

    def johnson(self):
        ''''algoritmo 26.11'''
        s = Vertice(len(self.V))
        _e = [[s.valor, v.valor, 0] for v in self.V[1:]]
        _D = MatrizAdjacenciasDigrafo(
            [v.valor for v in self.V+[s]], self.E + _e)
        _D.bellman_ford(_D.V[s.valor])
        if _D.ciclo_negativo:
            return "O digrafo D contém ciclo de peso negativo"
        D_ = deepcopy(self)
        for e in D_.E:
            u, v = e[0], e[1]
            D_.w[u][v] = _D.V[u].distancia + _D.w[u][v] - _D.V[v].distancia
        for u in self.V[1:]:
            D_.dijkstra(D_.V[u.valor])
            for v in self.V[1:]:
                u.distancias[v.valor] = D_.V[v.valor].distancia + \
                    (_D.V[v.valor].distancia-_D.V[u.valor].distancia)
