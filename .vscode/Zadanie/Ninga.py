def Ninjas_50(ningas):
    if 30<=ningas and ningas<=49:
        print ("Их Слишком Много")



def Ninjas_30(ningas):
    if 10<=ningas and ningas<=29:
        print ("Будет Не просто,но я с ними Разделаюсь")



def Ninjas_10(ningas):
    if 1<=ningas and ningas<=9:
        print ("Я Одолею этих ниндзя")

if __name__ == "__main__":
    ningas=int(input())
    Ninjas_50(ningas)
    Ninjas_30(ningas)
    Ninjas_10(ningas)