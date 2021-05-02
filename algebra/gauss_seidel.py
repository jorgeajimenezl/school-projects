import math

def error(A, gamma):
    n = len(A)
    alpha = 0

    for i in range(n):
        p = sum([abs(A[i][j] / A[i][i]) for j in range(i)])
        q = sum([abs(A[i][j] / A[i][i]) for j in range(i + 1, n)])
        alpha = max(q / (1 - p), alpha)

    return (alpha) / (1 - alpha) * gamma
    
def gauss_seidel(A, B):
    n = len(A)
    assert len(A) == len(B)
    assert all([len(x) == n for x in A])

    X = [0] * n
    e = 1
    k = 0
    
    while e > 1E-8:
        gamma = -(1 << 30)

        for i in range(n):
            sum = 0
            for  j in range(n):
                if i != j:
                    sum += A[i][j] * X[j]
            
            old = X[i]
            X[i] = (B[i] - sum) / A[i][i]
            gamma = max(gamma, abs(X[i] - old))

        # print(f"Iteration #{k}: {X}")
        e = error(A, gamma)
        k += 1

    return X, k
    
def main():
    sol, iterations = gauss_seidel(
        A = [
            [-6, 0, 12],
            [4, -1, -1],
            [10, 7, -1]
        ], 
        B = [60, -2, 42]
    )
    print('\n'.join([f"x{i} = {v}" for i, v in enumerate(sol)]))
    print(f"Iterations: {iterations}")

if __name__ == "__main__":
    main()