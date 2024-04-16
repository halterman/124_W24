class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'