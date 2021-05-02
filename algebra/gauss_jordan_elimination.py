import math
from fractions import Fraction

def gauss_jordan_elimination(A, B):
    # Make use fractions
    A = [[Fraction(c) for c in r] for r in A]

    n = len(A)
    assert len(A) == len(B)
    assert all([len(x) == n for x in A])
    
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
    
def main():
    sol = gauss_jordan_elimination(
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