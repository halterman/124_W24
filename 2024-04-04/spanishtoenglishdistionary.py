def translate(word: str) -> str:
    trans = {'uno':'one',
             'dos':'two',
             'tres':'three',
             'cuatro':'four',
             'cinco':'five',
             'seis':'six',
             'siete':'seven'}
    if word in trans:
        return trans[word]
    else:
        return '????'


while True:
    word = input('Enter Spanish number: ')
    if word == '':
        break
    print(translate(word))
