class UnionFind():
    def __init__(self, valor):
        self.valor = valor
        self.representante = self
        self.lista = [self.representante]

    def tamanho(self):
        return len(self.lista)

    def find_set(self):
        return self.representante

    @staticmethod
    def union(u, v):
        '''algoritmo 12.3'''
        X = u.find_set()
        Y = v.find_set()
        if X.tamanho() < Y.tamanho():
            for _v in X.lista:
                _v.representante = Y
            Y.lista = Y.lista + X.lista
            X.lista = []
        else:
            for _v in Y.lista:
                _v.representante = X
            X.lista = X.lista + Y.lista
            Y.lista = []
