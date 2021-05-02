def newton(f, d, x0):
    x = x0
    
    while abs(f(x)) > 1E-6:
        x -= f(x) / d(x)

    return x

def main():
    x = newton (
        f = lambda x: x**2 + 4*x + 2,
        d = lambda x: 2*x + 4,
        x0 = 0
    )

    print(f"x = {x}")

if __name__ == "__main__":
    main()