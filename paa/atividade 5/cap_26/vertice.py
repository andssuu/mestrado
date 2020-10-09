class Vertice():
    def __init__(self, valor, prioridade=None, indice=None):
        self.valor = valor
        self.visitado = 0
        self.predecessor = None
        self.distancia = 0
        self.prioridade = prioridade
        self.indice = indice  # a indicar a posição do heap em que x está armazenado
        self.predecessores = []
        self.distancias = []
