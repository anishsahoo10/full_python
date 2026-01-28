#experiment 1 : write a program defining datatypes and operators 
#datatypes
# Numeric Data Types
a = 10          # int
b = 3.5         # float
c = 2 + 3j      # complex

print("Numeric Data Types")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print()

# Text Data Type
text = "Hello Python"
print("Text Data Type")
print(text, type(text))
print()

# Boolean Data Type
x = True
y = False
print("Boolean Data Type")
print(x, type(x))
print(y, type(y))
print()

# Sequence Data Types
lst = [1, 2, 3]
tup = (4, 5, 6)
rng = range(1, 5)

print("Sequence Data Types")
print(lst, type(lst))
print(tup, type(tup))
print(list(rng), type(rng))
print()

# Set Data Type
st = {1, 2, 3}
print("Set Data Type")
print(st, type(st))
print()

# Dictionary Data Type
d = {"name": "Anish", "age": 20}
print("Dictionary Data Type")
print(d, type(d))
print()

# None Data Type
n = None
print("None Data Type")
print(n, type(n))
print()

# Binary Data Types
bt = b"ABC"
ba = bytearray(b"ABC")

print("Binary Data Types")
print(bt, type(bt))
print(ba, type(ba))
print()

# operators

a = 10
b = 5

# Arithmetic Operators
print("Arithmetic Operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print()

# Assignment Operators
print("Assignment Operators")
x = 10
x += 5
print(x)
x -= 3
print(x)
print()

# Comparison Operators
print("Comparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print()

# Logical Operators
print("Logical Operators")
print(True and False)
print(True or False)
print(not True)
print()

# Membership Operators
lst = [1, 2, 3]
print("Membership Operators")
print(2 in lst)
print(5 not in lst)
print()

# Bitwise Operators
p = 6
q = 3
print("Bitwise Operators")
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 1)
print(p >> 1)
