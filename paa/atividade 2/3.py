# Problema 3: Implementar uma Fila em uma lista simplesmente encadeada.

class Fila:
  def __init__(self):
    self.cabeca = None
    self.calda = None

  def __repr__(self):
    nodo = self.cabeca
    nodos = []
    while nodo is not None:
      nodos.append(str(nodo.chave))
      nodo = nodo.proximo
    nodos.append("Null")
    return " -> ".join(nodos)

  def enfileirar(self, x):
    x.proximo = None
    if self.calda != None:
      self.calda.proximo = x
    else:
      self.cabeca = x
    self.calda = x

  def desenfileirar(self):
    if self.cabeca == None:
      return None
    elif self.cabeca == self.calda:
      self.cabeca, self.cabeca = None, None
    else:
      self.cabeca = self.cabeca.proximo

class Nodo:
  def __init__(self, chave):
    self.chave = chave
    self.proximo = None

  def __repr__(self):
    return str(self.chave)

if __name__ == '__main__':
    fila = Fila()
    print(fila)
    n1, n2, n3 = Nodo(1), Nodo(2), Nodo(3)
    fila.enfileirar(n1)
    print(fila)
    fila.enfileirar(n2)
    print(fila)
    fila.enfileirar(n3)
    print(fila)
    fila.desenfileirar()
    print(fila)
    fila.desenfileirar()
    print(fila)
    fila.desenfileirar()
    print(fila)
