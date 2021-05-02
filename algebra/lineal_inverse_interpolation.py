def inverse_interpolation(f, a, b):
    # Initial condition
    assert f(a) * f(b) < 0, "sign(f(a)) != sign(f(b))"

    while 1:
        m = a - (f(a) * (b - a)) / (f(b) - f(a))

        if abs(f(m)) < 1E-6:
            return m

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

def main():
    x = inverse_interpolation (
        f = lambda x: 0.5*(x-5)**2-2,
        a = 2,
        b = 4
    )

    print(f"x = {x}")

if __name__ == "__main__":
    main()