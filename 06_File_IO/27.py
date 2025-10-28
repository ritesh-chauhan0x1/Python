# ===== FILE 27: Recursion - Functions Calling Themselves =====
# Topic: Recursive functions and their applications
# Concepts: Recursion, base case, recursive case, stack memory

# ORIGINAL CODE - Recursive functions

# Function 1: Calculate sum of first n natural numbers using recursion
def sum(n):
    """Recursive function to sum natural numbers from 1 to n"""
    if (n == 0):  # Base case - stops recursion
        return 0
    return sum(n - 1) + n  # Recursive case

print(sum(5))  # Output: 15 (1+2+3+4+5)

# Function 2: Print all elements of a list using recursion
def printlist(list, index=0):
    """Recursively print each item in a list"""
    if (index == len(list)):  # Base case - reached end of list
        return
    print(list[index])  # Print current element
    printlist(list, index + 1)  # Recursive call with next index

cities = ["brj", "ktm", "pkhr", "jnk"]
printlist(cities)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Calculate factorial using recursion
print("\n--- Problem 1: Factorial recursion ---")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120
print("Factorial of 6:", factorial(6))  # Output: 720

# Problem 2: Calculate power using recursion (x^n)
print("\n--- Problem 2: Power calculation ---")
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("2^5 =", power(2, 5))  # Output: 32
print("3^4 =", power(3, 4))  # Output: 81

# Problem 3: Find nth Fibonacci number
print("\n--- Problem 3: Fibonacci sequence ---")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6:", fibonacci(6))  # Output: 8 (0,1,1,2,3,5,8)
print("Fibonacci of 8:", fibonacci(8))  # Output: 21

# Problem 4: Reverse a string using recursion
print("\n--- Problem 4: Reverse string recursively ---")
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print("Reverse of 'Python':", reverse_string("Python"))

# Problem 5: Count digits in a number
print("\n--- Problem 5: Count digits ---")
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("Digits in 12345:", count_digits(12345))  # Output: 5

# Problem 6: Sum of digits using recursion
print("\n--- Problem 6: Sum of digits ---")
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print("Sum of digits in 1234:", sum_of_digits(1234))  # Output: 10

# Problem 7: Print numbers from n to 1
print("\n--- Problem 7: Countdown ---")
def countdown(n):
    if n == 0:
        return
    print(n, end=" ")
    countdown(n - 1)

print("Countdown from 5:")
countdown(5)
print()

# Problem 8: Calculate GCD using recursion (Euclidean algorithm)
print("\n--- Problem 8: GCD (Greatest Common Divisor) ---")
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6

# CONCEPT SUMMARY:
# - Recursion: A function calling itself
# - Base case: Condition that stops recursion
# - Recursive case: Function calls itself with modified argument
# - Each call waits for the next to complete (stack)
# - Simpler code but uses more memory
# - Good for: trees, graphs, divide-and-conquer problems