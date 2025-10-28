# ===== FILE 34: OOP - Circle Class with Area and Perimeter =====
# Topic: Creating geometric shape classes
# Concepts: Constructor, methods, mathematical calculations, constants

# ORIGINAL CODE - Circle class with area and perimeter

class Circe:  # Note: Typo in original class name
    """Class to represent a circle with radius"""
    
    def __init__(self, r):
        """Initialize circle with radius"""
        self.radius = r
    
    def area(self):
        """Calculate area of circle"""
        return (22/7) * self.radius * self.radius
    
    def perimeter(self):
        """Calculate perimeter (circumference) of circle"""
        return (22/7) * 2 * self.radius

# Create circle and calculate properties
radius = Circe(21)
print(radius.area())        # Area of circle with radius 21
print(radius.perimeter())   # Perimeter of circle with radius 21

# ===== PRACTICE QUESTIONS =====

# Problem 1: Fix class name and use proper PI value
print("\n--- Problem 1: Circle with proper PI ---")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius
    
    def display(self):
        print(f"Circle with radius {self.radius}:")
        print(f"  Diameter: {self.diameter():.2f}")
        print(f"  Area: {self.area():.2f}")
        print(f"  Circumference: {self.circumference():.2f}")

c1 = Circle(7)
c1.display()

# Problem 2: Create Rectangle class
print("\n--- Problem 2: Rectangle class ---")
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
    
    def diagonal(self):
        return math.sqrt(self.length**2 + self.width**2)

rect = Rectangle(10, 6)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Diagonal: {rect.diagonal():.2f}")
print(f"Is square? {rect.is_square()}")

# Problem 3: Create Triangle class
print("\n--- Problem 3: Triangle class ---")
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_valid(self):
        """Check if triangle is valid"""
        return (self.a + self.b > self.c and 
                self.b + self.c > self.a and 
                self.a + self.c > self.b)
    
    def area(self):
        """Calculate area using Heron's formula"""
        if not self.is_valid():
            return 0
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

tri = Triangle(3, 4, 5)
print(f"Valid triangle? {tri.is_valid()}")
print(f"Area: {tri.area():.2f}")
print(f"Perimeter: {tri.perimeter()}")

# Problem 4: Create Square class
print("\n--- Problem 4: Square class ---")
class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def diagonal(self):
        return self.side * math.sqrt(2)

sq = Square(5)
print(f"Area: {sq.area()}")
print(f"Perimeter: {sq.perimeter()}")
print(f"Diagonal: {sq.diagonal():.2f}")

# Problem 5: Create Cylinder class
print("\n--- Problem 5: Cylinder class ---")
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return math.pi * self.radius ** 2 * self.height
    
    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)
    
    def display(self):
        print(f"Cylinder (r={self.radius}, h={self.height}):")
        print(f"  Volume: {self.volume():.2f}")
        print(f"  Surface Area: {self.surface_area():.2f}")

cyl = Cylinder(3, 10)
cyl.display()

# Problem 6: Create Sphere class
print("\n--- Problem 6: Sphere class ---")
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

sphere = Sphere(5)
print(f"Volume: {sphere.volume():.2f}")
print(f"Surface Area: {sphere.surface_area():.2f}")

# Problem 7: Create a Shape base class with inheritance
print("\n--- Problem 7: Shape inheritance ---")
class Shape:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        print(f"This is a {self.name}")

class Circle2(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

shape = Circle2(10)
shape.describe()
print(f"Area: {shape.area():.2f}")

# CONCEPT SUMMARY:
# - Classes can represent real-world objects (geometric shapes)
# - math module provides constants like math.pi
# - Methods can call other methods of the same class
# - Use descriptive method names (area, perimeter, volume)
# - ** operator for exponentiation (power)
# - Mathematical formulas:
#   * Circle area: π × r²
#   * Circle circumference: 2 × π × r
#   * Rectangle area: length × width
#   * Triangle area (Heron's): √(s(s-a)(s-b)(s-c))
#   * Cylinder volume: π × r² × h        