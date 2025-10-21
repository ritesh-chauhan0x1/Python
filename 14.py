# ===== FILE 14: Number Sequences with While Loop =====
# Topic: Counting up and counting down using while loops
# Concepts: Increment, decrement, loop direction

# ===== COUNTING UP: 1 to 100 =====
print("=== Counting from 1 to 100 ===")
i = 1
while i <= 100:
    print(i, end=" ")  # Print on same line with space
    if i % 10 == 0:  # New line after every 10 numbers
        print()
    i = i + 1
print("\nCounting up completed!")

# ===== COUNTING DOWN: 100 to 1 =====
print("\n=== Counting from 100 to 1 ===")
i = 100
while i >= 1:  # Condition changes to >=
    print(i, end=" ")
    if i % 10 == 1:  # New line at 91, 81, 71, etc.
        print()
    i = i - 1  # Decrement instead of increment
print("\nCountdown completed!")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Count specific range
print("\n--- Practice: Count from 50 to 60 ---")
num = 50
while num <= 60:
    print(num, end=" → ")
    num += 1
print("Done")

# Problem 2: Count backwards from user input
print("\n--- Practice: Custom Countdown ---")
start = int(input("Enter starting number: "))
temp = start
while temp > 0:
    print(temp, end=" ")
    temp -= 1
print("Zero!")

# Problem 3: Skip numbers
print("\n--- Practice: Every 5th Number (1-50) ---")
i = 5
while i <= 50:
    print(i, end=" ")
    i += 5
print()

# Problem 4: Print only specific range
print("\n--- Practice: Numbers between 20 and 30 ---")
number = 20
while number <= 30:
    print(number, end=" | ")
    number += 1
print()

# Problem 5: Two counters simultaneously
print("\n--- Practice: Two Counters ---")
up = 1
down = 10
while up <= 5:
    print(f"Up: {up}, Down: {down}")
    up += 1
    down -= 1

# Problem 6: Sum while counting
print("\n--- Practice: Sum from 1 to N ---")
n = int(input("Enter N: "))
counter = 1
total = 0
while counter <= n:
    total += counter
    counter += 1
print(f"Sum of 1 to {n} = {total}")

# Problem 7: Print specific multiples
print("\n--- Practice: Multiples of 7 up to 70 ---")
multiple = 7
while multiple <= 70:
    print(multiple, end=" ")
    multiple += 7
print()

# Problem 8: Formatted counting
print("\n--- Practice: Formatted Output ---")
i = 1
while i <= 10:
    print(f"Number {i:02d}")  # 02d means 2 digits with leading zero
    i += 1

# Problem 9: Count with break condition
print("\n--- Practice: Count Until Condition ---")
count = 1
while count <= 100:
    if count == 50:
        print(f"\nStopped at {count}")
        break
    print(count, end=" ")
    count += 1

# Problem 10: Reverse table
print("\n\n--- Practice: Reverse Multiplication Table ---")
num = int(input("Enter number: "))
i = 10
while i >= 1:
    print(f"{num} × {i} = {num * i}")
    i -= 1

# KEY CONCEPTS:
# Counting UP:   start = low,  condition: i <= high, increment: i += 1
# Counting DOWN: start = high, condition: i >= low,  decrement: i -= 1
# 
# Common patterns:
# • i += 1  (increment by 1)
# • i -= 1  (decrement by 1)
# • i += 5  (increment by 5)
# • i *= 2  (double each time)
#
# Always ensure:
# 1. Counter is initialized correctly
# 2. Condition will eventually become False
# 3. Counter is updated inside loop