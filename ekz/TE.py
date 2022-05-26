def deistvie(x,xk):
    res = ""
    for number in range(x,xk+1,1):
        res += f"{number}\n"
    return res

def deistvie2(xk,x):
     if x<=xk:
        for number in range(xk,1,-2):
            print(number)

def exam(x, xk):
    res = deistvie(1,xk)
    print(res)
    deistvie2(xk,1)

if __name__ == "__main__":           
    xk=int(input())
    print("!!!!!!!!!!!!!!!!")
    exam(1, xk)

