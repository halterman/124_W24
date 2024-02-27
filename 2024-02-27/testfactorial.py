def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial2(n: int) -> int:
    return 0


# for i in range(10):
#     print(f'{i}! = {factorial(i):6}   ({factorial2(i):6})')

print(factorial(6))