def bisection(f, a, b):
    # Initial condition
    assert f(a) * f(b) < 0, "sign(f(a)) != sign(f(b))"

    while abs(a - b) > 1E-10:
        m = (a + b) * 0.5

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return a

def main():
    x = bisection (
        f = lambda x: x**2 + 4*x + 2,
        a = -2,
        b = 2
    )

    print(f"x = {x}")

if __name__ == "__main__":
    main()