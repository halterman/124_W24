from typing import Generator, Any

def gen2() -> Generator[Any, Any, Any]:
    yield 5
    yield 'Bubba'
    return 99
    yield 3.14159

def gen3(n: int) -> Generator[Any, Any, Any]:
    for i in range(n):
        yield i

if __name__ == '__main__':
    for i in gen2():
        print(i)

    print('-----------------------')

    for i in gen3(5):
        print(i)