class Counter:
    def __init__(self) -> None:
        self.data = 0
    def inc(self) -> None:
        print('Incrementing...')
        self.data += 1
    def get(self) -> int:
        return self.data

class LimitedCounter(Counter):
    def __init__(self, limit: int) -> None:
        super().__init__()
        self.limit = limit

    def inc(self) -> None:
        if self.get() != self.limit:
            super().inc()
        else:
            print('Counter has reached its limit')


def reveal_counter_value(ctr: Counter) -> int:
    return ctr.get()


if __name__ == '__main__':
    my_obj = Counter()
    print(reveal_counter_value(my_obj))
    # # This won't work because reveal_counter_value expects
    # # a Counter object
    # s = 'Hello'
    # print(reveal_counter_value(s))
    lc = LimitedCounter(5)
    print(reveal_counter_value(lc))
