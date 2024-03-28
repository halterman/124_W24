sum = 0.0
NUMBER_OF_ENTRIES = 5
num_list = []
print(f'Please enter {NUMBER_OF_ENTRIES} numbers:')
for i in range(1, NUMBER_OF_ENTRIES + 1):
    num = float(input(f'Enter number {i}: '))
    num_list += [num]
    sum += num
print('Numbers entered:', end=' ')
for num in num_list:
    print(num, end=' ')
print()   # Print newline
print('Average:', sum/NUMBER_OF_ENTRIES)
