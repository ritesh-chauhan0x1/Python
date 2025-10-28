# ===== FILE 26: Functions - Practical Applications =====
# Topic: Creating reusable functions for common tasks
# Concepts: Function definition, parameters, return values, function calls

# ORIGINAL CODE - Functions with different purposes

# Function 1: Print the length of a list
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["abc", "def", "ghi"]

def print_len_list(list):
    """Print the length of any list"""
    print(len(list))

print_len_list(list1)  # Output: 6
print_len_list(list2)  # Output: 3

# Function 2: Print all elements of a list in a single line
def print_listsl(list):
    """Print all items in a list on one line"""
    for items in list:
        print(items, end=" ")

print_listsl(list1)  # Output: 1 2 3 4 5 6
print_listsl(list2)  # Output: abc def ghi
print()

# Function 3: Calculate factorial of a number
def fact(n):
    """Calculate factorial using loop"""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

fact(10)  # 10! = 3628800
fact(5)   # 5! = 120
fact(6)   # 6! = 720
fact(5)   # 5! = 120

# Function 4: Convert USD to INR
def convert(usd):
    """Convert US Dollars to Indian Rupees"""
    inr = usd * 83  # Conversion rate
    print("Rs : ", inr)

convert(10)  # $10 = Rs 830

# Function 5: Check if number is odd or even
def numberOddEven(number):
    """Determine if a number is odd or even"""
    if (number % 2 == 0):
        print("Even")
    else:
        print("Odd")

numberOddEven(number=int(input("Enter Your Number : ")))

# ===== PRACTICE QUESTIONS =====

# Problem 1: Create a function to calculate the square of a number
print("\n--- Problem 1: Square function ---")
def square(n):
    return n * n

print("Square of 5:", square(5))
print("Square of 12:", square(12))

# Problem 2: Create a function to find maximum of three numbers
print("\n--- Problem 2: Maximum of three ---")
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Max of 10, 25, 15:", find_max(10, 25, 15))

# Problem 3: Create a function to check if a number is prime
print("\n--- Problem 3: Prime number checker ---")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))

# Problem 4: Create a function to reverse a string
print("\n--- Problem 4: Reverse string ---")
def reverse_string(text):
    return text[::-1]

print("Reverse of 'Python':", reverse_string("Python"))

# Problem 5: Create a function to calculate area of rectangle
print("\n--- Problem 5: Rectangle area ---")
def rectangle_area(length, width):
    return length * width

print("Area of 5x3 rectangle:", rectangle_area(5, 3))

# Problem 6: Create a function to convert Celsius to Fahrenheit
print("\n--- Problem 6: Temperature conversion ---")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))

# Problem 7: Create a function to count vowels in a string
print("\n--- Problem 7: Count vowels ---")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("Vowels in 'education':", count_vowels("education"))

# CONCEPT SUMMARY:
# - Functions help organize code into reusable blocks
# - def keyword defines a function
# - Parameters allow passing data to functions
# - return statement sends data back from function
# - Functions can call other functions
# - Docstrings document what a function does
