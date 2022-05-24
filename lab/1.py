import math;

def kghjy (a: float, b: float,x: float)-> float:

    chislitel = math.acos((x**2)-(b**2))

    znamenatel = math.asin((x**2)-(a**2))
# math.acos - функция вычисл. аркос
# получаем у
    y=chislitel/znamenatel;

    return y;
if __name__ =="main":
    print(kghjy(0.05, 0.06, 0.15));

    hhh=kghjy(0.05, 0.06, 0.26 );
    print(hhh)

    
if __name__ == "main":
   print(hhh(0.05, 0.06, 0.15)); 