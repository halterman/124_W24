# Get the size of the table from the user
n = int(input())

# Print the column titles
for column in range(1, n + 1):
    print(f'{column:4}', end='')
print()
for column in range(1, n + 1):
    print('----', end='')
print()

# Print the table with the row titles
for row in range(1, n + 1):
    for column in range(1, n + 1):
        print(f'{row * column:4}', end='')
    print()