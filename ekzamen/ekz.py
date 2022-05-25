def table(a):
  for i in range(1, a+1):
    for j in range(i, i*a+1, i):
      print(j, end='\t')
print()

value = int(input())
table(value)