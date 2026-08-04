def addnote():
    note = input('Write your note: ')
    try:
        with open('Lecture 5/notes.txt', 'a') as file:
            file.write(note + '\n')
        print('Note saved successfully')
    except Exception as e:
        print('Error: ', e)

def viewnote():
    try:
        with open('Lecture 5/notes.txt', 'r') as file:
            notes = file.readlines()
            if not notes:
                print('No notes found')
            else:
                for i, note in enumerate(notes, start=1):
                    print(f'{i}. {note.strip()}')
    except FileNotFoundError:
        print('Note not found')
    except Exception as e:
        print('Error: ', e)

def delete_all_notes():
    with open('Lecture 5/notes.txt', 'w') as file:
        pass
    print('Notes have been deleted successfully')

while True:
    print()
    print("1. Add Note  2. View Notes   3. Delete All   4. Exit")
    choice = input('Choice: ')
    if choice == "1":
        addnote()
    elif choice == '2':
        viewnote()
    elif choice == '3':
        delete_all_notes()
    elif choice == '4':
        print("Bye")
        break
    else:
        print('Invalid choice')