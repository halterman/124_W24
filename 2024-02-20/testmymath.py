# Test the functions in the mymath module.
import mymath

print(mymath.square_root(100))

for i in range(2, 21):
    if mymath.is_prime(i):
        print(i)

print(mymath.is_prime(2))
print(mymath.is_prime(3))
print(mymath.is_prime(4))