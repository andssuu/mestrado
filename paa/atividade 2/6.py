# Problema 6: Implemente o tipo heap e suas operações
class Heap():
	def __init__(self, lista):
		self.l = lista

	def __repr__(self):
		return str([x.prioridade for x in self.l])

class Nodo():
	def __init__(self, prioridade=None, indice=None):
		self.prioridade = prioridade
		self.indice = indice

def corrige_heap_descendo(h, i):
	i-=1
	maior = i
	if (2*(i+1)-1<len(h)) and (h[2*(i+1)-1].prioridade>h[maior].prioridade):
		maior = 2*(i+1)-1
	if (2*(i+1)<len(h)) and (h[2*(i+1)].prioridade>h[maior].prioridade):
		maior = 2*(i+1)
	if maior!=i:
		h[i].indice, h[maior].indice = h[maior].indice, h[i].indice
		h[i], h[maior] = h[maior], h[i]
		corrige_heap_descendo(h, maior+1)

def corrige_heap_subindo(h, i):
	pai = (i//2)-1
	i-=1
	if i>=1 and h[i].prioridade>h[pai].prioridade:
		h[i].indice, h[pai].indice = h[pai].indice, h[i].indice
		h[i], h[pai] = h[pai], h[i]
		corrige_heap_subindo(h, pai+1)

def constroi_heap(h, n):
	heap = [Nodo() for x in range(n)]
	for i, v in enumerate(h):
		heap[i].indice = i
		heap[i].prioridade = v
	#print([x.prioridade for x in heap])
	for i in reversed(range(n//2)):
		corrige_heap_descendo(heap, i+1)
		#print([x.prioridade for x in heap])
	return heap

def insere_heap(h, x):
	nodo = Nodo(x, len(h)-1)
	h.append(nodo)
	corrige_heap_subindo(h, len(h))

def remove_heap(h):
	if len(h)>=1:
		h[0].indice, h[0].prioridade = h[-1].indice, h[-1].prioridade
		h = h[:-1]
		corrige_heap_descendo(h, 1)
	return h

def altera_heap(h, i, k):
	aux = h[i-1].prioridade
	h[i-1].prioridade = k
	if aux < k:
		corrige_heap_subindo(h, i)
	if aux > k:
		corrige_heap_descendo(h, i)
	return h

def maior_prioridade(h):
	return h[0]


if __name__ == '__main__':
	print("Corrigindo Heap descendo")
	heap = Heap([Nodo(v, i) for i, v in enumerate([100,3,36,17,8,25,1,7,12,5])])
	print(heap)
	corrige_heap_descendo(heap.l, 2)
	print(heap)

	print("Corrigindo Heap subindo")
	heap = Heap([Nodo(v, i) for i, v in enumerate([100,17,36,12,8,125,1,7,2,5])])
	print(heap)
	corrige_heap_subindo(heap.l, 6)
	print(heap)

	print("Contruindo a Heap")
	l = [3, 1, 5, 8, 2, 4, 7, 6, 9]
	heap = constroi_heap(l, len(l))
	print([x.prioridade for x in heap])

	print("Inserção na Heap")
	l = [3, 1, 5, 8, 2, 4, 7, 6, 9]
	heap = constroi_heap(l, len(l))
	insere_heap(heap, 12)
	print([x.prioridade for x in heap])

	print("Remoção na Heap")
	for i in range(9):
		heap = remove_heap(heap)
		print([x.prioridade for x in heap])

	print("Alteração na Heap")
	l = [3, 1, 5, 8, 2, 4, 7, 6, 9]
	heap = constroi_heap(l, len(l))
	print([x.prioridade for x in heap])
	heap = altera_heap(heap, 1, 100)
	print([x.prioridade for x in heap])

	print("Maior prioridade na Heap: ", end="")
	print(maior_prioridade(heap).prioridade)
