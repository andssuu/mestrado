from math import inf
from copy import deepcopy


from vertice import Vertice
# from union_find import UnionFind
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
        elif(tipo_busca == 'profundidade_iterativa'):
            self.busca_prof_iterativa(s)
        elif(tipo_busca == 'profundidade_recursiva'):
            self.busca_prof_recursiva(s)
        elif(tipo_busca == 'profundidade'):
            self.busca_profundidade(s)
        elif(tipo_busca == 'componentes'):
            return self.busca_componentes()
        else:
            print('Tipo de busca inválido')

    def constroi_caminho(self, s, v):
        '''algoritmo 23.4'''
        print("Contrução do {}-{} caminho".format(s.valor, v.valor))
        L = []
        print("Estado Inicial da lista: {}".format(L))
        if v.visitado == 0:
            return L
        atual = v
        _iter = 1
        while(atual.valor != s.valor):
            print("Iteração {}: ".format(_iter))
            L = [atual] + L
            print("\tAdicionando o vértice {} com predecessor {} na lista".format(
                atual.valor, atual.predecessor.valor))
            print("\tEstado atual da lista: {}".format([l.valor for l in L]))
            atual = atual.predecessor
            _iter += 1
        print("Iteração: {}".format(_iter))
        print("\tAdicionando {} no início da lista".format(s.valor))
        L = [s]+L
        print("\tEstado final da lista: {}".format([l.valor for l in L]))
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
        print("Iteração: {}".format(_iter))
        print("\tFila vazia!")

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
            _iter += 1
        print("Iteração: {}".format(_iter))
        print("\tFila vazia!")

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
        print("Iteração: {}".format(_iter))
        print("\tPilha vazia!")

    def busca_prof_recursiva(self, s):
        '''algoritmo 23.8'''
        s.visitado = 1
        check = False
        print("Visitando o vértice {}".format(s.valor))
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                check = True
                v.predecessor = s
                print("\tChamada para o vizinho {} com o predecessor {}".format(
                    v.valor, s.valor))
                self.busca_prof_recursiva(v)
        if not check:
            print("\tTodos os vizinhos do vértice {} foram visitados".format(s.valor))

    def busca_profundidade(self, s):
        '''algoritmo 23.9 e 23.12'''
        self.pre_ordem.append(s)
        s.visitado = 1
        # print("Adicionando o vértice {} na lista de pré-ordem".format(s.valor))
        # print("Estado atual da lista de pré-ordem: {}".format(
        #    [v.valor for v in self.pre_ordem]))
        for v in self.vizinhanca(s):
            if v.visitado == 0:
                v.predecessor = s
                v.componente = s.componente
        #        print("Chamada para o vizinho {} com o predecessor {}".format(
        #            v.valor, s.valor))
                self.busca_profundidade(v)
        self.pos_ordem.append(s)
        self.pos_ordem_reversa = [s] + self.pos_ordem_reversa
        # print("Estado atual da lista de pós-ordem: {}".format(
        #    [v.valor for v in self.pos_ordem]))
        # print("Estado atual da lista de pós-ordem reversa: {}".format(
        #    [v.valor for v in self.pos_ordem_reversa]))

    def busca_componentes(self):
        '''algoritmo 23.10'''
        for v in self.V[1:]:
            v.visitado = 0
            v.predecessor = None
        qtd_componentes = 0
        for s in self.V[1:]:
            if s.visitado == 0:
                print("Visitando vértice {}: chama busca em profundidade".format(
                    s.valor))
                s.visitado = 1
                s.componente = s.valor
                qtd_componentes += 1
                self.busca_profundidade(s)
                print("Fim da busca em profundidade no vértice {}".format(s.valor))
            else:
                print("Visitando vértice {}: vértice já visitado!".format(s.valor))
        return qtd_componentes

    def _verifica_ciclo(self, s, matriz_aux):
        s.visitado = 1
        for v in self.vizinhanca(s):
            if matriz_aux[s.valor][v.valor]:
                continue
            matriz_aux[s.valor][v.valor], matriz_aux[v.valor][s.valor] = 1, 1
            if v.visitado:
                matriz_aux[0][0] = 1
            self._verifica_ciclo(v, matriz_aux)

    def kruskal(self):
        '''algoritmo 24.1'''
        C = sorted(deepcopy(self.E), key=lambda e: e[2])
        F = []  # conjunto de arestas
        _iter = 1
        for c in C:
            print("Iteração {}:".format(_iter))
            _G = MatrizAdjacencias(
                [v.valor for v in deepcopy(self.V)], E=F+[c])
            matriz_aux = [[0 for x in range(len(self.V))]
                          for y in range(len(self.V))]
            _G._verifica_ciclo(_G.V[c[0]], matriz_aux)
            if not matriz_aux[0][0]:
                F = F+[c]
                print("\tNão há ciclo. Adicionando a aresta {} em F".format(c))
                print("\tEstado atual de F: {}".format([f for f in F]))
            else:
                print("\tHá ciclo se adicionar a aresta {} em F".format(c))
            _iter += 1
        return F

    def kruskal_union_find(self):
        '''algoritmo 24.2'''
        C = sorted(deepcopy(self.E), key=lambda e: e[2])
        F = []  # conjunto de arestas
        sets = [UnionFind(v.valor) for v in self.V]
        _iter = 1
        for c in C:
            print("Iteração {}".format(_iter))
            u, v = sets[c[0]], sets[c[1]]
            print("\tTestando aresta {}-{}".format(c[0], c[1]))
            if u.find_set() != v.find_set():
                F = F+[c]
                UnionFind.union(u, v)
                print("\tAresta {}-{} adicionada".format(c[0], c[1]))
                print("\tEstado da Union-Find:")
                [print("\t\tVértice: {} Representante: {} Tamanho: {} Lista: {}".format(s.valor, s.representante.valor, len(s.lista), [e.valor for e in s.lista]))
                 for s in sets[1:]]
            else:
                print("\tArestas com o mesmo representante {}".format(
                    u.representante.valor))
            _iter += 1
        return F

    def prim(self):
        '''algoritmo 24.3'''
        for v in self.V:
            v.visitado = 0
            v.predecessor = None
        x = self.V[6]  # escolha de qualquer vértice
        print("Iniciando pelo vértice {}".format(x.valor))
        x.visitado = 1
        visitados = []
        _n = 1
        while (len([0 for v in self.V[1:] if not v.visitado])):
            print("Iteração: ", _n)
            for e in sorted(deepcopy(self.E), key=lambda e: e[2]):
                if (self.V[e[0]].visitado == 1) and (self.V[e[1]].visitado == 0):
                    print("\tAresta mímina {}-{} adicionada com peso {}".format(e[0], e[1],
                                                                                e[2]))
                    self.V[e[1]].visitado = 1
                    self.V[e[1]].predecessor = self.V[e[0]]
                    visitados.append(
                        [self.V[e[0]].valor, self.V[e[1]].valor])
                    print("\tVértices visitados: {}".format(
                        [_v.valor for _v in self.V[1:] if _v.visitado]))
                    break
                elif self.V[e[0]].visitado == 0 and self.V[e[1]].visitado == 1:
                    print("\tAresta mímina {}-{} adicionada com peso {}".format(e[0], e[1],
                                                                                e[2]))
                    self.V[e[0]].visitado = 1
                    self.V[e[0]].predecessor = self.V[e[1]]
                    visitados.append(
                        [self.V[e[1]].valor, self.V[e[0]].valor])
                    print("\tVértices visitados: {}".format(
                        [_v.valor for _v in self.V[1:] if _v.visitado]))
                    break
            _n += 1
        print("Não há mais vértice não visitado")
        print("Lista de arestas utilizadas: ")
        [print(x) for x in visitados]

    def prim_heap(self):
        '''algoritmo 24.4'''
        w = [[0 for x in range(len(self.E))] for y in range(len(self.E))]
        for e in self.E:
            w[e[0]][e[1]], w[e[1]][e[0]] = e[2], e[2]
        s = self.V[6]  # escolha de qualquer vértice
        s.visitado = 1
        s.predecessor = None
        # H = [None for e in range(len(self.E))]
        H = []
        print("Vertice {} escolhido inicialmente".format(s.valor))
        print("Atualizando prioridade, visitado e predecessor dos vizinhos de {}"
              .format(s.valor))
        for v in self.vizinhanca(s):
            print("\tAcessando o vértice {}".format(v.valor))
            v.prioridade = -w[s.valor][v.valor]
            v.visitado = 0
            v.predecessor = s
            insere_heap(H, v)
            print("\tEstado atual da Heap: ", [h.valor for h in H])
            print("\tpredecessor: ", end="")
            [print(h.predecessor.valor, end=" ") if h.predecessor is not None else print(None, end=" ")
             for h in H]
            print("\n\tvisitado: ", end="")
            [print(h.visitado, end=" ") for h in H]
            print("\n\tindice: ", end="")
            [print(h.indice, end=" ") for h in H]
            print("\n\tprioridade: ", end="")
            [print(h.prioridade, end=" ") for h in H]
            print()
        print("\nAtualizando prioridade, visitado e predecessores dos não vizinhos de {}".
              format(s.valor))
        for v in self.nao_vizinhanca(s):
            print("\tAcessando o vértice {}".format(v.valor))
            v.prioridade = -inf
            v.visitado = 0
            v.predecessor = None
            insere_heap(H, v)
            print("\tEstado atual da Heap: ", [h.valor for h in H])
            print("\tpredecessor: ", end="")
            [print(h.predecessor.valor, end=" ") if h.predecessor is not None else print(None, end=" ")
             for h in H]
            print("\n\tvisitado: ", end="")
            [print(h.visitado, end=" ") for h in H]
            print("\n\tindice: ", end="")
            [print(h.indice, end=" ") for h in H]
            print("\n\tprioridade: ", end="")
            [print(h.prioridade, end=" ") for h in H]
            print()
        while len(H) > 0:
            print("\nRevomendo o vértice {} da heap".format(H[0].valor))
            v, H = remove_heap(H)
            v.visitado = 1
            for x in self.vizinhanca(v):
                if x.visitado == 0 and x.prioridade < -w[v.valor][x.valor]:
                    x.predecessor = v
                    altera_heap(H, x.indice, -w[v.valor][x.valor])
            print("Prioridades atualizadas da Heap: ", [h.valor for h in H])
        print("\nÁrvore geradora com os predecessores")
        for v in self.V[1:]:
            predecessor = "None" if v.predecessor is None else v.predecessor.valor
            print("Vertice: {}, prioridade: {}, predecessor: {}".format(
                v.valor, v.prioridade, predecessor))


class MatrizAdjacenciasDigrafo(MatrizAdjacencias):
    def __init__(self, V, E):
        self.V = [Vertice(v) for v in V[:]]
        self.E = E[:]
        self.matriz = [[0 for x in range(len(V))] for y in range(len(V))]
        for e in E:
            self.matriz[e[0]][e[1]] = 1
        self.pre_ordem, self.pos_ordem, self.pos_ordem_reversa = [], [], []
        self.ciclo_negativo = False
        # tabela custo dos caminhos
        self.W = None
        # funcao de distancias entre vertices
        self.w = [[0 for x in range(len(self.V))] for y in range(len(self.V))]
        for e in self.E:
            self.w[e[0]][e[1]] = e[2]
        # iniciando lista de predecessores
        for v in self.V:
            v.predecessores = [None for i in self.V]
            v.distancias = [None for i in self.V]

    @ staticmethod
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
            print("\nIteração: {}".format(_iter))
            if self.V[u.valor].visitado == 0:
                print("Acessando o vértice {}".format(u.valor))
                print("Adicionando o vértice {} na componente {}".format(
                    u.valor, u.valor))
                self.V[u.valor].componente = u.valor
                print("Chamando busca em profundidade para o vértice {}".format(
                    u.valor))
                self.busca_profundidade(self.V[u.valor])
            else:
                print("Vértice {} já visitado. Está na componente {}".format(
                    u.valor, u.componente))
            _iter += 1

    def ordenacao_topologica(self):
        '''algoritmo 23.14'''
#        print("Fazendo a chamada para para busca de componentes")
        self.busca_componentes()
#        print("Fim da busca de componentes")
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

    def _arco(self, s, v):
        self.matriz[s.valor][v.valor] = 0
        # print("Chamada busca em profundidade")
        self.chama_busca(v, tipo_busca='profundidade')
        # print("Fim da busca em profundidade")
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
            print("Iteração {} :".format(i))
            print("\tAcessando o vértice {}".format(W[i].valor))
            print("\tVizinhos: {}".format(
                [vizinho.valor for vizinho in vizinhos]))
            seguro = False
            for y in vizinhos:
                if (self._arco(W[i], y)):  # seguro
                    seguro = True
                    break
            if seguro:
                print("\tHá arco seguro entre {} e {}".format(
                    W[i].valor, y.valor))
                W[i+1] = y
            else:
                print(
                    "\tNão há arco seguro saindo do vértice {}".format(W[i].valor))
                W[i+1] = vizinhos[0]
            # remove aresta em D
            self.matriz[W[i].valor][W[i+1].valor] = 0
            i += 1
            vizinhos = self.vizinhanca(W[i])
            print("\tEstado atual da trilha: {}".format(
                [w.valor for w in W if w is not None]))
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
            print("\tEstado de antecedores dos vértices: {}".format(
                ["{}:{}".format(_n+1, v.predecessor.valor) if v.predecessor is not None else "{}:{}".format(_n+1, 'Null') for _n, v in enumerate(self.V[1:])]))
            _iter += 1

    def dijkstra_heap(self, s):
        '''algoritmo 26.2'''
        H = []
        for v in self.V[1:]:
            v.predecessor = None
            v.prioridade = -inf
            v.visitado = 0
            insere_heap(H, v)
        altera_heap(H, s.indice, 0)
        print("Iniciando Heap. Apenas o Vértice {} com prioridade {}".format(
            s.valor, s.prioridade))
        print("\tEstado atual da Heap: ", [h.valor for h in H])
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
            print("\tEstado atual da Heap: ", [h.valor for h in H])
            print("\tpredecessor: ", end="")
            [print(_v.predecessor.valor, end=" ") if _v.predecessor is not None else print("Null", end=" ")
             for _v in self.V[1:]]
            print("\n\tvisitado: ", end="")
            [print(_v.visitado, end=" ") for _v in self.V[1:]]
            print("\n\tindice: ", end="")
            [print(_v.indice, end=" ")
             if _v.valor in [_h.valor for _h in H] else print(" ", end=" ") for _v in self.V[1:]]
            print("\n\tprioridade: ", end="")
            [print(_v.prioridade, end=" ") for _v in self.V[1:]]
            print()
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
        _iter = 1
        for i in self.V[1:]:
            for j in self.V[1:]:
                # print(
                #    "Iteração {}: Chamada floyd_warshall_rec_top_down(k:{}, i:{}, j:{})".format(_iter, len(self.V[1:]), i.valor, j.valor))
                self.W[i.valor][j.valor][len(self.V[1:])] = self.floyd_warshall_rec_top_down(
                    self.w, len(self.V[1:]), i, j)
                _iter += 1
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
                # print("Chamada para floyd_warshall_rec_top_down(k:{}, i:{}, j:{}) não usando k".format(
                #    k-1, i.valor, j.valor))
                nao_usa_k = self.floyd_warshall_rec_top_down(w, k-1, i, j)
                # print("Chamada para floyd_warshall_rec_top_down(k:{}, i:{}, j:{}) usando k".format(
                #    k-1, i.valor, j.valor))
                usa_k = self.floyd_warshall_rec_top_down(w, k-1, i, self.V[k]) +\
                    self.floyd_warshall_rec_top_down(w, k-1, self.V[k], j)
                if nao_usa_k < usa_k:
                    #    print("Não vale a pena com o k={}".format(k-1))
                    self.W[i.valor][j.valor][k] = nao_usa_k
                else:
                    #    print("Vale a pena com o k={}".format(k))
                    self.W[i.valor][j.valor][k] = usa_k
                    j.predecessores[i.valor] = j.predecessores[k]
        # else:
            # print("Custo com o k={}: {}".format(
            #    k, self.W[i.valor][j.valor][k]))
        return self.W[i.valor][j.valor][k]

    def floyd_warshall_bottom_up(self):
        '''algoritmo 26.7'''
        self.W = [[[inf for k in self.V] for j in self.V] for i in self.V]
        # _iter = 1
        for i in self.V[1:]:
            for j in self.V[1:]:
                # print("Iteração {}: vertice i={} vértice j={}".format(
                #    _iter, i.valor, j.valor))
                if (i.valor == j.valor):
                    # print("\tMesmo vértice. Distância = 0")
                    self.W[i.valor][j.valor][0] = 0
                    j.predecessores[i.valor] = i
                elif self.matriz[i.valor][j.valor]:
                    # print("\tExiste aresta entre os vértices. Distância = {}".format(
                    #    self.w[i.valor][j.valor]))
                    self.W[i.valor][j.valor][0] = self.w[i.valor][j.valor]
                    j.predecessores[i.valor] = i
                else:
                    #    print("\tNão existe aresta entre os vértices. Distância = inf")
                    self.W[i.valor][j.valor][0] = inf
                    j.predecessores[i.valor] = None
                # _iter += 1
        # print("Preenchimento final de W")
        # _iter = 1
        for k in self.V[1:]:
            for i in self.V[1:]:
                for j in self.V[1:]:
                    # print("Iteração {}: k= {} com par de vértices ({}, {})".format(
                    #     _iter, k.valor, i.valor, j.valor))
                    nao_usa_k = self.W[i.valor][j.valor][k.valor-1]
                    usa_k = self.W[i.valor][k.valor][k.valor-1] +\
                        self.W[k.valor][j.valor][k.valor-1]
                    # print("Custo sem k: {}".format(nao_usa_k))
                    # print("Custo com k: {}".format(usa_k))
                    if nao_usa_k < usa_k:
                        # print("Melhor não usar")
                        self.W[i.valor][j.valor][k.valor] = nao_usa_k
                    else:
                        # print("Melhor usar")
                        self.W[i.valor][j.valor][k.valor] = usa_k
                        j.predecessores[i.valor] = j.predecessores[k.valor]
                    # _iter += 1
        return self.W

    def floyd_warshall_melhorado(self):
        '''algoritmo 26.8'''
        self.W = [[inf for j in self.V] for i in self.V]
        _iter = 1
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
                _iter += 1
        for k in self.V[1:]:
            for i in self.V[1:]:
                for j in self.V[1:]:
                    if self.W[i.valor][j.valor] > self.W[i.valor][k.valor]+self.W[k.valor][j.valor]:
                        self.W[i.valor][j.valor] = self.W[i.valor][k.valor] +\
                            self.W[k.valor][j.valor]
                        j.predecessores[i.valor] = j.predecessores[k.valor]
        return self.W

    def resolve_caminhos_todos_pares(self):
        '''algoritmo 26.9'''
        self.floyd_warshall_melhorado()
        # verificando ciclos negativos
        _iter = 1
        for i in self.V[1:]:
            print("Iteração {}".format(_iter))
            if self.W[i.valor][i.valor] < 0:
                print("Custo para {}-{}: {}".format(
                    i.valor, i.valor, self.W[i.valor][i.valor]))
                return None
            print("Custo para {}-{}: {}".format(
                i.valor, i.valor, self.W[i.valor][i.valor]))
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
        print("Início de Bellman-Ford")
        _D.bellman_ford(_D.V[s.valor])
        print("Fim de Bellman-Ford")
        if _D.ciclo_negativo:
            return "O digrafo D contém ciclo de peso negativo"
        D_ = deepcopy(self)
        for e in D_.E:
            u, v = e[0], e[1]
            D_.w[u][v] = _D.V[u].distancia + _D.w[u][v] - _D.V[v].distancia
        for u in self.V[1:]:
            print("Início de Dijkstra para o vértice {}".format(
                D_.V[u.valor].valor))
            D_.dijkstra(D_.V[u.valor])
            print("Fim de Dijkstra para o vértice {}".format(
                D_.V[u.valor].valor))
            for v in self.V[1:]:
                u.distancias[v.valor] = D_.V[v.valor].distancia +\
                    (_D.V[v.valor].distancia-_D.V[u.valor].distancia)
