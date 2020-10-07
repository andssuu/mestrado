from copy import deepcopy
from math import inf

from vertice import Vertice
from union_find import UnionFind
from heap import insere_heap, remove_heap, altera_heap


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

    def verifica_ciclo(self, s, matriz_aux):
        s.visitado = 1
        for v in self.vizinhanca(s):
            if matriz_aux[s.valor][v.valor]:
                continue
            matriz_aux[s.valor][v.valor], matriz_aux[v.valor][s.valor] = 1, 1
            if v.visitado:
                matriz_aux[0][0] = 1
            self.verifica_ciclo(v, matriz_aux)

    def kruskal(self):
        '''algoritmo 24.1'''
        C = sorted(deepcopy(self.E), key=lambda e: e[2])
        F = []  # conjunto de arestas
        for c in C:
            _G = MatrizAdjacencias(
                [v.valor for v in deepcopy(self.V)], E=F+[c])
            matriz_aux = [[0 for x in range(len(self.V))]
                          for y in range(len(self.V))]
            _G.verifica_ciclo(_G.V[c[0]], matriz_aux)
            if not matriz_aux[0][0]:
                F = F+[c]
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
                    print("Aresta mímina {}-{} adicionada com peso {}".format(e[0], e[1],
                                                                              e[2]))
                    self.V[e[1]].visitado = 1
                    self.V[e[1]].predecessor = self.V[e[0]]
                    visitados.append(
                        [self.V[e[0]].valor, self.V[e[1]].valor])
                    break
                elif self.V[e[0]].visitado == 0 and self.V[e[1]].visitado == 1:
                    print("Aresta mímina {}-{} adicionada com peso {}".format(e[0], e[1],
                                                                              e[2]))
                    self.V[e[0]].visitado = 1
                    self.V[e[0]].predecessor = self.V[e[1]]
                    visitados.append(
                        [self.V[e[1]].valor, self.V[e[0]].valor])
                    break
            _n += 1
        # print("Lista de arestas utilizadas: ")
        # [print(x) for x in visitados]

    def prim_heap(self):
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
        print("Árvore geradora")
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

    def _d_plus(self, s):
        return

    def _arco(self, s, v):
        self.matriz[s.valor][v.valor] = 0
        self.chama_busca(tipo_busca='profundidade')
        if self.V[v.valor].visitado:
            self.matriz[s.valor][v.valor] = 1
            return True
        else:
            self.matriz[s.valor][v.valor] = 1
            return False
