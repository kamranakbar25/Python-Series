coordinates = (28.6367, 77.7634)
print(coordinates)
print(type(coordinates))

t1 = (5,)
print(type(t1))

# Packing
person = ('Kamran', 19, 'Delhi')

# Unpacking
name, age, city = person
print(name)
print(age)
print(city)

first, *rest = person
print(first)
print(rest)

# Indexing and Slicing
print(person[0])
print(person[-1])
print(person[1:3])

data = ('Kamran', [90, 80, 70])
data[1].append(60)
print(data)

# Methods
num = (1, 2, 3, 2, 4, 3, 2)
print(num.count(2))
print(num.count(3))

print(num.index(4))
print(num.index(3))

stu_rec = ('Rohan', 21, 'CSE', 8.0)
name, age, branch, cgpa = stu_rec
print(f'{name} is {age} yrs old, studying {branch} with gpa of {cgpa}')


# Return Sum and product of two numbers in tuple form
def cal(a, b):
    return a + b, a * b

result = cal(5, 3)
print(result)
print(type(result))

sumval, proval = cal(5, 3)
print(sumval, proval)