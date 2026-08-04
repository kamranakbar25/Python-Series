try:
    result = 10/0
except ZeroDivisionError as e:
    print('Error occurred: ', e)
else:
    print('Success! Result: ', result)
finally:
    print('It will always execute')


try:
    num1 = int(input('Number: '))
    result = 10 / num1
except ZeroDivisionError as z:
    print('Error occurred: ', z)
except ValueError as v:
    print('Error occurred: ', v)
except Exception as e:
    print('Error occurred: ', e)


# raise
age = int(input('Age: '))
if age < 0:
    raise ValueError('Age cannot be negative')


# Types of errors:
# FileNotFoundError
# ZeroDivisionError
# ValueError
# IndexError
# KeyError
# TypeError
# NameError
# AttributeError
# ImportError


l = [1, 2, 3, 4]
try:
    print(l[5])
except IndexError as i:
    print('Error occurred: ', i)


# File + Exception 
def safe_read_file(fname):
    try:
        with open(fname, 'r') as file:
            content = file.read()
    except FileNotFoundError as f:
        print(f'{fname} doesn\'t exist')
        return None
    else:
        print('Program successfully executed without any error')
        return content
    finally:
        print('Read operation complete...')


data = safe_read_file('Lecture 5/sample.txt')
if data:
    print(data)