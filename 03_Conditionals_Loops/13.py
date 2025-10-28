# ===== FILE 13: While Loops =====
# Topic: While loop, counter variables, loop control
# Concepts: Condition-based repetition, increment operators

# ===== EXAMPLE 1: Basic While Loop =====
print("=== Example 1: Print message 5 times ===")
count = 1
while count <= 5:  # Loop continues while condition is True
    print("Hello Ritesh")
    count += 1  # Increment counter (same as count = count + 1)
print("Loop ended, count =", count)

# ===== EXAMPLE 2: Another Counter Loop =====
print("\n=== Example 2: Another message loop ===")
i = 1
while i < 6:  # Loop from 1 to 5
    print("Ok boss")
    i = i + 1
print("Final value of i:", i)

# ===== EXAMPLE 3: Print Numbers =====
print("\n=== Example 3: Print numbers 0 to 5 ===")
a = 0
while a < 6:
    print(a)
    a = a + 1

# ===== PRACTICE QUESTIONS =====

# Problem 1: Countdown timer
print("\n--- Practice: Countdown ---")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrement
print("Blast off! 🚀")

# Problem 2: Sum of first N numbers
print("\n--- Practice: Sum of First N Numbers ---")
n = int(input("Enter a number: "))
total = 0
counter = 1

while counter <= n:
    total += counter  # Add counter to total
    counter += 1

print(f"Sum of first {n} numbers: {total}")
# Formula: n*(n+1)/2

# Problem 3: While with break
print("\n--- Practice: Find First Multiple of 7 ---")
num = 1
while True:  # Infinite loop
    if num % 7 == 0:
        print(f"First multiple of 7: {num}")
        break  # Exit loop
    num += 1

# Problem 4: Password validator
print("\n--- Practice: Password Entry ---")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password! {remaining} attempts remaining")
        else:
            print("Account locked!")

# Problem 5: Print even numbers
print("\n--- Practice: Even Numbers from 2 to 20 ---")
even = 2
while even <= 20:
    print(even, end=" ")  # Print on same line
    even += 2
print()  # New line

# Problem 6: Multiplication table
print("\n--- Practice: Multiplication Table ---")
num = int(input("Enter number for table: "))
i = 1
while i <= 10:
    print(f"{num} × {i} = {num * i}")
    i += 1

# Problem 7: While with continue
print("\n--- Practice: Skip Multiples of 3 ---")
x = 0
while x < 10:
    x += 1
    if x % 3 == 0:
        continue  # Skip rest of loop body
    print(x, end=" ")
print()

# Problem 8: Factorial calculator
print("\n--- Practice: Factorial ---")
n = int(input("Enter number for factorial: "))
factorial = 1
temp = n

while temp > 0:
    factorial *= temp  # factorial = factorial * temp
    temp -= 1

print(f"{n}! = {factorial}")

# WHILE LOOP CONTROL:
# break     - Exit loop immediately
# continue  - Skip to next iteration
# else      - Executes when loop completes normally (no break)

# COMMON MISTAKES:
# 1. Forgetting to increment counter → infinite loop
# 2. Wrong condition → loop never runs or runs forever
# 3. Off-by-one errors in conditions

# WHILE vs FOR:
# While: Use when you don't know how many iterations needed
# For:   Use when iterating over a sequence or fixed range