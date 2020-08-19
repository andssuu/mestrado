# Pesquisar sobre a Ordenação da Bolha (Bubble Sort): análise e implementação
'''
Análise

O Bubble sort é um dos mais simples algoritmos de ordenação. A ideia consiste
basicamente em percorrer um vetor e comparar dois elementos adjacentes e trocar
suas posições, caso o primeiro elemento seja maior que o segundo elemento.

Sua complexidade no pior caso é de n² passos; n, no melhor caso.

'''
def bubble_sort(vector):
    n = len(vector)-1
    for i in range(n):
        for j in range(0, n-i):
            if vector[j] > vector[j+1] :
                vector[j], vector[j+1] = vector[j+1], vector[j]

if __name__ == '__main__':
	v = [94, 17, 22, 13, 45, 12, 2020]
	print(v)
	bubble_sort(v)
	print(v)
