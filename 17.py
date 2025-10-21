# ===== FILE 17: Searching in Tuple =====
# Topic: Linear search algorithm in tuple
# Concepts: Sequential search, tuple indexing, break statement, found flag

# ===== LINEAR SEARCH IN TUPLE =====
# Tuple of perfect squares
tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print("Tuple:", tuples)

# Get search value from user
x = int(input("Enter number to search in the tuple: "))

# Search using while loop
b = 0  # Index counter
found = False  # Flag to track if element is found

while b < len(tuples):
    if tuples[b] == x:  # Check if current element matches
        print(f"Found {x} at index {b}")
        found = True
        break  # Exit loop after finding (no need to continue)
    b += 1  # Move to next index

# Check if element was not found
if not found:
    print(f"Number {x} not found in tuple")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Search with for loop
print("\n--- Practice: Search Using For Loop ---")
numbers = (5, 10, 15, 20, 25, 30)
print("Tuple:", numbers)
search = int(input("Enter number to search: "))

for index, value in enumerate(numbers):
    if value == search:
        print(f"Found at index {index}")
        break
else:  # Executes if loop completes without break
    print("Not found")

# Problem 2: Find all occurrences
print("\n--- Practice: Find All Positions ---")
data = (3, 7, 3, 9, 3, 15, 3, 21)
print("Tuple:", data)
search = int(input("Find all positions of: "))

positions = []
for i in range(len(data)):
    if data[i] == search:
        positions.append(i)

if positions:
    print(f"Found at positions: {positions}")
else:
    print("Not found")

# Problem 3: Search in string tuple
print("\n--- Practice: Search in String Tuple ---")
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Fruits:", fruits)
search_fruit = input("Search for fruit: ").lower()

if search_fruit in fruits:
    index = fruits.index(search_fruit)  # Built-in method
    print(f"'{search_fruit}' found at index {index}")
else:
    print(f"'{search_fruit}' not in list")

# Problem 4: Count occurrences
print("\n--- Practice: Count Occurrences ---")
grades = ('A', 'B', 'A', 'C', 'B', 'A', 'D', 'A', 'B')
print("Grades:", grades)
search_grade = input("Grade to count: ").upper()

count = 0
i = 0
while i < len(grades):
    if grades[i] == search_grade:
        count += 1
    i += 1

print(f"Grade '{search_grade}' appears {count} times")
# Alternative: print(grades.count(search_grade))

# Problem 5: Search with condition
print("\n--- Practice: Find First Number > X ---")
numbers = (12, 45, 23, 67, 34, 89, 56)
print("Numbers:", numbers)
threshold = int(input("Find first number greater than: "))

index = 0
found = False
while index < len(numbers):
    if numbers[index] > threshold:
        print(f"First number > {threshold}: {numbers[index]} at index {index}")
        found = True
        break
    index += 1

if not found:
    print(f"No number greater than {threshold}")

# Problem 6: Binary search (sorted tuple)
print("\n--- Practice: Binary Search ---")
sorted_tuple = (2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78)
print("Sorted tuple:", sorted_tuple)
target = int(input("Search for: "))

# Binary search algorithm
left = 0
right = len(sorted_tuple) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if sorted_tuple[mid] == target:
        print(f"Found {target} at index {mid}")
        found = True
        break
    elif sorted_tuple[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print(f"{target} not found")

# Problem 7: Search in nested tuple
print("\n--- Practice: Search in Nested Tuple ---")
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
search = int(input("Search in 2D tuple: "))

found_at = None
for row_idx, row in enumerate(matrix):
    for col_idx, value in enumerate(row):
        if value == search:
            found_at = (row_idx, col_idx)
            break
    if found_at:
        break

if found_at:
    print(f"Found at position: row {found_at[0]}, column {found_at[1]}")
else:
    print("Not found")

# Problem 8: Search with multiple conditions
print("\n--- Practice: Complex Search ---")
students = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95)
)
print("Students:", students)
min_marks = int(input("Find students with marks >=: "))

print(f"\nStudents with marks >= {min_marks}:")
for name, marks in students:
    if marks >= min_marks:
        print(f"{name}: {marks}")

# SEARCH ALGORITHMS:
#
# Linear Search (Sequential):
# • Check each element one by one
# • Works on unsorted data
# • Time complexity: O(n)
# • Best for small datasets
#
# Binary Search:
# • Requires sorted data
# • Divides search space in half each time
# • Time complexity: O(log n)
# • Much faster for large datasets
#
# KEY CONCEPTS:
# • Use 'found' flag to track success
# • 'break' exits loop early
# • 'in' operator is simplest for membership test
# • .index() finds first occurrence
# • .count() counts occurrences
#
# LOOP PATTERNS:
# While with index:
#   i = 0
#   while i < len(tuple):
#       process(tuple[i])
#       i += 1
#
# For with enumerate:
#   for index, value in enumerate(tuple):
#       process(index, value)