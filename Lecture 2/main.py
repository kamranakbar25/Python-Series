# Operators

# Arithmetic operators
a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)

print(a % 2)

# Assignment Operator
num = 10
print(num)
num += 10   # num += 10 --> num = num + 10
print(num)
num -= 10   # num = num - 10
print(num)
num *= 10
print(num)
num /= 10
print(num)
a //= 10
print(a)
b **= 2
print(b)


# Comparison Operator
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

age = 17
has_id = True
print(age == 18)


# Logical Operator
# and, or, not
print(age >= 18 and has_id == True)
print(age >= 18 or has_id == False)
print(not age >= 18)

username = 'admin'
password = 1234
print(username == 'admin' and password == 1234)

# Bitwise Operator
a = 5
b = 3
print(bin(b))

# AND --> &
# OR --> |
# XOR --> ^
# NOT --> ~
# Left Shift --> <<
# Right Shift --> >>

print('Bitwise AND: ', a & b)
print('Bitwise OR: ', a | b)
print('Bitwise XOR: ', a ^ b)
print('Bitwise NOT: ', ~a)
print('Left Shift: ', a << 1)
print('Right Shift: ', a >> 1)
print('Left Shift: ', a << 2)
print('Right Shift: ', a >> 2)


# Membership + Identity 
name = 'Kamran'
print("K" not in name)
print("k" not in name)
print("z" in name)

a = 10
b = 10
print(a is b)
print(a is not b)


# Operator Precedence
# + - * /

result = (10 + 5) * 2
print(result)



# If Statement
marks = int(input('Enter your marks: '))
if (marks >= 85):
    print('Grade: A')
elif (marks >= 60):
    print('Grade: B')
elif (marks >= 50):
    print('Grade: C')
elif (marks >= 40):
    print('Need Improvment')
else:
    print('Fail')


# Loops
for i in range(1, 11, 3):
    print(f'{i}')


num = int(input('Enter a number: '))
for i in range(1, 21):
    print(f'{num} * {i} = {num * i}')


# While Loop
count = 1
while count <= 5:
    print(count)
    count += 1    # count = count + 1


# Break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print()
# Continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


