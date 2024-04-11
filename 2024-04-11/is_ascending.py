from random import randrange
from stopwatch import Stopwatch


def is_ascending_1(seq: list[int]) -> bool:
    n = len(seq)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                return False
    return True


def is_ascending_2(seq: list[int]) -> bool:
    n = len(seq)
    for i in range(1, n):
        if seq[i - 1] > seq[i]:
            return False
    return True


if __name__ == '__main__':
    LIST_LENGTH = 50_000
    # xs = [randrange(500) for x in range(LIST_LENGTH)]
    xs = list(range(10, LIST_LENGTH + 1))
    timer = Stopwatch()
    timer.start()
    ia = is_ascending_1(xs)
    timer.stop()
    print(timer.elapsed())

    timer.reset()

    timer.start()
    ia = is_ascending_2(xs)
    timer.stop()
    print(timer.elapsed())