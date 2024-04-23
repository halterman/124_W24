x = [6, 10, 34, 9, -1, 4]
try:
    i = int(input('Please enter a position: '))
    if 1 <= i <= len(x):
        print(x[i - 1])
    else:
        print('That value is out of range')
except ValueError:
    print('That\'s not really an integer number')