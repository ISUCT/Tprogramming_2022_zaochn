def say_hello():
    print("Hello")
    print("more actions in function....")



print("Functions...")
say_hello()
print("-------")
say_hello()
print("end")

def summ(a, b, d = 0):
    c = a + b + d
    return c

summ(4, 6)
c = 5
b = 9
res = summ(c, b)
print(f"b after function = {b}")
print(f"result = {res}")

res = summ(c, b, 15)
print(f"result = {res}")

res = summ(b = 5, a = 3, d = 20)
print(f"result = {res}")

a = str(3) + "_some"
print(a)
