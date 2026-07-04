print("Hello World\n")
print('I am learning python')
print('I\'m Kamran')
print(5)
print(3.14)


name = "Kamran"
print(name)
age = 19
print(age)
pi = 3.14
isHuman = True
print(pi)
print(isHuman)


print('name: ', type(name))
print('age: ', type(age))
print('pi', type(pi))
print('boolean: ', type(isHuman))


# &*$@name = ''

# myname
# MYNAME



# single line comment

'''
This 
is 
multi
line
comment
'''

a= 4 
b = 7
# this program is adding a and b
print(a + b)


# Input

my_name = input('Enter your name: ')
print('Your name is: ', my_name)
my_age = input('Enter your age: ')
print('Your age is: ', my_age)
print(type(my_age))


# Type Casting

my_age = int(input('Enter your age: '))
print(my_age)
print(type(my_age))



# Operators
a = 10
b = 2 
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b) # float
print("Floor Division: ", a // b) # integer
print('Remainder: ', a % b) # remainder
print('Power: ', a ** b) # power

# practice - simple bill calculator
product = input('Enter product name: ')
price = int(input('Enter price: '))
quantity = int(input('Enter quantity: '))

total = price * quantity

print('Product: ', product)
# print('Total quantity: ', quantity, 'Total Bill: ', total)
print(f'Total Quantity: {quantity}, Total Bill: {total}') # f-string method


# match case

while True:
    choice = int(input('Enter your choice (1-3): '))

    match choice:
        case 1:
            print('you selected 1')
        case 2:
            print('you selected 2')
        case 3:
            print('you selected 3')
        case _:
            print("Invalid choice")
