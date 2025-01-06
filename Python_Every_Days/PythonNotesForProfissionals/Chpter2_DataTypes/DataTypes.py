# sets - They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('abracadabra')
print(a)

a.add('z')
print(a)

# Frozen Sets - They are immutable and new elements cannot added after its defined
b = frozenset('asdfagsa')
print(b)

cities = frozenset(["Frankfurt", "Basel", "Freiburg"])
print(cities)
frozenset({'Frankurt', 'Basel', 'Freiburg'})