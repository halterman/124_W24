# Function definition
def count(n: int):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

def double(n: int) -> int:
    return 2 * n

# Function invocation
count(5)
count(10)
count(20)
# count('15')
num = int(input('Please enter number to double: '))
print(f'Double {num} is {double(num)}')
count(double(3))
