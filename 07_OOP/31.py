# ===== FILE 31: Object-Oriented Programming - Classes and Objects =====
# Topic: Creating classes with attributes and methods
# Concepts: class, __init__(), self, methods, objects, instance variables

# ORIGINAL CODE - Student class with average calculation

class Student:
    """Class to represent a student with name and marks"""
    
    def __init__(self, name, marks):
        """Constructor - initialize student with name and marks"""
        self.name = name      # Instance variable
        self.marks = marks    # List of marks
    
    def avrage(self):
        """Calculate and print average of marks"""
        avg = 0
        for val in self.marks:
            avg += val
        avrag = avg / 3
        print("Hi ", self.name, "Your avg marks is : ", avrag)

# Create student object and calculate average
s1 = Student("Ritesh", [60, 50, 80])
s1.avrage()  # Output: Hi Ritesh Your avg marks is: 63.33...

# ===== PRACTICE QUESTIONS =====

# Problem 1: Add method to check if student passed (average >= 40)
print("\n--- Problem 1: Check pass/fail ---")
class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def is_passed(self):
        avg = self.average()
        if avg >= 40:
            print(f"{self.name} PASSED with average {avg:.2f}")
        else:
            print(f"{self.name} FAILED with average {avg:.2f}")

s2 = Student2("Alice", [45, 50, 55])
s2.is_passed()

# Problem 2: Create a Book class
print("\n--- Problem 2: Book class ---")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display(self):
        print(f"'{self.title}' by {self.author} ({self.pages} pages)")

book1 = Book("Python Programming", "John Doe", 500)
book1.display()

# Problem 3: Create a Car class with methods
print("\n--- Problem 3: Car class ---")
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, km):
        self.mileage += km
        print(f"{self.brand} {self.model} drove {km} km")
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km")

car1 = Car("Toyota", "Camry", 2020)
car1.drive(100)
car1.drive(50)
car1.display_info()

# Problem 4: Create a Rectangle class
print("\n--- Problem 4: Rectangle class ---")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return self.length == self.width

rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square? {rect.is_square()}")

# Problem 5: Create Employee class with salary calculation
print("\n--- Problem 5: Employee class ---")
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise of ${amount}")
    
    def annual_salary(self):
        return self.salary * 12
    
    def display(self):
        print(f"{self.name} - {self.position}: ${self.salary}/month")

emp1 = Employee("Bob", 5000, "Developer")
emp1.display()
emp1.give_raise(500)
print(f"Annual salary: ${emp1.annual_salary()}")

# Problem 6: Create BankAccount class
print("\n--- Problem 6: BankAccount class ---")
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

# CONCEPT SUMMARY:
# - class: Blueprint for creating objects
# - __init__(): Constructor method (runs when object is created)
# - self: Refers to the current object instance
# - Instance variables: Unique to each object (self.variable)
# - Methods: Functions defined inside a class
# - Object: Instance of a class
# - Encapsulation: Data and methods bundled together