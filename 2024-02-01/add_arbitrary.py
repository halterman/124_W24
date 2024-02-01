print(f'Please enter non-negative numbers (-1 ends the list)')
sum = 0
looping = True
while looping:
    entry = float(input('=> '))
    if entry >= 0.0:
        sum += entry
    else:
        looping = False

print(f'The sum is {sum}')