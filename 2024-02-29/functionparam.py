
def multiply(x, y):
    """ Multiplies the parameters x and y """
    return x * y

def add(x, y):
    """ Multiplies the parameters x and y """
    return x + y

def evaluate(f, x, y):
    """ Calls the function f with parameters x 
        and y: f(x, y) """
    return f(x, y)


print(multiply(2, 3))
# print(multiply('2', '3'))
print(evaluate(multiply, 2, 3))
print(evaluate(add, 2, 3))