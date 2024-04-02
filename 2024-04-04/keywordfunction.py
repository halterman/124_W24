def f(a, b, c):
    return 2*a*a + 3*b + c

def f2(**args):
    a = args['a']
    b = args['b']
    c = args['c']
    return 2*a*a + 3*b + c


if __name__ == '__main__':
    x = f(2, 3, 8)
    y = f(b=3, a=2,c=8)
    print(x, y)

    print('------------------')

    #x = f2(2, 3, 8)
    y = f2(b=3, a=2,c=8)
    print(x, y)