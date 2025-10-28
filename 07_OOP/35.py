# ===== FILE 35: OOP - Inheritance and Advanced Concepts =====
# Topic: Class inheritance, method overriding, super()
# Concepts: Parent class, child class, inheritance, polymorphism, super()

# Example 1: Basic inheritance
class Animal:
    """Base class representing an animal"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
    def move(self):
        print(f"{self.name} is moving")

class Dog(Animal):
    """Dog class inherits from Animal"""
    
    def speak(self):  # Method overriding
        print(f"{self.name} barks: Woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    """Cat class inherits from Animal"""
    
    def speak(self):  # Method overriding
        print(f"{self.name} meows: Meow!")

# Create objects
dog = Dog("Buddy")
dog.speak()
dog.move()
dog.fetch()

cat = Cat("Whiskers")
cat.speak()
cat.move()

# ===== PRACTICE QUESTIONS =====

# Problem 1: Create Vehicle hierarchy
print("\n--- Problem 1: Vehicle inheritance ---")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc
    
    def rev(self):
        print("Vroom vroom!")

car = Car("Toyota", "Camry", 4)
car.start()
car.honk()

bike = Motorcycle("Harley", "Davidson", 1200)
bike.start()
bike.rev()

# Problem 2: Employee hierarchy with salary
print("\n--- Problem 2: Employee hierarchy ---")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def display(self):
        super().display()
        print(f"Manages team of {self.team_size} people")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def display(self):
        super().display()
        print(f"Programs in {self.language}")

mgr = Manager("Alice", 80000, 10)
mgr.display()

dev = Developer("Bob", 60000, "Python")
dev.display()

# Problem 3: Multiple inheritance
print("\n--- Problem 3: Multiple inheritance ---")
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Animal, Flyer, Swimmer):
    """Duck inherits from multiple classes"""
    def speak(self):
        print(f"{self.name} quacks: Quack!")

duck = Duck("Donald")
duck.speak()
duck.fly()
duck.swim()

# Problem 4: Abstract concept with private attributes
print("\n--- Problem 4: Private attributes ---")
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private attribute (name mangling)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("John", 1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")
# print(account.__balance)  # This would cause an error

# Problem 5: Property decorator
print("\n--- Problem 5: Property decorator ---")
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 30
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

# Problem 6: Class methods and static methods
print("\n--- Problem 6: Class and static methods ---")
class MathOperations:
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """Class method - can access class variables"""
        return cls.pi * radius ** 2
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance"""
        return a + b

print(f"Circle area: {MathOperations.circle_area(5):.2f}")
print(f"5 + 3 = {MathOperations.add(5, 3)}")

# CONCEPT SUMMARY:
# INHERITANCE:
# - Child class inherits attributes and methods from parent
# - Use super() to call parent class methods
# - Method overriding: Child class redefines parent's method
# - Multiple inheritance: Class inherits from multiple parents
#
# SPECIAL CONCEPTS:
# - Private attributes: __variable (name mangling)
# - Property decorator: @property for getters/setters
# - Class method: @classmethod (works with class, not instance)
# - Static method: @staticmethod (utility function)
#
# OOP PRINCIPLES:
# - Inheritance: Reuse code from parent classes
# - Polymorphism: Same method, different behavior
# - Encapsulation: Hide internal details
# - Abstraction: Simplify complex systems
