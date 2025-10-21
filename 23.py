# ===== FILE 23: Factorial Calculation =====
# Topic: Calculating factorial using while loop
# Concepts: Factorial (n!), multiplication loop, accumulator pattern

# ===== FACTORIAL CALCULATION =====
# Factorial: n! = n × (n-1) × (n-2) × ... × 2 × 1
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

print("=== Factorial Calculator ===")
n = int(input("Enter a number for factorial: "))

factorial = 1  # Start with 1 (not 0, as 0 × anything = 0)
i = 1

while i <= n:
    factorial = factorial * i  # Multiply each number
    i += 1

print(f"{n}! = {factorial}")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Factorial with explanation
print("\n--- Practice: Show Calculation Steps ---")
num = int(input("Enter number: "))
result = 1
i = 1
calculation = ""

while i <= num:
    result *= i
    calculation += str(i)
    if i < num:
        calculation += " × "
    i += 1

print(f"{num}! = {calculation} = {result}")

# Problem 2: Factorial using for loop
print("\n--- Practice: Factorial with For Loop ---")
n = int(input("Enter number: "))
factorial = 1

for i in range(1, n + 1):  # 1 to n (inclusive)
    factorial *= i

print(f"{n}! = {factorial}")

# Problem 3: Factorial of multiple numbers
print("\n--- Practice: Factorial Table ---")
for num in range(1, 11):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"{num:2}! = {fact:,}")  # Comma separates thousands

# Problem 4: Factorial with function
print("\n--- Practice: Factorial Function ---")
def factorial_func(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter number: "))
print(f"{num}! = {factorial_func(num)}")

# Problem 5: Recursive factorial
print("\n--- Practice: Recursive Factorial ---")
def factorial_recursive(n):
    """Calculate factorial recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Enter number: "))
print(f"{num}! (recursive) = {factorial_recursive(num)}")

# Problem 6: Factorial with validation
print("\n--- Practice: Validated Input ---")
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Factorial not defined for negative numbers")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")

fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")

# Problem 7: Compare factorials
print("\n--- Practice: Factorial Growth ---")
for i in range(1, 11):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    print(f"{i}! = {fact:>10,}")  # Right-aligned with commas

# Problem 8: Using math module
print("\n--- Practice: Using Built-in Function ---")
import math
num = int(input("Enter number: "))
print(f"{num}! = {math.factorial(num)}")

# Problem 9: Trailing zeros in factorial
print("\n--- Practice: Count Trailing Zeros ---")
def count_trailing_zeros(n):
    """Count trailing zeros in n!"""
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

num = int(input("Enter number: "))
fact = math.factorial(num)
zeros = count_trailing_zeros(num)
print(f"{num}! = {fact}")
print(f"Trailing zeros: {zeros}")

# Problem 10: Factorial vs Exponential
print("\n--- Practice: Factorial vs 2^n ---")
print("n    n!           2^n")
print("=" * 30)
for n in range(1, 11):
    fact = math.factorial(n)
    power = 2 ** n
    print(f"{n:2}   {fact:>10}   {power:>10}")

# FACTORIAL PROPERTIES:
# • 0! = 1 (by definition)
# • 1! = 1
# • n! = n × (n-1)!
# • Grows very rapidly
# • Used in permutations and combinations
#
# FACTORIAL FORMULAS:
# • Permutations: P(n,r) = n! / (n-r)!
# • Combinations: C(n,r) = n! / (r! × (n-r)!)
#
# CALCULATION METHODS:
# 1. Iterative (loop): Most common, efficient
# 2. Recursive: Elegant but slower for large n
# 3. Built-in (math.factorial): Fastest, most reliable
#
# IMPORTANT NOTES:
# • Start with 1 (not 0) for multiplication
# • Factorial grows extremely fast
# • 20! = 2,432,902,008,176,640,000
# • Negative numbers: factorial undefined
# • Decimal numbers: use gamma function instead