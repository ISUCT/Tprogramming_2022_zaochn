a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#заменил for k in b 
# if k in a
#c.append(k)
#print(c)
result = list(set(a) & set(b))
print(result)