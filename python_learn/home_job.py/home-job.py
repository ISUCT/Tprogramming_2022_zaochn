import math


def example(a: float, b: float, x: float) -> float:
    one = 1 + math.log2(x / a)
    two = b - math.exp(x / a)
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


print(example(2, 0.95, 1.25))

y = example_a(2, 0.95, 1.25, 2.75, 0.3)
print(y)

y = example_b(2, 0.95, [2.2, 3.78, 4.51, 6.58, 1.2])
print(y)
