class Widget:
    def __init__(self, v: int) -> None:
        self.value = v
        self.qual = 10

    def double(self):
        self.value *= 2

    def get(self) -> int:
        return self.value - self.qual




class Gadget(Widget):
    def __init__(self) -> None:
        super().__init__(100)

    def get(self) -> int:
        return super().get() + self.qual

w = Widget(20)
print(w.get())

g = Gadget()
print(g.get())

w = Widget(20)
for _ in range(5):
    w.double()
print(w.get())

w = Widget(20)
print(isinstance(w, Gadget))

g = Gadget()
print(isinstance(g, Widget))

