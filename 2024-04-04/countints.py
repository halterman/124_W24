element_count = {}    # Begin with an empty dictionart

# Make an arbitrary list containing integers
a = [1, -4, 22, 10, 3, 21, 10, 18, -4, 3, 11, 10, 10, 3, 21, 10]

# Count the elements
for elem in a:
    if elem in element_count:
        element_count[elem] += 1  # Found another one
    else:
        element_count[elem] = 1   # Found one I have not seen yet

# Report the counts of the elements
for int_element, count in element_count.items():
    print(f'Number {int_element} appears in the list {count} times')
