def lt5(a: list) -> list:

    l = []
    for i in a:
        if isinstance(i, (int, float)):
            if i < 5.0:            
                l.append(i)

    return l


if __name__ == '__main__':

    print('empty')
    print(lt5([]))

    print('1-9')
    print(lt5([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print('5-9')
    print(lt5([5, 6, 7, 8, 9]))