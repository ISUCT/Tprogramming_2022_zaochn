#x=1
#print(x)


def deistvie(x,xk):
    if x<=xk:
        for number in range(1,xk,1):
            print(number)

def deistvie2(xk,x):
     if x<=xk:
        for number in range(xk,1,-2):
            print(number)


if __name__ == "__main__":           
    xk=int(input())
    deistvie(1,xk)
    print("---------------------------")
    deistvie2(xk,1)

