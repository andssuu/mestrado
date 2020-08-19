# Ler e implementar os algoritmos da Parte III (capítulos 13 a 17)

def insertion_sort(A, n):
	for i in range(1, n):
		atual=A[i]
		j=i-1
		while(j>=0 and A[j]>atual):
			A[j+1]=A[j]
			j-=1
		A[j+1]=atual

def shell_sort(A, n, H, m):
	for t in range(m):
		for i in range(H[t], n):
			atual=A[i]
			j=i-1
			while(j>=H[t]-1 and A[j-H[t]+1]>atual):
				A[j+1]=A[j-H[t]+1]
				j=j-H[t]
			A[j+1]=atual

def merge_sort(A, inicio, fim):
	if inicio<fim:
		meio = (inicio+fim)//2
		merge_sort(A, inicio, meio)
		merge_sort(A, meio+1, fim)
		combina(A, inicio, meio, fim)

def combina(A, inicio, meio, fim):
	n1 = meio-inicio+1
	n2 = fim - meio
	B, C = [], []
	for i in range(n1):
		B.append(A[inicio+i])
	for j in range(n2):
		C.append(A[meio+j+1])
	i = 0
	j = 0
	k = inicio
	while i<n1 and j<n2:
		if B[i]<=C[j]:
			A[k] = B[i]
			i+=1
		else:
			A[k] = C[j]
			j+=1
		k+=1
	while i<n1:
		A[k]=B[i]
		i+=1
		k+=1
	while j<n2:
		A[k] = C[j]
		j+=1
		k+=1

def selection_sort(A, n):
	for i in range(1, n)[::-1]:
		indice_max = i
		for j in range(i):
			if A[j]>A[indice_max]:
				indice_max = j
		A[indice_max], A[i] = A[i], A[indice_max]
	return A

def corrige_heap_descendo(H, i):
	maior = i-1
	if 2*i-1<=len(H)-1 and H[2*i-1]>H[maior]:
		maior = 2*i-1
	if 2*i<=len(H)-1 and H[2*i]>H[maior]:
		maior = 2*i
	if maior!=i-1:
		H[i-1], H[maior] = H[maior], H[i-1]
		corrige_heap_descendo(H, maior+1)

def constroi_heap(H):
	for i in range(len(H)//2)[::-1]:
		corrige_heap_descendo(H, i+1)

def heap_sort(A, n):
	constroi_heap(A)
	vector_sorted = []
	for i in range(1, n)[::-1]:
		A[0], A[i] = A[i], A[0]
		vector_sorted.insert(0, A[-1])
		A = A[:-1]
		corrige_heap_descendo(A, 1)
	vector_sorted.insert(0, A[-1])
	return (vector_sorted)

def quick_sort(A, inicio, fim):
	if inicio<fim:
		p = fim
		A[p], A[fim] = A[fim], A[p]
		x = particiona(A, inicio, fim)
		quick_sort(A, inicio, x-1)
		quick_sort(A, x+1, fim)

def particiona(A, inicio, fim):
	pivo = A[fim]
	i = inicio
	for j in range(inicio, fim):
		if A[j]<=pivo:
			A[i], A[j] = A[j], A[i]
			i+=1
	A[i], A[fim] = A[fim], A[i]
	return i

def counting_sort(A, k):
	B = [0 for x in range(len(A))]
	C = [0 for x in range(k)]
	for j in set(A):
		C[j] = A.count(j)
	for i in range(1, k):
		C[i] += C[i-1]
	for j in range(len(A))[::-1]:
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
	return B

if __name__ == '__main__':
	# Insertion Sort
	print("Insertion Sort")
	v = [2,5,1,4,3]
	print(v)
	insertion_sort(v, len(v))
	print(v)

	# Shell Sort
	print("Shell Sort")
	H = [4, 1]
	v = [10,2,5,1,4,3]
	print(v)
	shell_sort(v, len(v), H, len(H))
	print(v)

	# Merge Sort
	print("Merge Sort")
	v = [1,3,7,10,2,6,8,15]
	print(v)
	merge_sort(v, 0, len(v)-1)
	print(v)

	# Selection Sort
	print("Selection Sort")
	v = [2, 5, 1, 4, 3]
	print(v)
	selection_sort(v, len(v))
	print(v)

	# Heap Sort
	print("Heap Sort")
	v = [4,7,3,8,1,9]
	print(v)
	v = heap_sort(v, 6)
	print(v)

	# Quick Sort
	print("Quick Sort")
	v = [3, 9, 1, 2, 7, 4, 8, 5, 0, 6]
	print(v)
	quick_sort(v, 0, 9)
	print(v)

	# Counting Sort
	print("Counting Sort")
	v = [3, 0, 5, 4, 3, 0, 1, 2]
	print(v)
	v = counting_sort(v, 6)
	print(v)
