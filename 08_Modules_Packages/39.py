"""
Python Modules & Packages - Custom Modules
===========================================
You can create your own modules by saving Python code in .py files.
Then import and use them in other files.
"""

# This file demonstrates how to create and use custom modules
# First, let's create some utility functions that could be a module

# =========================
# EXAMPLE 1: Math Utilities
# =========================
# If this was saved as 'math_utils.py', you could import it

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Testing the functions
print("=== Math Utilities Module ===")
print(f"Add 10 + 5 = {add(10, 5)}")
print(f"Subtract 10 - 5 = {subtract(10, 5)}")
print(f"Multiply 10 * 5 = {multiply(10, 5)}")
print(f"Divide 10 / 5 = {divide(10, 5)}")

# =========================
# EXAMPLE 2: String Utilities
# =========================
# If this was saved as 'string_utils.py', you could import it

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):
    """Check if string is palindrome"""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return text.title()

# Testing the functions
print("\n=== String Utilities Module ===")
text = "hello world"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")
print(f"Vowel count: {count_vowels(text)}")
print(f"Is 'madam' palindrome? {is_palindrome('madam')}")
print(f"Capitalized: {capitalize_words(text)}")

# =========================
# EXAMPLE 3: List Utilities
# =========================
# If this was saved as 'list_utils.py', you could import it

def find_max(numbers):
    """Find maximum in list"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    """Find minimum in list"""
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def calculate_average(numbers):
    """Calculate average of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    """Remove duplicates from list"""
    return list(set(items))

# Testing the functions
print("\n=== List Utilities Module ===")
numbers = [45, 23, 67, 12, 89, 34, 67, 12]
print(f"Numbers: {numbers}")
print(f"Maximum: {find_max(numbers)}")
print(f"Minimum: {find_min(numbers)}")
print(f"Average: {calculate_average(numbers):.2f}")
print(f"Without duplicates: {remove_duplicates(numbers)}")

# =========================
# HOW TO USE CUSTOM MODULES
# =========================
print("\n=== How to Import Custom Modules ===")
print("""
To use these functions in another file:

1. Save functions in a file (e.g., 'math_utils.py')
2. In another file, import the module:
   
   # Import entire module
   import math_utils
   result = math_utils.add(5, 3)
   
   # Import specific functions
   from math_utils import add, subtract
   result = add(5, 3)
   
   # Import with alias
   import math_utils as mu
   result = mu.add(5, 3)
   
   # Import all functions (not recommended)
   from math_utils import *
   result = add(5, 3)
""")

# =========================
# __name__ == "__main__"
# =========================
print("\n=== Module vs Script ===")
print(f"Current __name__: {__name__}")
print("""
When you run a file directly, __name__ is '__main__'
When you import it as a module, __name__ is the module name

Example usage:
if __name__ == "__main__":
    # This code only runs when file is executed directly
    # Not when imported as a module
    print("Running as main script")
""")

"""
PRACTICE PROBLEMS:
1. Create a function to check if a number is prime
2. Create a function to generate Fibonacci sequence up to n terms
3. Create a function to convert Celsius to Fahrenheit
4. Create a function to count words in a string
5. Create a function to find factorial recursively
6. Create a function to check if a string is an anagram of another
7. Create a function to find the second largest number in a list
8. Create a function to merge two sorted lists
9. Create a function to remove all whitespace from a string
10. Create a validation module with functions for email, phone, password validation

CHALLENGE:
Create three separate module files:
- calculator.py (add, subtract, multiply, divide)
- converter.py (celsius_to_fahrenheit, km_to_miles, etc.)
- validators.py (is_email, is_phone, is_password_strong)
Then import and use them in a main.py file
"""
