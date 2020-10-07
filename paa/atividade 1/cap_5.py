def busca_linear_recursiva(A, n, x):
    """
    Algotimo 5.1
    Problema:
        Dado um vetor A[1:n] contendo n números reais e um número real k qualquer,
        descobrir se k está armazenado em A. 
    """
    if n < 0:
        return -1
    elif A[n] == x:
        return n
    return busca_linear_recursiva(A, n-1, x)


def fatorial(n):
    """
    Algotimo 5.2
    Problema:
        Calcular fatorial de n 
    """
    if n == 0:
        return 1
    return n * fatorial(n-1)


def potencia_v1(x, n):
    """
    Algotimo 5.3
    Problema:
        Calcular potência de x^n
    """
    if n == 0:
        return 1
    return x * potencia_v1(x, n-1)


def potencia_v2(x, n):
    """
    Algotimo 5.4
    Problema:
        Calcular potência de x^n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:  # n é par
        return potencia_v2(x, n/2) * potencia_v2(x, n/2)
    else:
        return x * potencia_v2(x, (n-1)/2) * potencia_v2(x, (n-1)/2)


def potencia_v3(x, n):
    """
    Algotimo 5.5
    Problema:
        Calcular potência de x^n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:  # n é par
        aux = potencia_v3(x, n/2)
        return aux*aux
    else:
        aux = potencia_v3(x, (n-1)/2)
        return x * aux * aux


def busca_binaria_recursiva(A, esq, _dir, x):
    """
    Algoritmo 5.6
    Problema>Dado um vetor A[1::n] contendo n números reais em ordem não-decrescente,
    i.e., A[i] <= A[i + 1] para todo 1 <= i < n, e um número real k qualquer,
    descobrir se k está armazenado em A.
    """
    if esq > _dir:
        return -1
    meio = (esq+_dir)//2
    if A[meio] == x:
        return meio
    elif x < A[meio]:
        return busca_binaria_recursiva(A, esq, meio-1, x)
    else:
        return busca_binaria_recursiva(A, meio+1, _dir, x)


def fibonacci_recursivo(n):
    """
    Algoritmo 5.7
    Problema: Dado um inteiro n >= 0, encontrar Fn.
    """
    if n <= 2:
        return 1
    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)


def fibonacci(n):
    """
    Algoritmo 5.8
    Problema: Dado um inteiro n >= 0, encontrar Fn.
    """
    if n <= 2:
        return 1
    F = [None]*n
    F[0] = 1
    F[1] = 1
    for i in range(2, n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Busca Linear Recursiva <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 123, 42, 66]
    print(busca_linear_recursiva(v, len(v)-1, 42))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Fatorial <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(fatorial(5))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Potência V1 <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(potencia_v1(2, 10))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Potência V2 <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(potencia_v2(2, 5))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Potência V3 <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(potencia_v3(2, 12))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Busca Binária Recursiva <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 312, 366, 1000]
    print(busca_binaria_recursiva(v, 0, len(v)-1, 312))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Fibonacci Recursivo <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(fibonacci_recursivo(10))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Fibonacci <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(fibonacci(11))
