# f is a file object
filename = input('Enter file name')
f = open(filename)
# Read each line as text
for line in f:
    # Remove trailing newline character
    print(line.strip())
f.close() # Close the file
