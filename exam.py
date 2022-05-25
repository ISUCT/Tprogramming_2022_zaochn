def table(a1:int, an:int, b1:int, bn:int) -> int:
    if a1 >= an:
        return 0
    if b1 >= bn:
        return 0
    for ai in (1, *range(a1, an)):
        for bi in (1, *range(b1, bn)):
            print(ai*bi, end='\t')
        print()
    
    return  (an-a1) * (bn-b1)


if __name__ == '__main__':

    print('1-9x1-9')
    table(1, 10, 1, 10)

    print('5x6')
    table(5, 6, 6, 7)

    print('3-6x7-9')
    table(3, 7, 7, 10)