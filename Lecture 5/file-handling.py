# File Handling

file1 = open("Lecture 5/sample.txt", "r")
print(file1)
file1.close()

file2 = open('Lecture 5/test.txt', 'w')
file2.write("This is a new file.")
file2.close

file3 = open('Lecture 5/test.txt', 'a')
file3.write('\nThis line is added')
file3.close()

# To get current working directory
import os
print(os.getcwd())


# read()
file = open('Lecture 5/sample.txt', 'r')
content = file.read()
print(content)
print(type(content))
file.close()

file = open('Lecture 5/sample.txt', 'r')
cntn = file.read(10)
print(cntn)
file.close()


# readline()
file = open('Lecture 5/sample.txt', 'r')
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print(line1.strip())
print(line2)
print(line3)
file.close()


# readlines()
file = open('Lecture 5/sample.txt', 'r')
lines = file.readlines()
print('Total lines:', len(lines))
print('First line:', lines[0].strip())
print('Last line:', lines[-1].strip())
file.close()


file = open('Lecture 5/sample.txt', 'r')
for line in file:
    print(line.strip())
file.close()



# Write Mode
file = open('Lecture 5/output.txt', 'w')
file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')
file.close()

# writelines()
lines = ['Apple\n', 'Banan\n', 'Cherry\n']
file = open('Lecture 5/fruits.txt', 'w')
file.writelines(lines)



# Log file
import datetime
def add_log(msg):
    file = open('Lecture 5/app_log.txt', 'a')
    time_now = datetime.datetime.now()
    file.write(f'[{time_now}] {msg}\n')
    file.close()

add_log("Application started")
add_log("User logged in")
add_log('File uploaded successfully')


# Saving user data
def user_data(name, age, city):
    file = open('Lecture 5/users.txt', 'a')
    file.write(f'{name}, {age}, {city}\n')
    file.close()

user_data('Kamran', 19, 'Delhi')
user_data('Rohan', 21, 'Mumbai')
user_data('Ayush', 20, 'Patna')


# Context Manager
with open('Lecture 5/sample.txt', 'r') as file:
    content = file.read()
    print(content)
print(file.closed)


