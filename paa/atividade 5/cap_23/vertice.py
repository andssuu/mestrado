class Vertice():
    def __init__(self, valor):
        self.valor = valor
        self.visitado = 0
        self.predecessor = None
        self.distancia = 0
        self.componente = None
        self.rotulo = 0
