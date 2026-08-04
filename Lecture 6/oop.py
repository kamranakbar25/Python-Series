class Student:
    def study(self):
        print('I am studying')

s1 = Student()
s2 = Student()
s3 = Student()
s1.study()
print(id(s1))
print(id(s2))
print(id(s3))
print('s1 id: ', id(s1))



# Constructors
class Student:
    def __init__(self, name, roll=0, marks=0):
        self.name = name
        self.roll = roll
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")

s1 = Student('Rahul', 101, 85)
s2 = Student('Ayush', 102)
s3 = Student('Aman', 103, 90)

s1.display()
s2.display()
s3.display()



# Instance Variable
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student('Kamran', 85)
s2 = Student('Rahul', 75)

print(s1.name)
print(s2.name)
print(s1.marks)
print(s2.marks)

s1.name = 'Ayush'
print(s1.name)


# Class Variables
class Student:
    schoolname = 'ABC Public School'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student('Rahul', 101)
s2 = Student('Krish', 102)

print(s1.schoolname)
print(Student.schoolname)

Student.schoolname = 'XYZ Public School'
print(s1.schoolname)
print(s2.schoolname)



# Counter
class Student:
    total_student = 0
    def __init__(self, name):
        self.name = name
        Student.total_student += 1

s1 = Student('Krish')
s2 = Student('Ayush')
print(Student.total_student)


# @staticmethod
class Add:
    @staticmethod
    def add(a, b):
        return a + b

print(Add.add(5, 3))


# @classmethod
class Student:
    schoolname = 'Abc public school'

    @classmethod
    def changeschool(cls, newname):
        cls.schoolname = newname

print(Student.schoolname)
Student.changeschool('Xyz public school')
print(Student.schoolname)


# Encapsulation
class BankAcc:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

acc1 = BankAcc('Ravi', 50000)
print(acc1.balance)
acc1.balance = 0
print(acc1.balance)

class Student:
    def __init__(self, name):
        self.__name = name

s1 = Student('Rahul')
# print(s1.__name)
print(s1._Student__name)


# Getter & Setter method
class BankAcc:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance    # private

    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount < 0:
            print('Amount cannot be negative')
        else:
            self.__balance = amount
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} has been deposited, new balance: {self.__balance}')
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient balance')
        else:
            self.__balance -= amount
            print(f'{amount} has been withdrew, new balance: {self.__balance}')

acc1 = BankAcc('Kamran', 5000)
acc1.set_balance(10000)
acc1.deposite(2000)
acc1.withdraw(99)
# print(acc1.__balance)     # this will throw error