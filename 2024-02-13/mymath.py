from math import isclose

def square_root(x: float) -> float:
    r = 1     # Set the provisional root to 1
    while not isclose(r*r, x):
        #print(f'The provisional root is {r}')
        r = (r + x/r) / 2
    return r

def cube_root(x: float) -> float:
    return 0.0