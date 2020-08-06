# Problema 1: Implemente o algoritmo de remoção em listas simplesmente encadeadas.

class ListaEncadeada:
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

  def inserir(self, x):
    x.proximo = None
    if self.calda != None:
      self.calda.proximo = x
    else:
      self.cabeca = x
    self.calda = x

  def remover(self, k):
    x = self.cabeca
    while (x!=None) and (x.chave!=k):
      anterior = x
      x = x.proximo
    if x == None:
      return None
    if x == self.cabeca:
      self.cabeca = x.proximo
    elif x == self.calda:
      anterior.proximo = None
      self.calda = anterior
    else:
      anterior.proximo = x.proximo

class Nodo:
  def __init__(self, chave):
    self.chave = chave
    self.proximo = None

  def __repr__(self):
    return str(self.chave)

if __name__ == '__main__':
    lista = ListaEncadeada()
    print(lista)
    n1, n2, n3 = Nodo(11), Nodo(22), Nodo(33)
    lista.inserir(n1)
    print(lista)
    lista.inserir(n2)
    print(lista)
    lista.inserir(n3)
    print(lista)
    lista.remover(22)
    print(lista)
    lista.remover(11)
    print(lista)
    lista.remover(33)
    print(lista)
