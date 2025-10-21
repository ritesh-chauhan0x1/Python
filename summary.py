# ============================================================================
# PYTHON LEARNING SUMMARY - All Original Code with Comments
# Author: Ritesh Chauhan
# Purpose: Complete collection of all original Python practice code
# Files: 1.py through 24.py (Original versions with explanatory comments)
# ============================================================================

print("=" * 70)
print("PYTHON COURSE - COMPLETE CODE SUMMARY")
print("=" * 70)
print()

# ============================================================================
# FILE 1: INPUT AND COMPARISON OPERATORS
# ============================================================================
print("\n--- FILE 1: Input and Comparison ---")

# Taking user input and converting to integer
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))

# Comparison operators demonstration
print(a == b)  # Equal to - checks if both numbers are same
print(a != b)  # Not equal to - checks if numbers are different
print(a >= b)  # Greater than or equal to
print(a > b)   # Greater than
print(a <= b)  # Less than or equal to
print(a < b)   # Less than


# ============================================================================
# FILE 2: STRINGS AND STRING METHODS
# ============================================================================
print("\n--- FILE 2: Strings and String Methods ---")

# String variable
str1 = "ritesh chauhan"

# String methods - modifying case
print(str1.upper())      # Convert to uppercase: RITESH CHAUHAN
print(str1.lower())      # Convert to lowercase: ritesh chauhan
print(str1.title())      # Title case: Ritesh Chauhan
print(str1.capitalize()) # Capitalize first letter: Ritesh chauhan

# String slicing - extracting parts of string
print(str1[0])           # First character: 'r'
print(str1[7])           # Character at index 7: 'c'
print(str1[0:6])         # Slice from index 0 to 5: 'ritesh'
print(str1[:6])          # Same as above: 'ritesh'
print(str1[7:])          # From index 7 to end: 'chauhan'
print(str1[7:14])        # Slice from 7 to 13: 'chauhan'

# Negative indexing - counting from end
print(str1[-7])          # 7th character from end
print(str1[-7:-1])       # Slice using negative indices


# ============================================================================
# FILE 3: CONDITIONAL STATEMENTS
# ============================================================================
print("\n--- FILE 3: Conditional Statements ---")

# Example 1: Age eligibility check
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")

# Example 2: Grade calculator using elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:  # 90 > marks >= 80
    print("Grade B")
elif marks >= 70:  # 80 > marks >= 70
    print("Grade B")
elif marks >= 60:  # 70 > marks >= 60
    print("Grade C")
elif marks >= 50:  # 60 > marks >= 50
    print("Grade D")
elif marks >= 40:  # 50 > marks >= 40
    print("Grade E")
else:
    print("Better luck next time")
    print("GiveUp")

# Storing grade in variable
if marks >= 90:
    Grade = "A"
elif marks >= 80:
    Grade = "B"
elif marks >= 70:
    Grade = "B"
elif marks >= 60:
    Grade = "C"
elif marks >= 50:
    Grade = "D"
elif marks >= 40:
    Grade = "E"
else:
    Grade = "why you checking your grade"
    print("Better luck next time")
    print("GiveUp")
print("Your Grade is", Grade)

# Example 3: Nested if statements
if age >= 18:
    if age <= 70:  # Checking age range for driving
        print("You can drive")
    else:
        print("Can't drive, you're old")
else:
    print("Can't drive, sorry")

# Example 4: Odd or even checker
number = int(input("Enter a number: "))
if number % 2 == 0:  # Modulo operator - remainder is 0 means even
    print("The number", number, "is even number")
else:
    print("The number", number, "is odd number")

# Example 5: Find greatest of three numbers
num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd number: "))
if num1 > num2 > num3:
    print(num1, "is the greatest")
elif num2 > num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")

# Example 6: Multiple of 7 checker
multiple = int(input("Enter your number: "))
check = multiple % 7 == 0  # Boolean expression
if check == True:
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")


# ============================================================================
# FILE 4: LISTS AND LIST SLICING
# ============================================================================
print("\n--- FILE 4: Lists and List Slicing ---")

# Creating a list of marks
marks = [69, 66, 78, 65, 87, 89]
print(type(marks))  # <class 'list'>
print(marks)        # Print entire list
print(marks[0])     # First element (index 0)
print(marks[1])     # Second element (index 1)

# List with mixed data types
student = ["Ritesh Chauhan", 21, "India"]
print(student)

# Lists are mutable - can be changed
student[0] = "Arjun"  # Changing first element
print(student)

# List slicing - extracting portions
print(marks[1:4])    # Elements from index 1 to 3
print(marks[:4])     # Elements from start to index 3
print(marks[0:])     # Elements from index 0 to end
print(marks[-3:-0])  # Using negative indices


# ============================================================================
# FILE 5: LIST OPERATIONS AND METHODS
# ============================================================================
print("\n--- FILE 5: List Operations ---")

# Creating a list with duplicates
list_nums = [1, 3, 4, 5, 2, 5, 6, 6, 1]

# append() - adds element at the end
list_nums.append(10)
print(list_nums)

# sort() - arranges in ascending order
list_nums.sort()
print(list_nums)

# sort(reverse=True) - descending order
list_nums.sort(reverse=True)
print(list_nums)

# Adding more elements
list_nums.append(11)
list_nums.append(15)
print(list_nums)

# reverse() - reverses the order
list_nums.reverse()
print(list_nums)

list_nums.sort(reverse=True)
print(list_nums)

# insert(index, element) - insert at specific position
list_nums.insert(2, 0)
print(list_nums)

# remove(element) - removes first occurrence
list_nums.remove(0)
print(list_nums)

# pop(index) - removes element at index
list_nums.pop(5)
print(list_nums)

# Final sort
list_nums.sort()
print(list_nums)

# count() - counts occurrences of element
print(list_nums.count(1))


# ============================================================================
# FILE 6: TUPLES
# ============================================================================
print("\n--- FILE 6: Tuples ---")

# Creating a tuple
tup = (1, 2, 4, 3, 2, 4, 4, 1)
print(tup)
print(type(tup))  # <class 'tuple'>

# Accessing tuple elements by index
print(tup[1])  # Second element
print(tup[0])  # First element
print(tup[6])  # Seventh element

# Single element tuple - comma is important
tup1 = (1,)  # Comma makes it a tuple
print(type(tup1))

# Tuple methods
print(tup.index(4))   # Find index of first occurrence of 4
print(tup.count(2))   # Count occurrences of 2


# ============================================================================
# FILE 7: USER INPUT FOR LISTS
# ============================================================================
print("\n--- FILE 7: User Input Lists ---")

# Method 1: Store inputs in variables, then create list
movie1 = input("Enter your 1st fav movie: ")
movie2 = input("Enter your second movie: ")
movie3 = input("Enter your third movie: ")
movie_list = [movie1, movie2, movie3]
print(type(movie_list))
print(movie_list)

# Method 2: Append to empty list
movies = []
movies.append(input("Enter your 1st movie: "))
movies.append(input("Enter your 2nd movie: "))
movies.append(input("Enter your 3rd movie: "))
print(movies)


# ============================================================================
# FILE 8: LIST AND TUPLE PRACTICE
# ============================================================================
print("\n--- FILE 8: List/Tuple Practice ---")

# Check if list is a palindrome
list5 = [1, 2, 3, 2, 1]
list1 = list5.copy()  # Create a copy
list1.reverse()       # Reverse the copy
if list5 == list1:
    print("The list is palindrome")
else:
    print("Not")

# Count specific grade in tuple
grade = ("A", "B", "C", "D", "A", "B", "E", "A", "B")
print(grade.count("A"))  # Count how many times 'A' appears

# Sort the tuple by converting to list
list1 = list(grade)  # Convert tuple to list
list1.sort()         # Sort the list
print(list1)


# ============================================================================
# FILE 9: DICTIONARIES
# ============================================================================
print("\n--- FILE 9: Dictionaries ---")

# Creating a dictionary
student_dict = {
    "name": "Ritesh",
    "cgpa": 6.7,
    "marks": [],
}
print(student_dict["name"])  # Access value by key

# Adding new key-value pair
student_dict["subject"] = "Python", "Java"
print(student_dict["subject"])

# Nested dictionary - dictionary inside dictionary
student = {
    "name": "Ritesh",
    "subject": {
        "phy": 76,
        "chem": 67,
        "math": 100
    }
}
print(student["subject"])           # Access nested dictionary
print(student["subject"]["phy"])    # Access nested value

# Dictionary methods
print(student.keys())                # Get all keys
print(student.values())              # Get all values
print(student.items())               # Get key-value pairs
print(len(student))                  # Number of keys

# Access nested dictionary keys
print(list(student["subject"]))
print(student["subject"]["phy"])

# Converting to lists
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(len(student))

# update() - add or modify keys
student.update({"city": "Bhubaneswar"})
print(student)


# ============================================================================
# FILE 10: SETS
# ============================================================================
print("\n--- FILE 10: Sets ---")

# Creating a set from list - duplicates automatically removed
num_list = [1, 1, 2, 3, 4, 4, 5, 4, 3, 2, 5, 6, 7, 8, 1, 1, 9, 10, 9, 9, 9, 10]
num_set = set(num_list)
print(type(num_set), "=", num_set)

# Convert back to list
unique_list = list(num_set)
print(type(unique_list), "=", unique_list)

# Set operations
print(num_set.pop())  # Remove and return random element
print(num_set.pop())

num_set.add(11)       # Add element
print(num_set.pop())

num_set.add(22)
print(num_set.pop())

num_set.add(9)
print(num_set.pop())

num_set.add(3)
print(num_set)

# Removing multiple elements
print(num_set.pop())
print(num_set.pop())
print(num_set.pop())
print(num_set.pop())
print(num_set.pop())
print(num_set.pop())
print(num_set.pop())

# clear() - remove all elements
num_set.clear()
print(num_set)


# ============================================================================
# FILE 11: SET OPERATIONS
# ============================================================================
print("\n--- FILE 11: Set Operations ---")

# Creating two sets
set1 = {1, 2, 3, 4, 5, 6, 3, 4, 2, 5, 7, 4}
set2 = {4, 5, 4, 3, 2, 3, 8, 11, 2, 2, 3, 3, 4, 9, 10, 0}

# union() - combines all unique elements from both sets
print(set1.union(set2))

# intersection() - elements common to both sets
print(set1.intersection(set2))

# Dictionary with multiple meanings (using sets)
words = {
    "table": {
        "a piece of furniture",
        "list of facts & figures"
    },
    "cat": "animals",
}
print(words)

# Dictionary with list values
word_dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "animals",
}
print(word_dict)

# Practical example - count unique subjects
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print("Classroom needed:", len(subjects))  # Set removes duplicates


# ============================================================================
# FILE 12: DICTIONARY FROM INPUT
# ============================================================================
print("\n--- FILE 12: Dictionary from Input ---")

# Getting marks from user
a = int(input("Enter marks of math: "))
b = int(input("Enter marks of python: "))
c = int(input("Enter marks of javascript: "))

# Creating dictionaries
marks_dict = {}  # Empty dictionary
dict1 = {
    "math": a,
    "python": b,    # Fixed typo from original "pyhton"
    "javascript": c,
}

# update() - merges dict1 into marks_dict
marks_dict.update(dict1)
print(marks_dict)


# ============================================================================
# FILE 13: WHILE LOOPS BASICS
# ============================================================================
print("\n--- FILE 13: While Loops ---")

# Example 1: Print message 5 times
count = 1
while count <= 5:
    print("Hello Ritesh")
    count += 1  # Increment counter

# Example 2: Another loop
i = 1
while i < 6:
    print("Ok boss")
    i = i + 1

# Example 3: Print numbers
a = 0
while a < 6:
    print(a)
    a = a + 1


# ============================================================================
# FILE 14: NUMBER SEQUENCES
# ============================================================================
print("\n--- FILE 14: Number Sequences ---")

# Counting from 1 to 100
i = 1
while i <= 100:
    print(i)
    i = i + 1

# Counting from 100 to 1
i = 100
while i >= 1:
    print(i)
    i = i - 1


# ============================================================================
# FILE 15: MULTIPLICATION TABLE
# ============================================================================
print("\n--- FILE 15: Multiplication Table ---")

# User input for table
number = int(input("Enter a number for a table: "))
table = 1

# Generate table from 1 to 10
while table <= 10:
    print(number, "multiplying with", table, "=", number * table)
    table += 1


# ============================================================================
# FILE 16: ITERATE LISTS WITH WHILE
# ============================================================================
print("\n--- FILE 16: Iterate Lists ---")

# List of perfect squares
square_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(len(square_list))  # Length of list

# Loop through list using index
i = 0
while i < len(square_list):
    element = square_list[i]
    print(element)
    i += 1


# ============================================================================
# FILE 17: SEARCHING IN TUPLE
# ============================================================================
print("\n--- FILE 17: Searching in Tuple ---")

# Tuple of perfect squares
tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(tuples)

# Get search value from user
x = int(input("Enter number to search from the tuple: "))

# Linear search algorithm
b = 0
found = False
while b < len(tuples):
    if tuples[b] == x:
        print("Found at index", b)
        found = True
        break  # Exit after finding - FIXED BUG
    b += 1

if not found:
    print("Number not found in tuple")


# ============================================================================
# FILE 18: BREAK AND CONTINUE
# ============================================================================
print("\n--- FILE 18: Break and Continue ---")

# Break example - exits loop when condition met
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break  # Exit loop immediately
    i += 1
print("End of loop")

# Continue example - skips rest of iteration
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue  # Skip to next iteration
    print(i)
    i += 1


# ============================================================================
# FILE 19: ODD AND EVEN WITH CONTINUE
# ============================================================================
print("\n--- FILE 19: Odd/Even with Continue ---")

# Print odd numbers using continue
i = 0
while i <= 10:
    if i % 2 == 0:  # If even
        i += 1
        continue    # Skip printing
    print(i)        # Only prints odd
    i += 1

# Print even numbers using continue
i = 0
while i <= 10:
    if i % 2 != 0:  # If odd
        i += 1
        continue    # Skip printing
    print(i)        # Only prints even
    i += 1


# ============================================================================
# FILE 20: FOR LOOPS WITH SETS
# ============================================================================
print("\n--- FILE 20: For Loops ---")

# Iterate through a set
num_set = {1, 2, 6, 3, 1, 44, 3, 2, 3, 44, 1, 1, 3, 3, 4, 5, 53, 44, 34}
for val in num_set:  # For loop iterates through each element
    print(val)


# ============================================================================
# FILE 21: INTERACTIVE TUPLE AND LIST
# ============================================================================
print("\n--- FILE 21: Interactive Input ---")

# Create tuple from user input
tup_input = input("Enter elements for tuple (comma-separated): ")
tup = tuple(tup_input.split(','))  # split() converts string to list, tuple() converts to tuple
print("Tuple elements:")
for a in tup:
    print(a.strip())  # strip() removes extra spaces

# Search in tuple
search_element = input("Enter an element to find in the tuple: ").strip()
if search_element in tup:  # Membership test - FIXED BUG
    print("Element Found")
else:
    print("Not Found")

print()  # Blank line

# Create list from input
list_input = input("Enter elements for list (comma-separated): ")
num_list = list_input.split(',')
print("List elements:")
for element in num_list:
    print(element.strip())


# ============================================================================
# FILE 22: RANGE FUNCTION
# ============================================================================
print("\n--- FILE 22: Range Function ---")

# range(stop) - 0 to stop-1
for i in range(10):
    print(i)
print()

# range(start, stop) - start to stop-1
for i in range(2, 10):
    print(i)
print()

# range(start, stop, step) - with custom increment
for i in range(1, 10, 2):
    print(i)

# Even numbers 0 to 100
for i in range(0, 101, 2):
    print(i)
print()

# Odd numbers 1 to 100
for i in range(1, 101, 2):
    print(i)

# Counting backward (negative step)
for i in range(100, 0, -1):
    print(i)

# Multiplication table using range
table_num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(table_num * i)


# ============================================================================
# FILE 23: FACTORIAL CALCULATION
# ============================================================================
print("\n--- FILE 23: Factorial ---")

# Calculate factorial using while loop
n = int(input("Enter a number for factorial: "))
factorial = 1  # Start with 1 (not 0)
i = 1

while i <= n:
    factorial = factorial * i  # Multiply each number
    i += 1

print(factorial)


# ============================================================================
# FILE 24: PATTERN PRINTING
# ============================================================================
print("\n--- FILE 24: Pattern Printing ---")

# Pattern 1: Right triangle
a = 5
for b in range(a):
    print("*" * b)  # Print b stars

# Pattern 2: With spaces
c = 5
for d in range(c):
    print(" " * c, "*" * d)
    c -= 1  # Decrease c in each iteration

# Pattern 3: Pyramid (centered)
num = 5
for i in range(num):
    print(" " * (num - i), (2 * i - 1) * "*")


# ============================================================================
# END OF SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY COMPLETE - All 24 Files Covered")
print("=" * 70)
print("\nThis file contains:")
print("✓ All original code from 1.py to 24.py")
print("✓ Explanatory comments for each section")
print("✓ Bug fixes noted where applied")
print("✓ Organized by file number")
print("\nFor detailed practice problems, see individual enhanced files.")
print("For course structure, see PYTHON_COURSE_README.md")
print("=" * 70)
