def somatorio_par(A, n):
    """
    Algotimo 3.1
    Problema: 
        Encontrar a soma dos elementos pares de um vetor. 
    """
    soma = 0
    for i in range(n):
        if not A[i] % 2:  # é par
            soma += A[i]
    return soma


def busca_linear(A, n, x):
    """
    Algotimo 3.2
    Problema:
        Dado um vetor A[1:n] contendo n números reais e um número real k qualquer,
        descobrir se k está armazenado em A. 
    """
    i = 0
    while (i < n):
        if A[i] == x:
            return i
        i += 1
    return -1


def busca_linear_ordem(A, n, x):
    """
    Algotimo 3.3
    Problema:
        Dado um vetor A[1:n] contendo n números reais em ordem não-decrescente,
        i.e., A[i] <= A[i + 1] para todo 1 <= i < n, e um número real k qualquer,
        descobrir se k está armazenado em A.
    """
    i = 0
    while (i < n and x >= A[i]):
        if A[i] == x:
            return i
        i += 1
    return -1


def busca_binaria(A, n, x):
    """
    Algoritmo 3.4
    Problema>Dado um vetor A[1::n] contendo n números reais em ordem não-decrescente,
    i.e., A[i] <= A[i + 1] para todo 1 <= i < n, e um número real k qualquer,
    descobrir se k está armazenado em A.
    """
    esq = 0
    _dir = n-1
    while (esq <= _dir):
        meio = (esq+_dir)//2
        if A[meio] == x:
            return meio
        elif x > A[meio]:
            esq = meio+1
        else:
            _dir = meio-1
    return -1


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Somatório Par  <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 13, 43, 60]
    print(somatorio_par(v, len(v)))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Busca Linear <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 123, 42, 66]
    print(busca_linear(v, len(v), 123))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Busca Linear Em Ordem <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 23, 42, 66]
    print(busca_linear_ordem(v, len(v), 23))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Busca Binária <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 312, 366, 1000]
    print(busca_binaria(v, len(v), 6))
