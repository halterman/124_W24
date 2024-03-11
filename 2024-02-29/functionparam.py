from typing import Callable


Func = Callable[[float, float], float]

def multiply(x: float, y: float) -> float:
    """ Multiplies the parameters x and y """
    return x * y

def add(x: float, y: float) -> float:
    """ Multiplies the parameters x and y """
    return x + y

def add3(x: float, y: float, z: float) -> float:
    return x + y + z

def evaluate(f: Func, x: float, y: float) -> float:
    """ Calls the function f with parameters x 
        and y: f(x, y) """
    return f(x, y)


print(multiply(2, 3))
#print(multiply('2', '3'))
print(evaluate(multiply, 2, 3))
print(evaluate(add, 2, 3))
#print(evaluate(add3, 2, 3))
