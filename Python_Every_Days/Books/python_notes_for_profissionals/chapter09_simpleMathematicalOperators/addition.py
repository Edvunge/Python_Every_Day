a, b = 1, 2

# Using the "+" operator:
a + b

# Using the "in-place" "+=" operator to add and assign
a += b

import operator
operator.add(a, b)

a = operator.iadd(a, b)

print("first string " + " second string")
print([1, 2, 3] + [4, 5, 6])
