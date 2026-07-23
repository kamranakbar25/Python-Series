# name = "Kamran"
# print(name)

# paragraph = """This is first line
# this is second line
# this is third line"""
# print(paragraph)
# print()
# sentence1 = 'This is Rohan\'s book'
# print(sentence1)

# print("Hello\nWorld")
# print("Hello\tWorld")
# print("C:\\Users\\Kamran")
# print("He said \"Hi\".")


# String Indexing
word = 'PYTHON'
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])

# print(word[-1])
# print(word[-2])
# print(word[-3])
# print(word[-4])
# print(word[-5])
# print(word[-6])


# Slicing
# word = 'PYTHON'
# print(word[0:3])
# print(word[2:5])
# print(word[:3])
# print(word[3:])
# print(word[:])
# print(word[1:100])


# # Step Slicing
# word = 'PYTHON'
# print(word[0:6:2])
# print(word[::2])
# print(word[::-1])


# String Immutability
# word = 'PYTHON'
# # word[0] = 'J'
# new_word = "J" + word[1:]
# print(new_word)


# Membership Operators in String
word = 'PYTHON'
# print('P' in word)
# print('Pyt' in word)
# print('PYT' in word)
# print('Z' not in word)


# String Methods
text = "   Hello World   "
# print(text)
# print(text.upper())
# print(text.lower())
# print(text.strip())
# print(text.title())
# print(text.replace("World", "Python"))
# print(text.split())

# name = 'kamran123'
# print(name.capitalize())
# print(name.startswith('ka'))
# print(name.endswith('mn'))
# print(name.count('a'))
# print(name.find('r'))
# print(name.isalpha())
# print(name.isdigit())
# print(name.isalnum())
# print("  ".isspace())


# String formatting
name = 'Kamran'
age = 19

print('My name is: ' + name + ' and I am ' + str(age) + ' years old')
print(f'My name is {name} and I am {age} years old.')


price = 49.6547
print(f'The price is {price:.2f}')


# Email Validation
email = 'kamran@gmail.com'
if '@' in email and '.' in email:
    print('Valid email')
else:
    print('Invalid email')


# Username generator
fname = 'Kamran'
lname = 'Akbar'
uname = (fname[:3] + lname[:3])
username = uname.lower()
print(username)


# Q1. user se input lena hai or uska pehla or aakhri character print krna hai.
# Q2. check karo ki string palindrome hai ya nhi
# madam --> madam
# Q3. ek string me total vowels count krna hai (a, e, i, o, u)
# Q4. user se fullname lo or use first name or last name me alag alag print kr do
# Q5. string ko reverse kro

word = input('Enter a word: ')
word = word.lower()
if word == word[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')