import math


def example(a: float, b: float, x: float) -> float:
    one = math.pow((a * x + b), 1 / 3)
    two = math.log2(x)
    y = one / two
    return y


def example_a(a, b, xn, xk, dx):
    x = xn
    y = []
    while x <= xk:
        y_tmp = example(a, b, x)
        y.append(y_tmp)
        x += dx
    return y


def example_b(a, b, x):
    y = []
    for item in x:
        y.append(example(a, b, item))
    return y

if __name__ == "__main__":

    print(example(1.35, 0.98, 1.14))

    y = example_a(1.35, 0.98, 1.14, 4.24, 0.62)
    print(y)

    y = example_b(1.35, 0.98, [0.35, 1.28, 3.51, 5.21, 4.16])
    print(y)