# ===== FILE 15: Multiplication Table with While Loop =====
# Topic: Generating multiplication table using while loop
# Concepts: While loop, counter variable, multiplication, formatting

# ===== MULTIPLICATION TABLE =====
print("=== Multiplication Table Generator ===")
number = int(input("Enter a number for a table: "))
table = 1  # Counter variable

while table <= 10:  # Generate table from 1 to 10
    result = number * table
    print(f"{number} multiplying with {table} = {result}")
    table += 1  # Increment counter

# ===== PRACTICE QUESTIONS =====

# Problem 1: Formatted table
print("\n--- Practice: Better Formatted Table ---")
num = int(input("Enter number: "))
i = 1

print(f"\nMultiplication Table of {num}")
print("=" * 25)
while i <= 10:
    print(f"{num} × {i:2} = {num * i:3}")
    i += 1

# Problem 2: Custom range table
print("\n--- Practice: Custom Range ---")
num = int(input("Enter number: "))
start = int(input("Start from: "))
end = int(input("End at: "))

i = start
while i <= end:
    print(f"{num} × {i} = {num * i}")
    i += 1

# Problem 3: Reverse table
print("\n--- Practice: Reverse Order ---")
num = int(input("Enter number: "))
i = 10

print(f"Reverse table of {num}:")
while i >= 1:
    print(f"{num} × {i} = {num * i}")
    i -= 1

# Problem 4: Skip even multipliers
print("\n--- Practice: Odd Multipliers Only ---")
num = int(input("Enter number: "))
i = 1

while i <= 20:
    if i % 2 != 0:  # Only odd numbers
        print(f"{num} × {i} = {num * i}")
    i += 1

# Problem 5: Table with running sum
print("\n--- Practice: Table with Sum ---")
num = int(input("Enter number: "))
i = 1
total = 0

while i <= 10:
    result = num * i
    total += result
    print(f"{num} × {i} = {result:3}  (Running sum: {total})")
    i += 1

# Problem 6: Multiple tables
print("\n--- Practice: Multiple Tables ---")
start_table = int(input("Start table: "))
end_table = int(input("End table: "))

table_num = start_table
while table_num <= end_table:
    print(f"\nTable of {table_num}:")
    i = 1
    while i <= 10:
        print(f"{table_num} × {i} = {table_num * i}")
        i += 1
    table_num += 1

# Problem 7: Horizontal table
print("\n--- Practice: Horizontal Layout ---")
num = int(input("Enter number: "))
i = 1

print(f"Table of {num}: ", end="")
while i <= 10:
    print(f"{num * i}", end="  ")
    i += 1
print()

# Problem 8: Table until result exceeds limit
print("\n--- Practice: Stop at Limit ---")
num = int(input("Enter number: "))
limit = int(input("Stop when result exceeds: "))
i = 1

while True:
    result = num * i
    if result > limit:
        print(f"Stopped: {num} × {i} = {result} exceeds {limit}")
        break
    print(f"{num} × {i} = {result}")
    i += 1

# Problem 9: Division table
print("\n--- Practice: Division Table ---")
num = int(input("Enter number: "))
i = 1

print(f"\nDivision Table of {num}:")
while i <= 10:
    result = num / i
    print(f"{num} ÷ {i} = {result:.2f}")
    i += 1

# Problem 10: Interactive table quiz
print("\n--- Practice: Table Quiz ---")
import random
num = int(input("Which table to practice? "))
score = 0
questions = 5

q = 1
while q <= questions:
    multiplier = random.randint(1, 10)
    answer = int(input(f"Question {q}: {num} × {multiplier} = "))
    
    correct_answer = num * multiplier
    if answer == correct_answer:
        print("Correct! ✓")
        score += 1
    else:
        print(f"Wrong! Correct answer: {correct_answer}")
    q += 1

print(f"\nFinal Score: {score}/{questions}")

# MULTIPLICATION TABLE PATTERNS:
#
# Standard (1-10):
# i = 1
# while i <= 10:
#     print(f"{num} × {i} = {num * i}")
#     i += 1
#
# Custom range:
# i = start
# while i <= end:
#     print(f"{num} × {i} = {num * i}")
#     i += 1
#
# Reverse:
# i = 10
# while i >= 1:
#     print(f"{num} × {i} = {num * i}")
#     i -= 1
#
# FORMATTING TIPS:
# • Use f-strings for clean output
# • Align columns: {value:3} (3 chars wide)
# • Use × symbol (Alt+0215) for multiplication
# • Add headers and separators
#
# COMMON ENHANCEMENTS:
# • Running sum/average
# • Skip certain multipliers
# • Stop at condition
# • Multiple tables
# • Interactive quiz mode