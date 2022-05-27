import math

def summ(a:float, b:float) -> float:
    return a + b

def example(a: float, b: float, x: float) -> float:
    one = 1 + math.log(x / a, 2)
    two = b - math.exp(x / a)
    y = one / two
    return y


def example_a(a, b, xn, xk, dx):
    x = xn
    x_arr = []
    y = []
    while x <= xk:
        y.append(example(a, b, x))
        x_arr.append(x)
        x += dx
    return (x_arr, y)


def example_b(a, b, x):
    y = []
    for item in x:
        y.append(example(a, b, item))
    return y

if __name__ == "__main__":    

    print(example(2, 0.95, 1.25))

    x, y = example_a(2, 0.95, 1.25, 2.75, 0.3) # (x, y)
    print(x, y)

    y = example_b(2, 0.95, [2.2, 3.78, 4.51, 6.58, 1.2])
    print(y)
