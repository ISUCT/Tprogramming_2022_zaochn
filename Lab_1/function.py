import math


def f(a:float, b:float, x:float) -> float:

    chisl = math.log((x**2) - 1)
    znam =  math.log(a * x**2 - b, 5)
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

    # print(f(1.1, 0.09, 0))

    print('Task A')
    print(task_a(1.1, 0.09, 1.2, 2.2, 0.2))

    print('Task B')
    print(task_b(1.1, 0.09, (1.21, 1.76, 2.53, 3.48, 4.52)))
