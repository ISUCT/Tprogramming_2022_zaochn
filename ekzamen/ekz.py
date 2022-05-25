def table(a):
    res = ""
    for i in range(1, a+1):
        for j in range(i, i*a+1, i):
            res += f"{j}\t"
        res += "\n"
    return res

if __name__ == "__main__":
  value = int(input())
  result = table(value)
  print(result)