def custo(a=0, b=0, gap=False):
    if gap:
        return -1
    elif a==b: return 2
    else: return -4
    
if __name__ == "__main__":
    X = "AGGGCT"
    Y = "AGGCA"
    m, n = len(X), len(Y)
    M = [[0] *(len(Y)+1) for i in range(len(X)+1)]
    M[0] = [0, -1, -2, -3, -4, -5]
    M[1] = [-1, 2, 1, 0, -1, -2]
    M[2] = [-2, 1, 4, 3, 2, 1]
    M[3] = [-3, 0, 3, 6, 5, 4]
    M[4] = [-4, -1, 2, 5, 4, 3]
    M[5] = [-5, -2, 1, 4, 7, 6]
    M[6] = [-6, -3, 0, 3, 6, 5]
    _X, _Y = [], []
    while m!=0 and m!=0:
        atual = M[m][n]
        if X[m-1] == Y[n-1]:
            if atual == M[m-1][n-1] + custo(X[m-1], Y[n-1]):
                _X.insert(0, X[m-1])
                _Y.insert(0, Y[n-1])
                m, n = m-1, n-1
        elif atual==M[m-1][n]+custo(gap=True):
            _X.insert(0, X[m-1])
            _Y.insert(0, "-")
            m, n = m-1, n
        else:
            _X.insert(0, "-")
            _Y.insert(0, Y[n-1])
            m, n = m, n-1
    print(_Y)
    print(_X)
