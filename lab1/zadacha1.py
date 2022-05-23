import math


def calc(x:float) -> float:
    chisl = (math.asin(x)**4 + math.acos(x)**6)*1/7
    return y

def task_a(xn, xk, dx):
        x=xn
        y=[]
        while x <= xk:
           y_tmp = calc(x)
           y.append(y_tmp)
           x += dx
        return y

if __name__ == "__main__":
        y= task_a(0.22, 0.92, 0,14)
        print (y)    
