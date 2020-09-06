if __name__ == "__main__":
    v = [15, 12, 17, 18, 15, 10, 15]
    w = [3, 4, 2, 5, 2, 3, 1]
    W = 10
    M = [[0] *(W+1) for i in range(len(v)+1)]
    for j in range(1, len(v)+1):
        for x in range(W+1):
            if w[j-1]>x:
                M[j][x] = M[j-1][x]
            else:
                usa = v[j-1] + M[j-1][x-w[j-1]]
                nao_usa = M[j-1][x]
                M[j][x] = max(usa, nao_usa)
    print(M[len(v)][W])
