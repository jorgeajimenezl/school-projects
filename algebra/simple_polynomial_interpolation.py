from gauss_jordan_elimination import gauss_jordan_elimination

def polynomial_interpolation(X, Y):
    n = len(X)
    assert len(X) == len(Y)
    A = []
    B = Y[:]

    for i in range(n):
        A.append([1] * n)
        for j in range(1, n):
            A[-1][j] = A[-1][j - 1] * X[i]

    print(A)
    C = gauss_jordan_elimination(A, B)
    return C


def main():
    C = polynomial_interpolation(
        X = [1, 4, 7, 8, 9],
        Y = [1, 3, 1, 6, 1]
    )

    print(" + ".join([f"{v}*x^{i}" for i, v in enumerate(C)]))

if __name__ == "__main__":
    main()