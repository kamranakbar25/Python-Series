# sets = {'Apple', 'Banana', 'Apple', 'Mango'}
# print(sets)

# empty = {}
# print(type(empty))  # <class 'dict'>

# empty_set = set()
# print(type(empty_set))

# Methods
# fruits = {'Apple', 'Banana'}
# fruits.add('Mango')
# print(fruits)

# fruits.update(['Kiwi', 'Orange', 'Papaya'])
# print(fruits)

# fruits.remove('Kiwi')
# print(fruits)

# fruits.discard('Strawberry')
# print(fruits)

# Set Operations
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a & b)

# print(a.difference(b))
# print(a - b)

# print(a.symmetric_difference(b))
# print(a ^ b)


# Subset and Superset
num1 = {1, 2}
num2 = {1, 2, 3, 4}
print(num1.issubset(num2))
print(num2.issuperset(num1))
print(num1.isdisjoint({5, 6}))


# Frozenset
fs = frozenset([1, 2, 3])
print(fs)


first = {'Amit', 'Priya', 'Karan', 'Ayush'}
second = {'Rohan', 'Karan', 'Priya', 'Vikas'}

commonfrnd = first.intersection(second)
print(commonfrnd)