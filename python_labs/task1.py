import math

# def calc(a: float, b: float, x: float) -> float:
def calc(a, b, x) -> float:
    chisl = (math.sin(a + b*x))**3.5
    znamen = 1 + math.cos(abs(math.log(a + b*x, 2)))
    y = chisl / znamen
    return y

if __name__ == "__main__":
    print(calc(2.5, 4.6, 1.15))

# 18 вариант
def task_example(a, b, x):
    chisl = (a + b*x)**2,5
    znamen = 1 + math.log(a + b*x)
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

if __name__ == "__main__":
    print(task_a(2.5, 4.6, 1.1))
    y = task_a()

