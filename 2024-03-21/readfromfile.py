def sum(a: list[float]) -> float:
    """ Computes and returns the sum of a list of 
        numbers. """
    s = 0
    for elem in a:
        s += elem
    return s


def average(a: list[float]) -> float:
    """ Computes and returns the average value
        of a list of numbers. """
    return sum(a)/len(a)

if __name__ == '__main__':
    # Reads in a set of numbers from a file and
    # prints some statistics about the numbers.
    
    filename = input('Please enter file name: ')
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(float(line))
    
    # Print the count
    print(f'Quantity: {len(data)}')
    
    # Print the sum
    print(f'Sum: {sum(data)}')
            
    # Print the average
    print(f'Average: {average(data)}')