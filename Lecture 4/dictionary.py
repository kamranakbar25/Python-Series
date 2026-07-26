# student = {'name': 'Kamran', 'age': 19, 'marks': 75, 'city': 'Delhi'}
# print(student['name'])
# print(student['age'])
# print(student['marks'])
# print(student['city'])

# # data = {[1, 2]: 'value'}
# # print(data)     # TypeError: unhashable type: 'list'


# # method 1
# student1 = {'name': 'Kamran', 'branch': 'CSE'}

# # method 2
# student2 = dict(name = 'Rohan', branch = 'CSE')

# # method 3 --> Empty dictionary
# empty = {}
# empty['name'] = 'Karan'
# empty['branch'] = 'ECE'

# print(empty)


# # get() --> method
# student = {'name': 'Kamran', 'age': 19}
# print(student.get('branch'))
# print(student.get('name'))
# print(student.get('marks', 0))


# # update() --> method
# student.update({'age': 22, 'city': 'Delhi'})
# print(student)


# # pop() and popitem()
# remove = student.pop('age')
# print(remove)
# print(student)

# last = student.popitem()
# print(last)
# print(student)


# # clear()
# student = {'name': 'Kamran', 'age': 22, 'city': 'Delhi'}
# student.clear()
# print(student)


# # keys(), values(), items()
# student = {'name': 'Kamran', 'age': 22, 'city': 'Delhi'}
# print(student.keys())
# print(student.values())
# print(student.items())


# student = {'name': 'Kamran', 'age': 19, 'city': 'Delhi'}

# for key in student:
#     print(key)

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(f'{key}: {value}')

# for key in student:
#     print(key, student[key])

# for key, value in student.items():
#     print(key, value)


# Nested Dictionaries
# students = {
#     'student1': {
#         'name': "Kamran",
#         'age': 19,
#         'marks': 89
#     },
#     'student2': {
#         'name': "Rohan",
#         'age': 21,
#         'marks': 90
#     }
# }

# print(students['student1'])
# print(students['student1']['name'])
# print(students['student2']['marks'])


# for stdId, details in students.items():
#     print(f'\n{stdId}:')
#     for key, value in details.items():
#         print(f' {key}: {value}')


# # Dictionary Comprehension

# # Normal Way
# sq = {}
# for i in range(1, 11):
#     sq[i] = i * i
# print(sq)

# # Dictionary Comprehension Way
# sqrs = {i: i * i for i in range(1, 6)}
# print(sqrs)


# numbers = {1, 2, 3, 4, 5, 6, 7, 8}
# evensq = {n: n*n for n in numbers if n % 2 == 0}
# print(evensq)


# # Membership
# student = {'name': 'Rohan', 'age': 21}
# print('name' in student)
# print('Rohan' in student)
# print('Rohan' in student.values())


# Contact list
contacts = {
    'Rohan': '9746548520',
    'Priya': '9563214874',
    'Aman': '9248756315'
}

name = input('Enter name of the person: ')
if name in contacts:
    print(f'{name}\'s phone number: {contacts[name]}')
else:
    print('Invalid name.')


# Word frequency counter
sentence = "Lorem ipsum dolor sit amet, Lorem consectetur adipiscing elit."
words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)