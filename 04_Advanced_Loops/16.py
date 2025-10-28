# ===== FILE 16: Iterating Through Lists with While Loop =====
# Topic: Accessing list elements using index and while loop
# Concepts: len(), indexing, loop through list

# ===== PRINTING LIST ELEMENTS =====
print("=== Iterating Through List ===")
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Get list length
print("List:", numbers)
print("Length of list:", len(numbers))

# Loop through list using index
i = 0
while i < len(numbers):  # Loop from 0 to length-1
    element = numbers[i]  # Access element at index i
    print(f"Index {i}: {element}")
    i += 1

# ===== PRACTICE QUESTIONS =====

# Problem 1: Print with position
print("\n--- Practice: Formatted List Output ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
index = 0
while index < len(fruits):
    print(f"{index + 1}. {fruits[index]}")  # Start numbering from 1
    index += 1

# Problem 2: Sum of list elements
print("\n--- Practice: Calculate Sum ---")
scores = [85, 90, 78, 92, 88]
print("Scores:", scores)

i = 0
total = 0
while i < len(scores):
    total += scores[i]
    i += 1

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.2f}")

# Problem 3: Find maximum in list
print("\n--- Practice: Find Maximum ---")
numbers = [45, 78, 23, 91, 67, 34, 89]
print("Numbers:", numbers)

i = 0
max_num = numbers[0]  # Assume first element is max
while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1

print(f"Maximum number: {max_num}")

# Problem 4: Count specific value
print("\n--- Practice: Count Occurrences ---")
grades = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'A']
target = 'A'
print("Grades:", grades)

i = 0
count = 0
while i < len(grades):
    if grades[i] == target:
        count += 1
    i += 1

print(f"Count of '{target}': {count}")

# Problem 5: Reverse print list
print("\n--- Practice: Print List in Reverse ---")
colors = ["red", "green", "blue", "yellow", "purple"]
print("Original:", colors)
print("Reversed:")

i = len(colors) - 1  # Start from last index
while i >= 0:
    print(f"{i}: {colors[i]}")
    i -= 1

# Problem 6: Even indexed elements
print("\n--- Practice: Even Indexes Only ---")
items = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Full list:", items)
print("Even indexes:", end=" ")

i = 0
while i < len(items):
    print(items[i], end=" ")
    i += 2  # Jump by 2

print()

# Problem 7: Search for element
print("\n--- Practice: Search Element ---")
numbers = [10, 20, 30, 40, 50, 60]
search = 30
print("List:", numbers)
print(f"Searching for: {search}")

i = 0
found = False
while i < len(numbers):
    if numbers[i] == search:
        print(f"Found {search} at index {i}")
        found = True
        break
    i += 1

if not found:
    print(f"{search} not found in list")

# Problem 8: Create new list with squares
print("\n--- Practice: Create Squares List ---")
original = [1, 2, 3, 4, 5]
squares = []

i = 0
while i < len(original):
    square = original[i] ** 2
    squares.append(square)
    i += 1

print("Original:", original)
print("Squares:", squares)

# Problem 9: Filter elements
print("\n--- Practice: Filter Numbers > 50 ---")
numbers = [45, 67, 23, 89, 56, 34, 91]
filtered = []

i = 0
while i < len(numbers):
    if numbers[i] > 50:
        filtered.append(numbers[i])
    i += 1

print("Original:", numbers)
print("Filtered (>50):", filtered)

# Problem 10: Parallel lists
print("\n--- Practice: Combine Two Lists ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]

i = 0
while i < len(names):
    print(f"{names[i]} is {ages[i]} years old")
    i += 1

# ITERATING PATTERNS:
# Forward:  i = 0, while i < len(list), i += 1
# Backward: i = len(list) - 1, while i >= 0, i -= 1
# Skip:     i = 0, while i < len(list), i += 2
# 
# IMPORTANT:
# • List index starts at 0
# • Last index is len(list) - 1
# • Use i < len(list), NOT i <= len(list)
# • Always increment/update i to avoid infinite loop