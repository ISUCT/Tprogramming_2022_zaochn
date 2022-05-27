import math

def summ(a:float, b:float) -> float:
    return a + b

# def calc(a:float, b: float, x: float) -> float:
def calc(a, b, x):
    chisl = (math.sin(a + b*x))**3.5
    znamen = 1 + math.cos(abs(math.log(a + b*x, 2)))
    y = chisl / znamen
    return y

def task_a(a, b, xn, xk, dx): 
    x = xn
    x_arr = []
    y = []
    while x <= xk:
        y.append(calc(a, b, x))
        x_arr.append(x)
        x += dx
    return (x_arr,y)

def task_b(a, b, x):
    y = []
    for item in x:
        y.append(calc(a, b, item))
    return y

if __name__ == "__main__":
    print(calc(2.5, 4.6, 1.15))
    x, y = task_a(2.5, 4.6, 1.15, 3.05, 0.38) # (x,y)

    for i in range(len(x)):
        print(f"x={x[i]}    y={y[i]}")
        
    y = task_b(2.5, 4.6,[1.2, 1.36, 1.57, 1.93, 2.25])
    print(y)