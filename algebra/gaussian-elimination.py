import math

def gaussian_elimination(A, B):
    n = len(A)
    assert (len(A) == len(B))
    assert (all([len(x) == n for x in A]))
    
    for k in range(n - 1):
        if abs(A[k][k]) < 1E-5:
            continue

        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            B[i] = B[i] - m * B[k]

    X = [0] * n
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * X[j]
        X[i] = (B[i] - sum) / A[i][i]

    return X

# More stable
# Only add errors when is computing solutions
def gaussian_elimination_stable(A, B):
    n = len(A)
    assert len(A) == len(B)
    assert all([len(x) == n for x in A])
    
    for k in range(n - 1):
        if A[k][k] == 0:
            continue        
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = A[k][k] * A[i][j] - A[k][j] * A[i][k]
            B[i] = A[k][k] * B[i] - A[i][k] * B[k]

            # normalize row
            m = A[i][k]
            if m == 0:
                continue
            for j in range(k, n):
                m = math.gcd(m, A[i][j])
            for j in range(k, n):
                A[i][j] //= m        

    X = [0] * n
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * X[j]
        X[i] = (B[i] - sum) / A[i][i]

    return X
    
def main():
    sol = gaussian_elimination_stable(
        A = [
            [1, 1],
            [2, 1]
        ], 
        B = [1, 3]
    )

    print('\n'.join([f"x{i} = {v}" for i, v in enumerate(sol)]))

if __name__ == "__main__":
    main()