import math

# def calc(a, b, x):


def calc(a: float, b: float, x: float) -> float:
    chisl = (math.sin(a + b * x)) ** 3.5
    znamen = 1 + math.cos(abs(math.log(a + b * x, 2)))
    y = chisl / znamen
    return y


def task_a(a, b, xn, xk, dx):

    x = xn
    y = []

    while x <= xk:
        y_tmp = calc(a, b, x)
        y.append(y_tmp)
        x += dx
    return y


def task_b(a, b, x):
    y = []
    for item in x:
        y.append(calc(a, b, item))
    return y


if __name__ == '__main__':
    print(calc(2.5, 4.6, 1.15))

    y = task_a(2.5, 4.6, 1.15, 3.05, 0.38)
    print(y)

    y = task_b(2.5, 4.6, [1.2, 1.36, 1.57, 1.93, 2.25])
    print(y)
