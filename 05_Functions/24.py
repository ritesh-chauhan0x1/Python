# ===== FILE 24: Pattern Printing =====
# Topic: Creating star patterns using loops
# Concepts: Nested loops, string repetition, spacing, pattern logic

# ===== PATTERN 1: Right Triangle =====
print("=== Pattern 1: Right Triangle ===")
a = 5
for b in range(a):
    print("*" * b)  # Print b stars on each line
# Output:
# (empty)
# *
# **
# ***
# ****

# ===== PATTERN 2: Descending Triangle =====
print("\n=== Pattern 2: Descending Triangle ===")
c = 5
for d in range(c):
    print(" " * c, "*" * d)  # Space and stars
    c -= 1
# Note: This decreases c in loop, affecting pattern

# ===== PATTERN 3: Pyramid (Centered) =====
print("\n=== Pattern 3: Pyramid ===")
num = 5
for i in range(num):
    spaces = " " * (num - i)  # Leading spaces decrease
    stars = "*" * (2 * i - 1)  # Stars increase by 2 (odd numbers)
    print(spaces, stars)
# Creates centered pyramid pattern

# ===== PRACTICE QUESTIONS =====

# Problem 1: Full right triangle
print("\n--- Practice: Complete Right Triangle ---")
rows = 5
for i in range(1, rows + 1):  # Start from 1
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# Problem 2: Inverted triangle
print("\n--- Practice: Inverted Triangle ---")
rows = 5
for i in range(rows, 0, -1):  # Count down
    print("*" * i)
# Output:
# *****
# ****
# ***
# **
# *

# Problem 3: Full pyramid
print("\n--- Practice: Perfect Pyramid ---")
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
# Output:
#     *
#    ***
#   *****
#  *******
# *********

# Problem 4: Inverted pyramid
print("\n--- Practice: Inverted Pyramid ---")
rows = 5
for i in range(rows, 0, -1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
# Output:
# *********
#  *******
#   *****
#    ***
#     *

# Problem 5: Diamond pattern
print("\n--- Practice: Diamond ---")
rows = 5
# Upper half (pyramid)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# Lower half (inverted)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Problem 6: Hollow square
print("\n--- Practice: Hollow Square ---")
size = 5
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)  # Top and bottom rows
    else:
        print("*" + " " * (size - 2) + "*")  # Hollow middle

# Problem 7: Number pattern
print("\n--- Practice: Number Triangle ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# Output:
# 1
# 12
# 123
# 1234
# 12345

# Problem 8: Alphabet pattern
print("\n--- Practice: Alphabet Pattern ---")
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end="")  # 65 is ASCII for 'A'
    print()
# Output:
# A
# AB
# ABC
# ABCD
# ABCDE

# Problem 9: Floyd's triangle
print("\n--- Practice: Floyd's Triangle ---")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Problem 10: Hourglass pattern
print("\n--- Practice: Hourglass ---")
rows = 5
# Top half (inverted pyramid)
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# Bottom half (pyramid)
for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Problem 11: Right-aligned triangle
print("\n--- Practice: Right-Aligned Triangle ---")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
# Output:
#     *
#    **
#   ***
#  ****
# *****

# Problem 12: Butterfly pattern
print("\n--- Practice: Butterfly ---")
n = 5
# Upper half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
# Lower half
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# PATTERN PRINTING CONCEPTS:
#
# Basic formula:
# • Rows: outer loop (for i in range(n))
# • Columns: inner loop (for j in range(i))
#
# Spacing:
# • Left spaces: " " * (n - i)
# • Centered: spaces = (width - stars) // 2
#
# Stars/characters:
# • Increasing: i or 2*i-1 (for pyramid)
# • Decreasing: n - i + 1
# • Odd numbers: 2*i - 1
#
# Common patterns:
# 1. Right triangle: stars increase (1, 2, 3, ...)
# 2. Inverted: stars decrease (5, 4, 3, ...)
# 3. Pyramid: centered with odd stars (1, 3, 5, ...)
# 4. Diamond: pyramid + inverted pyramid
# 5. Hollow: print only borders
#
# STRING REPETITION:
# • "*" * 5 produces "*****"
# • " " * 3 produces "   " (3 spaces)
# • Use for quick pattern generation
#
# TIPS:
# • Draw pattern on paper first
# • Identify rows and columns
# • Calculate spaces and characters for each row
# • Use nested loops for 2D patterns
# • Print without newline: print(x, end="")
# • Force newline: print()