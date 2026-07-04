# Project - Smart menu based profile generator

print("Welcome to Smart Profile Generator")


name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter your city name: ')
clg = input('Enter your college name: ')
course = input('Enter your course: ')
skill = input('Enter one skill you are learning: ')
goal = input('Enter your goal: ')

while True:
    print()
    print("Choose output type: ")
    print("1. Student Profile")
    print("2. LinkedIn Bio")
    print("3. Short Introduction")
    print("4. Learning Card")

    choice = int(input('Enter your choice: '))

    print()


    match choice:
        case 1:
            print('---- Student Profile ----')
            print(f'Name: {name}')
            print(f'Age: {age}')
            print(f'City: {city}')
            print(f'College: {clg}')
            print(f'Course: {course}')
            print(f'Currently Learning: {skill}')
            print(f'Goal: {goal}')

        case 2:
            print('---- LinkedIn Bio ----')
            print(f'I am {name}, a {age}-year old {course} student from {city}.')
            print(f'I study at {clg}.')
            print(f'Currently I am learning {skill}.')
            print(f'My goal is to become {goal}')

        case 3:
            print('---- Introduction ----')
            print(f'Hello, my name is {name}.')
            print(f'I am from {city}.')
            print(f'I am studying {course} at {clg}.')
            print(f'Currently I am learning {skill}.')

        case 4:
            print('---- Learning Card ----')
            print(f'Student: {name}')
            print(f'Skill Focus: {skill}')
            print(f'Goal: {goal}')
            print(f'Student: {name}')
            print(f'Message: Keep learning keep building.')
        
        case _:
            print('Invalid choice, Please enter again:')