fruits = ['Apple', 'Orange', 'Mango', 'Banana']
print(fruits)
print(type(fruits))

# Indexing
print(fruits[0])
print(fruits[2])
print(fruits[3])

# Slicing
print(fruits[1:3])
print(fruits[::-1])

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[1])
print(matrix[2])

# Mutability
fruits[1] = 'Papaya'
print(fruits)

# Lists Methods
frts = ['Apple', 'Banana', 'Mango']
frts.append('Mango')
print(frts)

frts.extend(['Mango', 'Orange'])
print(frts)

frts.insert(1, 'Papaya')
print(frts)

frts.remove('Banana')
print(frts)

removed_frts = frts.pop(1)
print(removed_frts)
print(frts)

frts.clear()
print(frts)

num = [3, 54, 67, 23, 7, 8]
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

newNum = sorted(num)
print(newNum)

num.reverse()
print(num)

org = [1, 2, 3]
duplicate = org.copy()
print(duplicate)
duplicate.append(4)
print(duplicate)


# Membership & Iteration
fruits = ['Apple', 'Banana', 'Mango']
print('Apple' in fruits)
print('Kiwi' not in fruits)
print('Kiwi' in fruits)

for i in fruits:
    print(i, end=' ')


# To-Do List app
todo_list = []
todo_list.append('Buy groceries')
todo_list.append('Complete python assignment')
todo_list.append('Attend Classes')

print('Your Tasks: ')
for i, task in enumerate(todo_list, start=1):
    print(f'{i}. {task}')

completed_task = 'Attend Classes'
if completed_task in todo_list:
    todo_list.remove(completed_task)
    print(f"'{completed_task}' is completed")

print('Remaining tasks: ', todo_list)


# Remove Duplicates
numbers = [1, 2, 3, 4, 4, 4, 5, 3, 3, 6]
uniq_num = []
for num in numbers:
    if num not in uniq_num:
        uniq_num.append(num)

print(uniq_num)