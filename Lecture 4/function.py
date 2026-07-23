# Function

def greet(name):
    print(f'Hello, {name}')

greet('Kamran')
greet('Rahul')


def sum(a, b):
    print(a + b)

def sum2(a, b):
    return a+b

result1 = sum(5, 7)
print(result1)

result2 = sum2(5, 7)
print(result2)

def checkNumber(n):
    if n>0:
        return 'Positive'
    return 'Negative'
    print('This line will not execute.')

print(checkNumber(-12))

def greet(name, greet = 'Hello'):
    print(f'{greet}, {name}')

greet('Rohan', 'Good morning')


def stu_info(name, age, city):
    print(f'{name}, {age} years old, from {city}')

stu_info('Rohan', 21, 'Delhi')

stu_info(age = 21, city='Delhi', name='Kamran')
print()

# *args
def addAll(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(addAll(10))
print(addAll(1, 2, 3))
print(addAll(1, 2, 3, 4, 5, 6))


# **kwargs
def stu_profile(**details):
    for key, value in details.items():
        print(f'{key}: {value}')
stu_profile(name='Kamran', age= 19, city='Delhi')
print()
stu_profile(name='Kamran', age= 19, branch='CSE', sem='3rd')

def order(customer_name, *items, **extra_info):
    print(f'Customer: {customer_name}')
    print(f'Item ordered: {items}')
    print(f'Extra Info: {extra_info}')

# order('Kamran', 'Pizza', 'Coke', 'Biryani', table_no=1, is_delivery=False)

num = 10    # --> Global Variable

def showNumber():
    num2 = 5    # --> Local Variable

    print(num2)

showNumber()
print(num)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# Lambda Function
def sq(x):
    return x * x
print(sq(5))

sq_lambda = lambda x: x*x
print(sq_lambda(5))


students = [('Rohan', 89), ('Aman', 95), ('Kamran', 80), ('Anshul', 60)]
sortedStu = sorted(students, key=lambda student: student[0])
print(sortedStu)