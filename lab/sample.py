def ninja_work(ninja):
    if ninja < 10 :
        print ("Я одолею этих ниндзя!")  
    if ninja < 30 :
        print ("Будет непросто, но я с ними разделаюсь")
    else:
        print("Их слишком много") 

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
    ninja_work(15)