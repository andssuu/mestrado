# Problema 4: Implementar arvore binarias de busca e suas operações.

class ArvoreBinaria:
	def __init__(self, raiz):
		self.raiz = raiz

class Nodo:
  def __init__(self, chave):
    self.chave = chave
    self.esq = None
    self.dir = None

  def __repr__(self):
    return str(self.chave)

def imprime_abb(r=None):
	if r is None:
		return None
	_esq = "Null" if r.esq is None else r.esq.chave
	_dir = "Null" if r.dir is None else r.dir.chave
	print("{} -> {}, {}".format(r.chave, _esq, _dir))
	if r.esq is not None: imprime_abb(r.esq)
	if r.dir is not None: imprime_abb(r.dir)

def busca_abb(r, k):
	if r == None or k == r.chave:
		return r
	elif k < r.chave:
		return busca_abb(r.esq, k)
	else:
		return busca_abb(r.dir, k)

def insere_abb(r, x):
	if r == None:
		return x
	if x.chave < r.chave:
		r.esq = insere_abb(r.esq, x)
	elif x.chave > r.chave:
		r.dir = insere_abb(r.dir, x)
	return r

def minimo_abb(r):
	if r.esq != None:
		return minimo_abb(r.esq)
	return r

def remove_abb(x, k):
	if x == None:
		return None
	if k < x.chave:
		x.esq = remove_abb(x.esq, k)
	elif k > x.chave:
		x.dir = remove_abb(x.dir, k)
	else:
		if x.esq == None:
			x = x.dir
		elif x.dir == None:
			x = x.esq
		else:
			y = minimo_abb(x.dir)
			x.chave = y.chave
			x.dir = remove_abb(x.dir, y.chave)
	return x

if __name__ == '__main__':
	arvore = ArvoreBinaria(Nodo(11))
	insere_abb(arvore.raiz, Nodo(9))
	insere_abb(arvore.raiz, Nodo(15))
	insere_abb(arvore.raiz, Nodo(13))
	insere_abb(arvore.raiz, Nodo(14))
	insere_abb(arvore.raiz, Nodo(12))
	imprime_abb(arvore.raiz)
	print("\nBuscando nodo {}".format(13))
	imprime_abb(busca_abb(arvore.raiz, 13))
	print("\nRemovendo nodo {}".format(13))
	imprime_abb(remove_abb(arvore.raiz, 13))
