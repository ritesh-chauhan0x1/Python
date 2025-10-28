# ===== FILE 22: Range Function in For Loops =====
# Topic: Using range() for numeric sequences
# Concepts: range(stop), range(start, stop), range(start, stop, step)

# ===== RANGE WITH STOP ONLY =====
# range(stop) - generates numbers from 0 to stop-1
print("=== range(10) - Numbers 0 to 9 ===")
for i in range(10):
    print(i, end=" ")
print("\n")

# ===== RANGE WITH START AND STOP =====
# range(start, stop) - generates numbers from start to stop-1
print("=== range(2, 10) - Numbers 2 to 9 ===")
for i in range(2, 10):
    print(i, end=" ")
print("\n")

# ===== RANGE WITH START, STOP, AND STEP =====
# range(start, stop, step) - generates numbers with custom increment
print("=== range(1, 10, 2) - Odd numbers 1 to 9 ===")
for i in range(1, 10, 2):  # Step size = 2
    print(i, end=" ")
print("\n")

# ===== EVEN NUMBERS =====
print("=== Even Numbers 0 to 100 ===")
for i in range(0, 101, 2):  # Start at 0, step by 2
    print(i, end=" ")
    if i % 20 == 0:  # New line every 20
        print()
print()

# ===== ODD NUMBERS =====
print("\n=== Odd Numbers 1 to 100 ===")
for i in range(1, 101, 2):  # Start at 1, step by 2
    print(i, end=" ")
    if i % 19 == 0:  # New line for readability
        print()
print()

# ===== REVERSE RANGE (COUNTDOWN) =====
print("\n=== Countdown 100 to 1 ===")
for i in range(100, 0, -1):  # Negative step for countdown
    print(i, end=" ")
    if i % 10 == 1:  # New line at 91, 81, etc.
        print()
print()

# ===== MULTIPLICATION TABLE =====
print("\n=== Multiplication Table ===")
table = int(input("Enter a number for table: "))
for i in range(1, 11):  # 1 to 10
    print(f"{table} × {i} = {table * i}")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Range examples
print("\n--- Practice: Different Range Patterns ---")
print("range(5):", list(range(5)))  # [0, 1, 2, 3, 4]
print("range(2, 8):", list(range(2, 8)))  # [2, 3, 4, 5, 6, 7]
print("range(0, 10, 3):", list(range(0, 10, 3)))  # [0, 3, 6, 9]
print("range(10, 0, -2):", list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# Problem 2: Sum of range
print("\n--- Practice: Sum of 1 to N ---")
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):  # +1 to include n
    total += i
print(f"Sum of 1 to {n}: {total}")
# Formula check: n*(n+1)/2
print(f"Formula result: {n * (n + 1) // 2}")

# Problem 3: Multiples
print("\n--- Practice: Multiples of 5 up to 50 ---")
for i in range(5, 51, 5):  # 5, 10, 15, ..., 50
    print(i, end=" ")
print()

# Problem 4: Square numbers
print("\n--- Practice: Squares of 1 to 10 ---")
for i in range(1, 11):
    print(f"{i}² = {i**2}")

# Problem 5: Reverse counting
print("\n--- Practice: Count from 20 to 10 ---")
for i in range(20, 9, -1):  # 20 to 10
    print(i, end=" → ")
print("Done")

# Problem 6: Skip numbers
print("\n--- Practice: Every 3rd Number (0-30) ---")
for i in range(0, 31, 3):
    print(i, end=" ")
print()

# Problem 7: Powers of 2
print("\n--- Practice: Powers of 2 ---")
for i in range(11):  # 0 to 10
    print(f"2^{i} = {2**i}")

# Problem 8: Nested range loops
print("\n--- Practice: Multiplication Grid ---")
print("   ", end="")
for i in range(1, 6):
    print(f"{i:3}", end="")
print()

for i in range(1, 6):
    print(f"{i:2}:", end="")
    for j in range(1, 6):
        print(f"{i*j:3}", end="")
    print()

# Problem 9: Countdown with message
print("\n--- Practice: Launch Countdown ---")
for i in range(10, 0, -1):
    print(f"T-minus {i}...")
print("Liftoff! 🚀")

# Problem 10: Pattern printing
print("\n--- Practice: Number Pattern ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Problem 11: Reverse multiplication table
print("\n--- Practice: Reverse Table ---")
num = int(input("Enter number for reverse table: "))
for i in range(10, 0, -1):
    print(f"{num} × {i} = {num * i}")

# Problem 12: ASCII characters
print("\n--- Practice: ASCII Letters ---")
for i in range(65, 91):  # A to Z
    print(f"{i}: {chr(i)}", end=" | ")
    if (i - 64) % 5 == 0:
        print()

# RANGE SYNTAX:
# range(stop)              → 0 to stop-1
# range(start, stop)       → start to stop-1
# range(start, stop, step) → start to stop-1, increment by step
#
# IMPORTANT NOTES:
# • range() is exclusive of stop (stop-1 is last number)
# • Negative step for counting down
# • range() returns a range object (not a list)
# • Use list(range()) to convert to list
#
# COMMON PATTERNS:
# 1 to n:        range(1, n+1)
# 0 to n-1:      range(n)
# Even numbers:  range(0, n, 2) or range(2, n, 2)
# Odd numbers:   range(1, n, 2)
# Countdown:     range(n, 0, -1)
# Reverse:       range(n-1, -1, -1)