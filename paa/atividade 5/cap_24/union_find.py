class UnionFind():
    def __init__(self, valor):
        self.valor = valor
        self.representante = self
        self.lista = [self.representante]
        self.tamanho = len(self.lista)

    def find_set(self):
        return self.representante

    @staticmethod
    def union(u, v):
        '''algoritmo 12.3'''
        X = u.find_set()
        Y = v.find_set()
        if X.tamanho < Y.tamanho:
            for _v in X.lista:
                _v.representante = Y
            Y.lista = Y.lista + X.lista
            X.lista = []
        else:
            for _v in Y.lista:
                _v.representante = X
            X.lista = X.lista + Y.lista
            Y.lista = []

    # @staticmethod
    # def _union(u, v):
    #     if u.representante.valor < v.representante.valor:
    #         if v.representante.valor == v.valor:
    #             for i in v.lista:
    #                 i.representante = u.representante
    #             u.representante.lista = u.representante.lista + v.lista
    #             v.lista = []
    #         else:
    #             for i in v.representante.lista:
    #                 i.representante = u.representante
    #             u.lista = u.lista + v.representante.lista
    #             v.representante.lista = []
    #     else:
    #         if u.representante.valor == u.valor:
    #             for i in u.lista:
    #                 i.representante = v.representante
    #             v.representante.lista = v.representante.lista + u.lista
    #             u.lista = []
    #         else:
    #             for i in u.representante.lista:
    #                 i.representante = v.representante
    #             v.lista = v.lista + u.representante.lista
    #             u.representante.lista = []
