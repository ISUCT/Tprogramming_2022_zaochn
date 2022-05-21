a = 5 
A = 6
print(a, A)
b = 5.5
c = a + b
print(a,b,c)
a = True
b = False
c = a | b
print(a,b,c)
str_sample = 'Пример с кавычками внутри '
multiline = '''Пример
Текста расположенного
на нескольких строках'''
print(str_sample)
print(multiline)
snake_case = "Python \r\n Newline"
print(snake_case)

a = 5
print(a)
ab = "Some string"
print(ab)

a = 4 + 8
print(a)

af = 5 / 2
print(af)

a = 5 // 2
print(a)

a = 5 ** 2
print(a)

a = 5 % 2
print(a)

i = 1
print(f"i={i} <- formatted string")

i = i + 1
print(f"i={i}")

i += 1 # пример операции с присвоением
print(f"i={i}") # для комментирования ctl /

a = 5
b = 7

print(f"a={a:0b}, b={b:0b} -> {a & b}")