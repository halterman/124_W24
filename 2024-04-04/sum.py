def sum(m: int, n: int) -> int:
    return m + n


def sum1(m: int, n: int=0, p: int=0) -> int:
    return m + n + p


def sum2(m: int, n: int=0, p: int=0, q: int=0, r: int=0) -> int:
    return m + n + p + q + r

def sum3(*args: int) -> int:
    s = 0
    for elem in args:
        s += elem
    return s


if __name__ == '__main__':
    print(sum(3, 6))