# ===== FILE 4: Lists & List Slicing =====
# Topic: List creation, indexing, mutability, slicing syntax
# Concepts: Lists are mutable, mixed data types, slicing ranges

# ===== CREATING LISTS =====
# List of numbers (integers)
marks = [69, 66, 78, 65, 87, 89]
print("Type:", type(marks))  # <class 'list'>
print("Marks list:", marks)

# ===== ACCESSING ELEMENTS (INDEXING) =====
# Lists use zero-based indexing
print("\nAccessing elements:")
print("First element [0]:", marks[0])  # 69
print("Second element [1]:", marks[1])  # 66

# ===== MIXED DATA TYPE LIST =====
# Lists can contain different types: strings, integers, etc.
student = ["Ritesh Chauhan", 21, "India"]
print("\nStudent list:", student)

# ===== MUTABILITY =====
# Lists can be changed (mutable)
student[0] = "Arjun"  # Change first element
print("After changing name:", student)

# ===== LIST SLICING =====
# Syntax: list[start:end:step]
# start: starting index (inclusive)
# end: ending index (exclusive)
# step: increment (default 1)

print("\n=== List Slicing Examples ===")
print("Original marks:", marks)

# Range slicing
print("marks[1:4]:", marks[1:4])  # Elements from index 1 to 3
print("marks[:4]:", marks[:4])    # From start to index 3
print("marks[0:]:", marks[0:])    # From index 0 to end

# Negative indexing (from end)
print("marks[-3:]:", marks[-3:])  # Last 3 elements
# Note: marks[-3:-0] doesn't work as expected (use marks[-3:])

# ===== PRACTICE QUESTIONS =====

# Problem 1: Working with list slicing
print("\n--- Practice: Advanced Slicing ---")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Full list:", numbers)

# Get specific ranges
print("First 5 elements:", numbers[:5])      # [10, 20, 30, 40, 50]
print("Last 5 elements:", numbers[-5:])      # [60, 70, 80, 90, 100]
print("Middle elements:", numbers[3:7])      # [40, 50, 60, 70]
print("Every 2nd element:", numbers[::2])    # [10, 30, 50, 70, 90]
print("Every 3rd element:", numbers[::3])    # [10, 40, 70, 100]
print("Reverse list:", numbers[::-1])        # [100, 90, 80, ...]

# Problem 2: Create and modify list
print("\n--- Practice: List Operations ---")
colors = ["red", "blue", "green", "yellow", "purple"]
print("Original colors:", colors)

# Change elements
colors[1] = "orange"  # Change "blue" to "orange"
print("After changing index 1:", colors)

# Change multiple elements using slicing
colors[2:4] = ["pink", "brown"]
print("After changing [2:4]:", colors)

# Problem 3: List of mixed data
print("\n--- Practice: Personal Information ---")
person = [
    "John Doe",        # Name (string)
    25,                # Age (integer)
    5.9,               # Height in feet (float)
    True,              # Employed (boolean)
    ["Python", "Java"] # Skills (list inside list)
]
print("Person data:", person)
print("Name:", person[0])
print("Age:", person[1])
print("Skills:", person[4])
print("First skill:", person[4][0])  # Nested indexing

# Problem 4: Copy part of list
print("\n--- Practice: Extract Data ---")
scores = [45, 78, 92, 67, 88, 54, 91, 73]
print("All scores:", scores)

# Get top 3 scores
sorted_scores = sorted(scores, reverse=True)
top_3 = sorted_scores[:3]
print("Top 3 scores:", top_3)

# Get failing scores (below 50)
failing = [score for score in scores if score < 50]
print("Failing scores:", failing)

# Problem 5: List concatenation
print("\n--- Practice: Combining Lists ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # Concatenation
print("Combined list:", combined)

# Repetition
repeated = list1 * 3  # Repeat list 3 times
print("Repeated list:", repeated)

# LIST SLICING QUICK REFERENCE:
# [start:end]   - Elements from start to end-1
# [:end]        - Elements from beginning to end-1
# [start:]      - Elements from start to end
# [:]           - All elements (copy of list)
# [start:end:2] - Every 2nd element from start to end
# [::-1]        - Reverse list
# [-3:]         - Last 3 elements
# [:-3]         - All except last 3 elements 
