####################################################
## 1. Primitive Datatypes and Operators
####################################################

# You have numbers
print(3)

# Math is what you would expect
print(1+1)  # => 2
print(8-1)  # => 7
print(10*2) # => 20
print(35/5) # => 7.0

# Integer division rounds down for both positive and negative numbers
print(5 // 3)       # => 1
print(-5 // 3)      # => -2
print(5.0 // 3.0)   # => 1.0 # works on floats too
print(-5.0 // 3.0)  # => -2.0

# The result of division is always a float
print(10.0 / 3) # => 3.3333333333

# Modulo operation
print(7 % 3)

# i % j have same sign as j
print(-7 % 3) # => 2

# Explonention (x**y, x to the yth power)
print(2**3) # => 8

# Enforce precedence with parentheses
print(1 + 3 * 2) # => 7
print((1 + 3) * 2) # => 8

# Boolean values are primitives
print(True)   # => False
print(False)  # => True

# Boolean Operators
# Note "and" and "or" are case-sentive
print(True and False)  # False 
print(False or True)   # True

# True and False
print(True  + True)
print(True  *    8)
print(False -    5)

# Comparison operators look
print(0 == False)
print(2 > True)
print(2 == True)
print(-5 != False)

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)         # => False
bool("")        # => False
bool([])        # => False
bool({})        # => False
bool(())        # => False
bool(set())     # => False
bool(4)         # => True
bool(-6)        # => True

# and/or (&,|)
bool(0)             # => False
bool(2)             # => True
print(0 and 2)      # => 0
bool(-5)            # => True
bool(2)             # => True
print(-5 or 0)      # => -5

# Equality is == 
print(1 == 1) # => True
print(2 == 1) # => False

# Inequality is != 
print(1 != 1) # => False
print(2 != 1) # => True

# More Comparisons
print(1 < 10) # => True
print(1 > 10) # => False
print(2 <= 2) # => True
print(2 >= 2) # => False

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal
