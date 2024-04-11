from random import randrange
from time import perf_counter_ns


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
    start = perf_counter_ns()
    ia = is_ascending_1(xs)
    stop = perf_counter_ns()
    print((stop - start)/1e9)
    start = perf_counter_ns()
    ia = is_ascending_2(xs)
    stop = perf_counter_ns()
    print((stop - start)/1e9)