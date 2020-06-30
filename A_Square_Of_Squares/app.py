import math

def is_square(n):
    return True if (n>=0) and ((int(math.sqrt(int(n)))**2) == n) else False

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))