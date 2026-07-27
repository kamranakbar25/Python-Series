# Student Result Management System

student_data = {}

def add_student(name, math, science, english):
    subjects = {'Math': math, 'Science': science, 'English': english}
    total = sum(subjects.values())
    average = total/len(subjects)

    student_data[name] = {
        'subjects': subjects,
        'total': total,
        'average': round(average, 2)
    }
    print(f'Record have been added for {name}')


def show_result(name):
    if name not in student_data:
        print('Invalid name')
        return

    data = student_data[name]
    print(f'Result of {name}')

    for subject, mark in data['subjects'].items():
        print(f'{subject}: {mark}')
    print(f'Total: {data['total']}')
    print(f'Average: {data['average']}')


def class_avg():
    if not student_data:
        print('No student marks has been added yet... Please try again later')
        return
    
    all_avg = [data['average'] for data in student_data.values()]
    overall_avg = sum(all_avg) / len(all_avg)
    print(f"\nClass's overall average: {round(overall_avg, 2)}")


def topper():
    if not student_data:
        print('No student marks has been added yet... Please try again later')
        return

    topper_name = None
    highest_average = 0

    for name, data in student_data.items():
        if data['average'] > highest_average:
            highest_average = data['average']
            topper_name = name

    print(f"\nTopper of the class: {topper_name} with average of: {highest_average}")


add_student('Rohan', 89, 92, 85)
add_student('Rohit', 95, 89, 75)
add_student('Vikas', 70, 80, 90)

show_result("Rohan")
print()
show_result("Vikas")
print()
show_result("Rohit")


class_avg()

topper()