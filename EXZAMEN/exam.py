def revers_word(s: str) -> str:
    l = s.split(' ')
    l.reverse()
    return ' '.join(l)


if __name__ == '__main__':

    print('0 words')
    print(revers_word(''))

    print('1 words')
    print(revers_word('one'))

    print('5 words')
    print(revers_word('one two tree four five'))