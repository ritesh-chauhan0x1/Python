# ===== FILE 6: Tuples - Immutable Sequences =====
# Topic: Working with tuples (immutable lists)
# Concepts: Tuples cannot be changed after creation, tuple methods

# Creating a tuple
tup = (1, 2, 4, 3, 2, 4, 4, 1)
print("Tuple:", tup)
print("Type:", type(tup))  # <class 'tuple'>

# ===== ACCESSING ELEMENTS =====
# Tuples use indexing like lists (0-based)
print("\nAccessing elements:")
print("Element at index 1:", tup[1])  # Second element (index 1)
print("Element at index 0:", tup[0])  # First element
print("Element at index 6:", tup[6])  # Seventh element
print("Last element:", tup[-1])  # Negative indexing from end

# ===== SINGLE ELEMENT TUPLE =====
# Important: Single element tuple needs a comma
tup1 = (1,)  # Comma makes it a tuple
print("\nSingle element tuple:", tup1)
print("Type:", type(tup1))  # <class 'tuple'>

# Without comma, it's just the value in parentheses
not_tuple = (1)  # This is just an integer
print("Without comma:", not_tuple, "Type:", type(not_tuple))  # <class 'int'>

# ===== TUPLE METHODS =====
# .index(element) - finds first index of element
print("\nTuple methods:")
print("Index of 4:", tup.index(4))  # Returns first occurrence
print("Index of 2:", tup.index(2))

# .count(element) - counts occurrences
print("Count of 2:", tup.count(2))
print("Count of 4:", tup.count(4))
print("Count of 1:", tup.count(1))

# ===== TUPLE SLICING =====
print("\nTuple slicing:")
print("First 3 elements:", tup[0:3])  # or tup[:3]
print("Last 3 elements:", tup[-3:])
print("Every 2nd element:", tup[::2])

# ===== PRACTICE QUESTIONS =====

# Problem 1: Create tuple from user input
print("\n--- Practice: Create tuple from input ---")
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
print("Your tuple:", numbers)
print("Length:", len(numbers))

if len(numbers) > 0:
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

# Problem 2: Tuple unpacking
print("\n--- Practice: Tuple unpacking ---")
coordinates = (10, 20)
x, y = coordinates  # Unpacking tuple into variables
print(f"X coordinate: {x}, Y coordinate: {y}")

# Multiple assignment using tuples
a, b, c = (100, 200, 300)
print(f"a={a}, b={b}, c={c}")

# Problem 3: Nested tuples
print("\n--- Practice: Nested tuples ---")
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matrix:", matrix)
print("First row:", matrix[0])
print("Element at [1][2]:", matrix[1][2])  # Row 1, Column 2

# Problem 4: Converting between list and tuple
print("\n--- Practice: List ↔ Tuple conversion ---")
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)  # Convert list to tuple
print("List to tuple:", my_tuple)

back_to_list = list(my_tuple)  # Convert tuple to list
back_to_list.append(6)  # Now we can modify it
print("Modified list:", back_to_list)

# WHY USE TUPLES?
# 1. Immutable - cannot be accidentally changed
# 2. Faster than lists
# 3. Can be used as dictionary keys (lists cannot)
# 4. Protect data that shouldn't change

# TUPLE vs LIST:
# Tuple: ( ) - Immutable, faster, less methods
# List:  [ ] - Mutable, slower, more methods