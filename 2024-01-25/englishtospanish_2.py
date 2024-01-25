english_word = input("Please enter number in English: ")
spanish_word = '?'
if english_word == 'one':
    spanish_word = 'uno'
elif english_word == 'two':
    spanish_word = 'dos'
elif english_word == 'three':
    spanish_word = 'tres'
elif english_word == 'four':
    spanish_word = 'cuatro'
elif english_word == 'five':
    spanish_word = 'cinco'
elif english_word == 'six':
    spanish_word = 'seis'

print(f'{english_word} --> {spanish_word}')