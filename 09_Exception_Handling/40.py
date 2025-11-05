"""
Python Exception Handling - Try/Except Basics
==============================================
Exception handling allows you to handle errors gracefully without crashing the program.
"""

# Basic try-except block
print("=== Basic Try-Except ===")
try:
    result = 10 / 0  # This will cause ZeroDivisionError
except:
    print("An error occurred!")

# Catching specific exception
print("\n=== Catching Specific Exception ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple exceptions
print("\n=== Multiple Exceptions ===")
try:
    num = int("abc")  # ValueError
except ValueError:
    print("Error: Invalid integer conversion!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# Catching multiple exceptions in one block
print("\n=== Multiple Exceptions in One Block ===")
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"An error occurred: {e}")

# Getting exception details
print("\n=== Exception Details ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")

# Generic exception handler
print("\n=== Generic Exception Handler ===")
try:
    x = undefined_variable  # NameError
except Exception as e:
    print(f"Caught exception: {type(e).__name__} - {e}")

# Example: Safe division function
print("\n=== Safe Division Function ===")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid data types for division"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# Example: Safe input conversion
print("\n=== Safe Input Conversion ===")
def get_integer():
    try:
        user_input = "25"  # Simulating input
        number = int(user_input)
        return number
    except ValueError:
        return "Invalid input: Not a number"

print(f"Converted value: {get_integer()}")

# Example: Safe list access
print("\n=== Safe List Access ===")
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} out of range"
    except TypeError:
        return "Error: Invalid index type"

my_list = [10, 20, 30, 40]
print(f"Element at index 2: {get_element(my_list, 2)}")
print(f"Element at index 10: {get_element(my_list, 10)}")

# Common exceptions
print("\n=== Common Python Exceptions ===")
print("""
1. ZeroDivisionError - Division by zero
2. ValueError - Invalid value conversion
3. TypeError - Invalid operation for type
4. IndexError - List index out of range
5. KeyError - Dictionary key not found
6. FileNotFoundError - File doesn't exist
7. AttributeError - Object has no attribute
8. NameError - Variable not defined
9. ImportError - Module import failed
10. RuntimeError - Generic runtime error
""")

"""
PRACTICE PROBLEMS:
1. Write a try-except block to handle division by zero
2. Create a function that safely converts string to integer
3. Handle IndexError when accessing list elements
4. Create a calculator that handles all input errors
5. Write a function to safely access dictionary keys
6. Handle FileNotFoundError when opening a file
7. Create a function that handles multiple exception types
8. Write code to handle ValueError in int() conversion
9. Create a safe square root function (handle negative numbers)
10. Build a function that validates email format with try-except
"""
