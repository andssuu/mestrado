def combinacao(n, k):
    if M[n][k] == -1:
        if k==0 or k==n:
            return 1
        else: 
            M[n][k] = combinacao(n-1, k-1)+combinacao(n-1, k)
    return M[n][k]

if __name__ == "__main__":
    n = 6
    k = 2
    M = [[-1] * (k+1) for i in range(n+1)]
    print(combinacao(n, k))
