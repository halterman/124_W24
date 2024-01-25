english_word = input("Please enter number in English: ")
spanish_word = '?'
match english_word:
    case 'one':
        spanish_word = 'uno'
    case 'two':
        spanish_word = 'dos'
    case 'three':
        spanish_word = 'tres'
    case 'four':
        spanish_word = 'cuatro'
    case 'five':
        spanish_word = 'cinco'
    case 'six':
        spanish_word = 'seis'
    case 'seven':
        spanish_word = 'siete'

print(f'{english_word} --> {spanish_word}')