# ===== FILE 8: List & Tuple Practice Problems =====
# Topic: Palindrome lists, counting elements, tuple-to-list conversion
# Concepts: .copy(), .reverse(), .count(), list(), .sort()

# ===== PROBLEM 1: Check if list is palindrome =====
print("=== Palindrome List Checker ===")
# A palindrome list reads the same forwards and backwards
list5 = [1, 2, 3, 2, 1]
print("Original list:", list5)

# Method: Copy list, reverse it, compare with original
list1 = list5.copy()  # Create a copy (don't modify original)
list1.reverse()       # Reverse the copy
print("Reversed list:", list1)

if list5 == list1:
    print("The list IS a palindrome")
else:
    print("The list is NOT a palindrome")

# Alternative method using slicing
print("\n=== Alternative Palindrome Check ===")
test_list = [1, 2, 3, 2, 1]
if test_list == test_list[::-1]:  # Compare with reversed slice
    print(f"{test_list} is a palindrome")
else:
    print(f"{test_list} is not a palindrome")

# ===== PROBLEM 2: Count specific grade in tuple =====
print("\n=== Count Students with Grade 'A' ===")
grades = ("A", "B", "C", "D", "A", "B", "E", "A", "B")
print("All grades:", grades)

# Use .count() method to count occurrences
a_count = grades.count("A")
print(f"Number of students with 'A': {a_count}")

# Count all grades
print("\nGrade distribution:")
unique_grades = set(grades)  # Get unique grades
for grade in sorted(unique_grades):
    count = grades.count(grade)
    print(f"Grade {grade}: {count} students")

# ===== PROBLEM 3: Sort tuple by converting to list =====
print("\n=== Sort Grades (Tuple → List) ===")
# Tuples are immutable, so convert to list to sort
list1 = list(grades)  # Convert tuple to list
print("Converted to list:", list1)

list1.sort()  # Sort the list
print("Sorted list:", list1)

# Convert back to tuple if needed
sorted_tuple = tuple(list1)
print("Sorted tuple:", sorted_tuple)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Check multiple lists for palindrome
print("\n--- Practice: Multiple Palindrome Checks ---")
test_cases = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'b', 'a'],
    [10, 20, 30, 20, 10]
]

for lst in test_cases:
    is_palindrome = (lst == lst[::-1])
    result = "YES" if is_palindrome else "NO"
    print(f"{lst} → Palindrome: {result}")

# Problem 2: Count occurrences in list
print("\n--- Practice: Count Elements in List ---")
numbers = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2, 8]
print("Numbers:", numbers)
target = 2
print(f"Count of {target}:", numbers.count(target))

# Find all unique numbers and their counts
unique_nums = set(numbers)
print("\nFrequency of each number:")
for num in sorted(unique_nums):
    print(f"{num}: {numbers.count(num)} times")

# Problem 3: Tuple operations
print("\n--- Practice: Tuple Manipulation ---")
colors = ("red", "blue", "green", "blue", "yellow", "blue")
print("Colors tuple:", colors)
print("Count of 'blue':", colors.count("blue"))
print("Index of first 'green':", colors.index("green"))

# Convert to list, remove duplicates, sort
color_list = list(set(colors))  # set() removes duplicates
color_list.sort()
print("Unique sorted colors:", color_list)

# Problem 4: Mirror list generator
print("\n--- Practice: Create Palindrome List ---")
half = [1, 2, 3, 4]
palindrome = half + half[::-1]  # Combine list with its reverse
print(f"Half list: {half}")
print(f"Palindrome: {palindrome}")

# Without repeating middle element
palindrome2 = half + half[-2::-1]  # Exclude last element
print(f"Palindrome (no repeat): {palindrome2}")

# Problem 5: Grade statistics
print("\n--- Practice: Comprehensive Grade Analysis ---")
student_grades = ["A", "B", "A", "C", "B", "A", "D", "B", "A", "C"]
print("Student grades:", student_grades)

total_students = len(student_grades)
print(f"\nTotal students: {total_students}")

# Calculate percentage for each grade
for grade in ["A", "B", "C", "D", "E"]:
    count = student_grades.count(grade)
    percentage = (count / total_students) * 100
    print(f"Grade {grade}: {count} students ({percentage:.1f}%)")

# Find most common grade
from collections import Counter
most_common = Counter(student_grades).most_common(1)
print(f"\nMost common grade: {most_common[0][0]} ({most_common[0][1]} students)")

# KEY CONCEPTS:
# .copy()           - Create a copy of list (doesn't affect original)
# .reverse()        - Reverse list in place
# [::-1]            - Reverse using slicing (returns new list)
# .count(element)   - Count occurrences of element
# list(tuple)       - Convert tuple to list
# tuple(list)       - Convert list to tuple
# set(list)         - Remove duplicates (returns set)
# .sort()           - Sort list in place