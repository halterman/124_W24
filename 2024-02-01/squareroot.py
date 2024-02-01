from math import isclose, sqrt

# Get input from user
i = float(input('Please enter number: '))

r = 1     # Set the provisional root to 1

while not isclose(r*r, i):
    print(f'The provisional root is {r}')
    r = (r + i/r) / 2

print(f'The square root of {i} is {r} (or {sqrt(i)}).')