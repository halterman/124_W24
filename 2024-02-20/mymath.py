from math import isclose

def square_root(x: float) -> float:
    r = 1     # Set the provisional root to 1
    while not isclose(r*r, x):
        #print(f'The provisional root is {r}')
        r = (r + x/r) / 2
    return r

def is_prime(n: int) -> bool:
    """ Determines if an integer is prime.
        The only factors a prime number has is 1 and
        itself. """
    for potential_factor in range(2, n):
        if n % potential_factor == 0:
            return False
    return True
    
