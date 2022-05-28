def summ(a:int=2, b:int=2) -> int:

    return a+b

# a и b заданы заранее и равны по умолчанию 2
# Функция возвращает их сумму

if __name__ == '__main__':

    print('empty args')
    print(summ())

    print('one args')
    print(summ(10))

    print('two args')
    print(summ(3, 3))