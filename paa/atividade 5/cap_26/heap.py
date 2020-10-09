from vertice import Vertice


def corrige_heap_descendo(h, i):
    i -= 1
    maior = i
    if (2*(i+1)-1 < len(h)) and (h[2*(i+1)-1].prioridade > h[maior].prioridade):
        maior = 2*(i+1)-1
    if (2*(i+1) < len(h)) and (h[2*(i+1)].prioridade > h[maior].prioridade):
        maior = 2*(i+1)
    if maior != i:
        h[i].indice, h[maior].indice = h[maior].indice, h[i].indice
        h[i], h[maior] = h[maior], h[i]
        corrige_heap_descendo(h, maior+1)


def remove_heap(h):
    x = None
    if len(h) >= 1:
        x = h[0]
        h[-1].indice = 1
        h[0] = h[-1]
        h = h[:-1]
        corrige_heap_descendo(h, 1)
    return x, h


def corrige_heap_subindo(h, i):
    pai = (i//2)-1
    i -= 1
    if i >= 1 and h[i].prioridade > h[pai].prioridade:
        h[i].indice, h[pai].indice = h[pai].indice, h[i].indice
        h[i], h[pai] = h[pai], h[i]
        corrige_heap_subindo(h, pai+1)


def insere_heap(h, v):
    h.append(v)
    v.indice = len(h)
    corrige_heap_subindo(h, len(h))


def altera_heap(h, i, k):
    aux = h[i-1].prioridade
    h[i-1].prioridade = k
    if aux < k:
        corrige_heap_subindo(h, i)
    if aux > k:
        corrige_heap_descendo(h, i)
    # return h


def consulta_heap(h):
    return h[0]
