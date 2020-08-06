"""
Problema 5: Implementar as operações da página 99 do livro da  Profa Carla Negri.
	1. Encontrar o menor elemento
	2. Encontrar o maior elemento
	3. O sucessor de um elemento k
	4. O predecessor de um elemento k
"""
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

def maximo_abb(r):
	if r.dir != None:
		return maximo_abb(r.dir)
	return r

def sucessor_abb(r, k):
	x = busca_abb(r, k)
	if x.dir is not None:
		return minimo_abb(x.dir)
	ancestrais = []
	while r!=None and r.chave!=x.chave:
		if x.chave > r.chave:
			r = r.dir
		else:
			ancestrais.append(r.chave)
			r = r.esq
	if len(ancestrais):
		return min(ancestrais)
	return None

def predecessor_abb(r, k):
	x = busca_abb(r, k)
	if x.esq is not None:
		return maximo_abb(x.esq)
	ancestrais = []
	while r!=None and r.chave!=x.chave:
		if x.chave > r.chave:
			ancestrais.append(r.chave)
			r = r.dir
		else:
			r = r.esq
	if len(ancestrais):
		return max(ancestrais)
	return None

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
	insere_abb(arvore.raiz, Nodo(6))
	insere_abb(arvore.raiz, Nodo(3))
	print("Menor elemento:", minimo_abb(arvore.raiz))
	print("Maior elemento:", maximo_abb(arvore.raiz))
	print("Sucessor: ", sucessor_abb(arvore.raiz, 9))
	print("Predecessor: ", predecessor_abb(arvore.raiz, 14))
