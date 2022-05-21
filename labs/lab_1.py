import math

def calc(a: float, b: float, x: float) -> float:
    chisl = a*math.sqrt(x) - b*math.log(x, 5)
    znamen = math.log10(abs(x - 1))
    y = chisl / znamen
    return y

def task_a(a: int, b: float, xn: float, xk: float, dx: float) -> list:
    x = xn
    result_array = []
    while x <= xk:
        result_array.append(calc(a, b, x))
        x += dx
    return result_array

def task_b(a: float, b: float, values: list) -> list:
    result_array = []
    for item in values:
        result_array.append(calc(a, b, item))
    return result_array

def print_answer(task_name: str, result_array: list):
    print(f"Ответы к задаче {task_name}:")
    for element in result_array:
        print(f"{result_array.index(element) + 1}) {round(element, 3)}")

if __name__ == "__main__":
    result_array = task_a(4.1, 2.7, 1.2, 5.2, 0.5)
    print_answer("A", result_array)
    result_array = task_b(4.1, 2.7, [1.9, 2.15, 2.34, 2.73, 3.16])
    print_answer("B", result_array)
