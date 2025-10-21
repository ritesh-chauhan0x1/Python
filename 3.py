# ===== FILE 3: Conditional Statements (if-elif-else) =====
# Topic: Decision making, branching logic, nested conditions
# Concepts: if, elif, else, comparison operators, nested if

# ===== EXAMPLE 1: Simple If-Else =====
print("=== Age Eligibility Check ===")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")  # Executes if condition is True
else:
    print("You are not eligible")  # Executes if condition is False

# ===== EXAMPLE 2: Multiple Conditions with elif =====
print("\n=== Grade Calculator ===")
marks = int(input("Enter your marks: "))

# First approach: Print grade directly
if marks >= 90:
    print("Grade A")
elif marks >= 80:  # Simplified: if previous condition false, check this
    print("Grade B")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Better luck next time")
    print("Don't give up!")

# Second approach: Store grade in variable
if marks >= 90:
    Grade = "A"
elif marks >= 80:
    Grade = "B"
elif marks >= 70:
    Grade = "B"
elif marks >= 60:
    Grade = "C"
elif marks >= 50:
    Grade = "D"
elif marks >= 40:
    Grade = "E"
else:
    Grade = "F"
    print("Better luck next time")
    print("Keep studying!")

print("Your Grade is:", Grade)

# ===== EXAMPLE 3: Nested If Statements =====
print("\n=== Driving Eligibility (Nested Conditions) ===")
# Nested if: if inside another if
if age >= 18:
    if age <= 70:  # Checks only if first condition is True
        print("You can drive")
    else:
        print("Can't drive, too old")
else:
    print("Can't drive, too young")

# Better way using 'and':
if 18 <= age <= 70:  # Python allows chained comparisons
    print("You can drive (using chained comparison)")

# ===== EXAMPLE 4: Odd or Even Number =====
print("\n=== Odd/Even Checker ===")
number = int(input("Enter a number: "))
if number % 2 == 0:  # % is modulo operator (remainder)
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")

# ===== EXAMPLE 5: Find Greatest Number =====
print("\n=== Find Greatest of Three Numbers ===")
num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest")
elif num2 >= num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")

# ===== EXAMPLE 6: Multiple of 7 Checker =====
print("\n=== Multiple of 7 Checker ===")
multiple = int(input("Enter your number: "))
check = (multiple % 7 == 0)  # Boolean expression

if check:  # No need for 'check == True'
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Leap year checker
print("\n--- Practice: Leap Year Checker ---")
year = int(input("Enter a year: "))
# A year is leap if divisible by 4 BUT not by 100, UNLESS divisible by 400
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Problem 2: Positive/Negative/Zero
print("\n--- Practice: Number Classification ---")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Problem 3: Ticket pricing based on age
print("\n--- Practice: Movie Ticket Price ---")
age = int(input("Enter your age: "))
if age < 5:
    price = 0
    print("Free entry for kids under 5")
elif age <= 12:
    price = 100
    print("Child ticket: ₹100")
elif age <= 60:
    price = 200
    print("Adult ticket: ₹200")
else:
    price = 150
    print("Senior citizen discount: ₹150")

# Problem 4: Password validator
print("\n--- Practice: Simple Password Checker ---")
password = input("Create a password (min 8 characters): ")
if len(password) >= 8:
    if password.isalnum():  # Check if alphanumeric
        print("Password accepted")
    else:
        print("Password contains special characters")
else:
    print("Password too short!")

# CONDITIONAL OPERATORS:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# and Logical AND (both conditions must be True)
# or  Logical OR (at least one condition must be True)
# not Logical NOT (reverses the condition)