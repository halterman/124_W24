class Counter:
    def __init__(self) -> None:
        self.value = 0
    def inc(self) -> None:
        self.value += 1
    def get(self) -> int:
        return self.value

if __name__ == '__main__':
    my_obj = Counter()
    print(my_obj.get())
    my_obj.inc()
    my_obj.inc()
    print(my_obj.get())