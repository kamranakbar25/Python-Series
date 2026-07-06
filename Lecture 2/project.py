print('---- STUDENT UTILITY TOOL ----')
print()
print('1. Grade Calculator')
print('1. Multiplication Table')
print('1. Even/Odd Checker')
print()

while True:
    choice = int(input('Enter your choice: '))
    print()
    match choice:
        case 1:
            marks = int(input('Enter your marks: '))
            
            if marks < 0 or marks > 100:
                print('Invalid marks\n')
            elif marks >= 90:
                print('Grade: A+\n')
            elif marks >= 80:
                print('Grade: A\n')
            elif marks >= 70:
                print('Grade: B\n')
            elif marks >= 60:
                print('Grade: C\n')
            elif marks >= 40:
                print('Grade: D\n')
            else:
                print('Fail\n')
            
        case 2:
            num = int(input('Enter a number: '))
            for i in range(1, 11):
                print(f'{num} * {i} = {num * i}')
            print()
            
        case 3:
            num = int(input('Enter a number: '))
            if num % 2 == 0:
                print(f'{num} is an Even Number\n')
            else:
                print(f'{num} is an Odd Number\n')
        
        case _:
            print('Invalid choice, Please enter again:\n')