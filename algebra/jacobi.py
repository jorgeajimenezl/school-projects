import math

def error(A, X, S):
    n = len(A)
    alpha = 0

    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum += abs(A[i][j] / A[i][i])
        alpha = max(alpha, sum)

    gamma = max([abs(S[i] - X[i]) for i in range(n)])
    return (alpha) / (1 - alpha) * gamma
    
def jacobi(A, B):
    n = len(A)
    assert (len(A) == len(B))
    assert (all([len(x) == n for x in A]))

    X = [0] * n
    e = 1
    k = 0

    while e > 1E-8:
        S = X[:]
        for i in range(n):
            sum = 0
            for  j in range(n):
                if i != j:
                    sum += A[i][j] * X[j]
            S[i] = (B[i] - sum) / A[i][i]

        # print(f"Iteration #{k}: {S}")
        e = error(A, X, S)
        X = S
        k += 1

    return X, k
    
def main():
    sol, iterations = jacobi(
        A = [
            [1, -3, 12],
            [5, -12, 2],
            [4, 2, 2]
        ], 
        B = [10, -33, 70]
    )
    print('\n'.join([f"x{i} = {v}" for i, v in enumerate(sol)]))
    print(f"Iterations: {iterations}")

if __name__ == "__main__":
    main()