MAX = 5
print(f'Please enter {MAX} numbers to add')
sum = 0
count = 0
while count < MAX:
    sum += float(input('=> '))
    count += 1

print(f'The sum is {sum}')