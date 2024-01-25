english_word = input("Please enter number in English: ")
spanish_word = '?'
if english_word == 'one':
    spanish_word = 'uno'
else:
    if english_word == 'two':
        spanish_word = 'dos'
    else:
        if english_word == 'three':
            spanish_word = 'tres'
        else:
            if english_word == 'four':
                spanish_word = 'cuatro'
            else:
                if english_word == 'five':
                    spanish_word = 'cinco'

print(f'{english_word} --> {spanish_word}')