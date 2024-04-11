class Counter(object):
    def __init__(self) -> None:
        self.value = 0
    def inc(self) -> None:
        self.value += 1
    def get(self) -> int:
        return self.value

class LimitedCounter(Counter):
    def __init__(self, limit: int) -> None:
        super().__init__()
        self.limit = limit

    def inc(self) -> None:
        if self.value != self.limit:
            super().inc()
        else:
            print('Counter has reached its limit')


if __name__ == '__main__':
    my_obj = Counter()
    print(my_obj.get())
    my_obj.inc()
    my_obj.inc()
    print(my_obj.get())