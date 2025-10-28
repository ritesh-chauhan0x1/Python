# ===== FILE 33: OOP - Operator Overloading (Polymorphism) =====
# Topic: Dunder methods and operator overloading
# Concepts: __add__(), __init__(), magic methods, operator overloading

# ORIGINAL CODE - Complex number addition using operator overloading

class Complex:
    """Class to represent complex numbers and perform operations"""
    
    def __init__(self, real, imag):
        """Initialize complex number with real and imaginary parts"""
        self.real = real
        self.imag = imag
    
    def shownumber(self):
        """Display the complex number"""
        print(self.real, "i +", self.imag, "j")
    
    def __add__(self, num2):
        """Override + operator to add two complex numbers"""
        newr = self.real + num2.real
        newi = self.imag + num2.imag
        return Complex(newr, newi)

# Create and add complex numbers
num1 = Complex(2, 3)
num1.shownumber()  # 2 i + 3 j

num2 = Complex(3, 4)
num2.shownumber()  # 3 i + 4 j

num3 = num1 + num2  # Uses __add__() method
num3.shownumber()   # 5 i + 7 j

# ===== PRACTICE QUESTIONS =====

# Problem 1: Add subtraction to Complex class
print("\n--- Problem 1: Complex number subtraction ---")
class Complex2:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex2(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Override - operator"""
        return Complex2(self.real - other.real, self.imag - other.imag)
    
    def __str__(self):
        """Override str() to display complex number"""
        return f"{self.real} + {self.imag}i"

c1 = Complex2(5, 3)
c2 = Complex2(2, 1)
c3 = c1 - c2
print(f"{c1} - {c2} = {c3}")

# Problem 2: Vector class with addition
print("\n--- Problem 2: Vector addition ---")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

# Problem 3: Override comparison operators
print("\n--- Problem 3: Compare objects ---")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Override == operator"""
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        """Override > operator (compare distances from origin)"""
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 1)
print(f"{p1} == {p2}: {p1 == p2}")
print(f"{p1} > {p3}: {p1 > p3}")

# Problem 4: Override multiplication
print("\n--- Problem 4: Multiply objects ---")
class Matrix:
    def __init__(self, value):
        self.value = value
    
    def __mul__(self, scalar):
        """Multiply matrix by a scalar"""
        return Matrix(self.value * scalar)
    
    def __str__(self):
        return f"Matrix({self.value})"

m1 = Matrix(5)
m2 = m1 * 3
print(f"{m1} * 3 = {m2}")

# Problem 5: Length of object using __len__
print("\n--- Problem 5: Custom length ---")
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        """Override len() function"""
        return len(self.songs)
    
    def __str__(self):
        return f"Playlist with {len(self)} songs"

playlist = Playlist(["Song1", "Song2", "Song3", "Song4"])
print(f"{playlist}")
print(f"Length: {len(playlist)}")

# Problem 6: Make object callable using __call__
print("\n--- Problem 6: Callable object ---")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make object callable like a function"""
        return x * self.factor

times5 = Multiplier(5)
print(f"5 * 10 = {times5(10)}")  # Object used like a function

# Problem 7: Override indexing with __getitem__
print("\n--- Problem 7: Custom indexing ---")
class MyList:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        """Enable indexing with []"""
        return self.data[index]
    
    def __len__(self):
        return len(self.data)

mylist = MyList([10, 20, 30, 40])
print(f"Item at index 2: {mylist[2]}")
print(f"Length: {len(mylist)}")

# CONCEPT SUMMARY:
# MAGIC METHODS (Dunder methods - double underscore):
# - __init__()     : Constructor
# - __str__()      : String representation (print)
# - __add__()      : Override + operator
# - __sub__()      : Override - operator
# - __mul__()      : Override * operator
# - __eq__()       : Override == operator
# - __gt__()       : Override > operator
# - __len__()      : Override len() function
# - __call__()     : Make object callable
# - __getitem__()  : Enable indexing []
#
# Benefits: Makes code intuitive and Pythonic


