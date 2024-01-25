# Get user input
num1 = int(input('Please enter an number: '))
num2 = int(input('Please enter another number: '))

if num2 != 0:
    quot = num1 // num2                 # Compute the quotient
    print(f'{num1} // {num2} = {quot}') # Print the result
else:
    print('Cannot divide by zero')

print('Program complete')