from typing import Generator, Any

def gen1() -> Generator[Any, Any, Any]:
    yield 5
    yield 10
    yield 50

if __name__ == '__main__':
    print(gen1())