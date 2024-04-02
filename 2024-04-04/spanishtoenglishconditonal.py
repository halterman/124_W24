def translate(word: str) -> str:
    result = '????'
    if word == 'uno':
        result = 'one'
    elif word == 'dos':
        result = 'two'
    elif word == 'tres':
        result = 'three'
    elif word == 'cuatro':
        result = 'four'
    elif word == 'cinco':
        result = 'five'
    elif word == 'seis':
        result = 'six'
    elif word == 'siete':
        result = 'seven'
    return result


if __name__ == '__main__':
    while True:
        word = input('Enter Spanish number: ')
        if word == '':
            break
        print(translate(word))
