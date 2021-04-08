import math

def lu_factorize(A):
    n = len(A)
    assert (all([len(x) == n for x in A]))

    l = [[0] * n for _ in range(n)]
    u = [[0] * n for _ in range(n)]

    for j in range(n):
        u[0][j] = A[0][j]
        l[j][j] = 1

    for i in range(1, n):
        l[i][0] = A[i][0] / u[0][0]

        for j in range(1, i):
            sum = 0
            for k in range(j):
                sum += l[i][k] * u[k][j]
            l[i][j] = (A[i][j] - sum) / u[j][j]

        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += l[i][k] * u[k][j]
            u[i][j] = (A[i][j] - sum)

    return (l, u)

def compute_solution(A, B):
    n = len(A)
    L, U = lu_factorize(A)

    Y = [0] * n
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * Y[j]
        Y[i] = B[i] - sum

    X = [0] * n
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * X[j]
        X[i] = (Y[i] - sum) / U[i][i]

    return X


def main():
    sol = compute_solution(
        A = [
            [1, -1, 2, -1],
            [1, 1, 1, 0],
            [2, -2, 3, -1],
            [1, -1, 4, 1]
        ], 
        B = [5, 1, 10, 3]
    )
    print('\n'.join([f"x{i} = {v}" for i, v in enumerate(sol)]))

if __name__ == "__main__":
    main()       

