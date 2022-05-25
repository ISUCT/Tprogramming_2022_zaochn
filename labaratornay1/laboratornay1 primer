import math


def f(a:float, b:float, x:float) -> float:

    chisl = math.asin(x**a)
    znam =  math.acos(x**b)
    return chisl + znam


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

    print(f(2.0, 3.0, 0))

    print('Task A')
    print(task_a(2.0, 3.0, 0.11, 0.36, 0.05))

    print('Task B')
    print(task_b(2.0, 3.0, (0.08, 0.26, 0.35, 0.41, 0.53)))
