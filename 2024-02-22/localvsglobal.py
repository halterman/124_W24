x = 2

def func1() -> None:
    y = 5
    print(f'x = {x}, y = {y}')


def func2() -> None:
    z = 3
    print(f'x = {x}, z = {z}')

print(f'x = {x}')
func1()
func2()
print(f'x = {x}')