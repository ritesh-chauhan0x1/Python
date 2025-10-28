# ===== FILE 1: Input & Comparison Operators =====
# Topic: Taking user input and comparing numbers
# Concepts: input(), type conversion, comparison operators

# Problem 1: Compare two numbers
# Ask user for two numbers and check if first is greater than or equal to second
a = float(input("Enter first number: "))  # float() converts string to decimal number
b = float(input("Enter second number: "))  # input() always returns string, so we convert it
print("Is", a, ">=", b, "?", a >= b)  # Comparison returns True or False

# ===== PRACTICE QUESTIONS =====

# Problem 2: Check if two numbers are equal
print("\n--- Problem 2: Check equality ---")
num1 = int(input("Enter first number: "))  # int() for whole numbers
num2 = int(input("Enter second number: "))
print("Are they equal?", num1 == num2)  # == checks equality

# Problem 3: Compare three numbers
print("\n--- Problem 3: Three number comparison ---")
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))
print("Is x < y < z?", x < y < z)  # Python allows chained comparisons
print("Is x the smallest?", x < y and x < z)  # Using 'and' operator

# Problem 4: Check if number is positive, negative, or zero
print("\n--- Problem 4: Positive/Negative/Zero check ---")
number = float(input("Enter a number: "))
print("Is positive?", number > 0)
print("Is negative?", number < 0)
print("Is zero?", number == 0)

# COMPARISON OPERATORS IN PYTHON:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to