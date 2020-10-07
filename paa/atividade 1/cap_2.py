def somatorio(A, n):
    """
    Algotimo 2.1
    Problema:
        Calcular a soma dos valores armazenados em um vetor A de tamanho n.
    """
    soma = 0
    for i in range(n):
        soma += A[i]
    return soma


def produtorio(A, n):
    """
    Algotimo 2.2
    Problema:
        Recebe um vetor A[1:n] e deve devolver o produtório de seus elementos
    """
    produto = 1
    for i in range(n):
        produto *= A[i]
    return produto


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Somatório  <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 123, 42, 66]
    print(somatorio(v, len(v)))
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Produtório  <<<<<<<<<<<<<<<<<<<<<<<<<")
    v = [2, 5, 6, 7, 123, 42, 66]
    print(produtorio(v, len(v)))
