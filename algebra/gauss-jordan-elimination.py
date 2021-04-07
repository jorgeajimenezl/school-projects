import math

M = [
    [1, -1, 2, -1],
    [1, 1, 1, 0],
    [2, -2, 3, -1],
    [1, -1, 4, 1]
]

N = [5, 1, 10, 3]

def gauss_jordan_elimination(A, B):
    n = len(A)
    assert (len(A) == len(B))
    assert (all([len(x) == n for x in A]))
    
    for k in range(n):
        if abs(A[k][k]) < 1E-5:
            continue
        for i in range(n):
            if i == k:
                continue

            m = A[i][k] / A[k][k] # pivot
            for j in range(k, n):
                A[i][j] = A[i][j] - m * A[k][j]
            B[i] = B[i] - m * B[k]

    return [B[i] / A[i][i] for i in range(n)]

# More stable from original method
def gauss_jordan_elimination_stable(A, B):
    n = len(A)
    assert (len(A) == len(B))
    assert (all([len(x) == n for x in A]))
    
    for k in range(n):
        if A[k][k] == 0:
            continue        
        for i in range(n):
            for j in range(k, n):
                A[i][j] = A[k][k] * A[i][j] - A[k][j] * A[i][k]
            B[i] = A[k][k] * B[i] - A[i][k] * B[k]

            # normalize row
            m = A[i][k + 1]
            for j in range(k + 1, n):
                m = math.gcd(m, A[i][j])                
            if m > 1:
                for j in range(k + 1, n):
                    A[i][j] //= m        

    return [B[i] / A[i][i] for i in range(n)]
    
def main():
    print(gauss_jordan_elimination(M, N))

if __name__ == "__main__":
    main()