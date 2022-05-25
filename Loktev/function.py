import math


def f(a:float, b:float, x:float) -> float:

    chisl = b**3 + math.sin(a*x)**2
    znam =  math.acos(x*(b**x)) + math.exp(-x/2)
    return chisl / znam


def task_a(a:float, b:float, xn:float, xk:float, dx:float) -> list:

    y = []
    while xn < xk:
        y.append(f(a, b, xn))
        xn += dx
    return y


def task_b(a:float, b:float, x:enumerate) -> list:

    y = []
    for i in x:
        y.append(f(a, b, i))
    return y


if __name__ == '__main__':

    print(f(1.2, 0.48, 0))

    print('Task A')
    print(task_a(1.2, 0.48, 0.7, 2.2, 0.3))

    print('Task B')
    print(task_b(1.2, 0.48, (0.25, 0.36, 0.56, 0.94, 1.28)))
