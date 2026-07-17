# Sum of digits of a number
n = int(input("Enter a number: "))
sod = 0
while n > 0:
    digit = n % 10
    sod += digit
    n //= 10

print(sod)


# Count the number of digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1

print('Number of digits: ', count)


# Reverse a number
rNum = int(input("Enter a number: "))
rev = 0
while rNum > 0:
    digit = rNum % 10
    rev = rev * 10 + digit
    rNum //= 10

print("Rev number: ", rev)


# Palindrome Number check
pNum = int(input("Enter a number: "))
oNum = pNum
revNum = 0
while pNum > 0:
    digit = pNum % 10
    revNum = revNum * 10 + digit
    pNum //= 10
if oNum == revNum:
    print(oNum, 'is a Palindrome number')
else:
    print(oNum, 'is not a Palindrome number')



# Prime number check
primeNum = int(input('Enter a number: '))
isPrime = True
if primeNum <= 1:
    isPrime = False
else:
    for i in range(2, primeNum):
        if primeNum % i == 0:
            isPrime = False
            break
if isPrime:
    print(primeNum, 'is a prime number')
else:
    print(primeNum, 'is not a prime number')


# Armstrong number check
aNum = int(input('Enter a number: '))
originalNumber = aNum
digitCount = len(str(aNum))
sum_of_power = 0
temp = aNum

while temp > 0:
    digit = temp % 10
    sum_of_power = sum_of_power + digit ** digitCount
    temp //= 10
if sum_of_power == originalNumber:
    print(originalNumber, 'is an Armstrong number.')
else:
    print(originalNumber, 'is not an Armstrong number.')

# Square Pattern Printing
sq = 4
for row in range(sq):
    for col in range(sq):
        print(col, end=' ')
    print()


# Triangle Pattern Printing
# * Pattern
for i in range(1, sq + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

# Number pattern
for i in range(1, sq + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


# FizzBuzz Problem
fbNum = int(input('Enter a number: '))
for number in range(1, fbNum + 1):
    if fbNum % 15 == 0:
        print('FizzBuzz')
    elif fbNum % 3 == 0:
        print('Fizz')
    elif fbNum % 5 == 0:
        print('Buzz')
    else:
        print(fbNum)