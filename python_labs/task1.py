import math

# def calc(a: float, b: float, x: float) -> float:
def calc(a, b, x) -> float:
    chisl = (math.sin(a + b*x))**3.5
    znamen = 1 + math.cos(abs(math.log(a + b*x, 2)))
    y = chisl / znamen
    return y

if __name__ == "__main__":
    print(calc(2.5, 4.6, 1.15))