"""
Python Modules & Packages - Math Module
========================================
A module is a file containing Python code (functions, classes, variables).
The math module provides mathematical functions and constants.
"""

import math

# Mathematical constants
print("=== Math Constants ===")
print(f"PI value: {math.pi}")  # 3.141592653589793
print(f"Euler's number (e): {math.e}")  # 2.718281828459045
print(f"Infinity: {math.inf}")
print(f"Not a Number: {math.nan}")

# Basic mathematical functions
print("\n=== Basic Math Functions ===")
print(f"Square root of 16: {math.sqrt(16)}")  # 4.0
print(f"Power 2^3: {math.pow(2, 3)}")  # 8.0
print(f"Absolute value of -10: {math.fabs(-10)}")  # 10.0

# Rounding functions
print("\n=== Rounding Functions ===")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")  # 5
print(f"Floor of 4.8: {math.floor(4.8)}")  # 4
print(f"Truncate 4.9: {math.trunc(4.9)}")  # 4

# Trigonometric functions
print("\n=== Trigonometric Functions ===")
angle = 45  # degrees
radian = math.radians(angle)  # Convert to radians
print(f"{angle} degrees = {radian} radians")
print(f"sin({angle}°) = {math.sin(radian):.4f}")
print(f"cos({angle}°) = {math.cos(radian):.4f}")
print(f"tan({angle}°) = {math.tan(radian):.4f}")

# Logarithmic functions
print("\n=== Logarithmic Functions ===")
print(f"Natural log of 10: {math.log(10)}")  # ln(10)
print(f"Log base 10 of 100: {math.log10(100)}")  # 2.0
print(f"Log base 2 of 8: {math.log2(8)}")  # 3.0

# Factorial and combinations
print("\n=== Factorial & Combinations ===")
print(f"Factorial of 5: {math.factorial(5)}")  # 120
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")  # 6

# Practical example: Calculate distance between two points
print("\n=== Practical Example: Distance Between Points ===")
x1, y1 = 0, 0  # Point 1
x2, y2 = 3, 4  # Point 2
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {distance}")

"""
PRACTICE PROBLEMS:
1. Calculate the area of a circle with radius 5 (use math.pi)
2. Find the hypotenuse of a right triangle with sides 6 and 8
3. Convert 90 degrees to radians and find its sine value
4. Calculate 2^10 using math.pow()
5. Find the factorial of 7
6. Round up 7.2 and round down 7.8
7. Calculate log base 10 of 1000
8. Find GCD of 56 and 98
9. Calculate the cube root of 27 (use math.pow with 1/3)
10. Find the distance between points (1,2) and (4,6)
"""
