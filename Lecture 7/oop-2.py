# INHERITANCE

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

dog = Dog('Tommy')
dog.eat()
dog.sleep()
dog.bark()





# Multilevel Inheritance
class Grandfather:
    def house(self):
        print("Grandfather's house")

class Father(Grandfather):
    def business(self):
        print("Father's business")

class Son(Father):
    def car(self):
        print('Car of the son')

s = Son()
s.house()
s.business()
s.car()



# Multiple Inheritance
class Phone:
    def call(self):
        print('Calling...')

class Camera:
    def photo(self):
        print('Taking selfie')

class Smartphone(Phone, Camera):
    def internet(self):
        print('Internet is working')

sm = Smartphone()
sm.call()
sm.photo()
sm.internet()



# Hierarchical Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} started")


class Car(Vehicle):
    def wheels(self):
        print('Have 4 wheels')

class Bike(Vehicle):
    def wheels(self):
        print('Have 2 wheels')


c = Car('Audi')
b = Bike('BMW')

c.start()
c.wheels()

b.start()
b.wheels()



# super()
class Animal:
    def sound(self):
        print('Animal is making some sound')

class Dog(Animal):
    def sound(self):
        super().sound()
        print('Dog is barking')


d = Dog()
d.sound()



# Example I:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Person is: {self.name}')


class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
        print(f"Student has been created, Roll no.: {self.roll}")

s1 = Student('Kamran', 19, 101)


# Example II:
class A:
    def greet(self):
        print('Hello from A')

class B(A):
    def greet(self):
        print('Hello from B')

class C(A):
    def greet(self):
        print('Hello from C')

class D(B, C):
    pass

d = D()

d.greet()
print(D.mro())



# Example III:
class BankAcc:
    def __init__(self, balance):
        self.balance = balance

    def show_bal(self):
        print(f"Balance: {self.balance}")

class SavingsAcc(BankAcc):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest / 100
        self.balance += interest
        print(f"Interest added: {interest}")

    def show_balance(self):
        super().show_bal()
        print(f"Interest rate: {self.interest}%")

acc = SavingsAcc(1000, 10)
acc.add_interest()
acc.show_balance()



# Polymorphism
class Animal:
    def makeSound(self):
        print('Animal Sound')

class Dog(Animal):
    def makeSound(self):
        print("Dog: Bark")

class Cat(Animal):
    def makeSound(self):
        print("Cat: Meow")

class Cow(Animal):
    def makeSound(self):
        print("Cow: Moo")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.makeSound()


# Duck Typing
class Duck:
    def sound(self):
        print('Quack Quack!')

class Human:
    def sound(self):
        print('I can make sound like a Duck')

def makeSound(entity):
    entity.sound()

d = Duck()
h = Human()

makeSound(d)
makeSound(h)



# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def show(self):
        print(f"Point({self.x}, {self.y})")


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
p3.show()



class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c = 0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))




# Abstract
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rect(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)


c = Circle(6)
print(c.area())
print(c.perimeter())

r = Rect(4, 6)
print(r.area())
print(r.perimeter())


shapes = [Circle(3), Rect(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area()}")



# Magic Method
# 1. __str__ method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

s = Student('Ayush', 20)
print(s)


# # 2. __repr__ method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
            return f"Student('{self.name}', {self.age})"

s = Student('Ayush', 20)
print(s)


# 3. __len__ method
class Classroom:
    def __init__(self, students):
        self.students = students

    def __len__(self):
            return len(self.students)

s = Classroom(['Rahul', 'Kamran', 'Aman'])
print(len(s))



# 3. __eq__ method
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1 == p2)



# Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine starts with {self.horsepower} HP.")

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)    # Composition: Car HAS-A Engine

    def start_car(self):
        print(f"{self.brand} is starting...")
        self.engine.start()

c = Car('Honda', 150)
c.start_car()