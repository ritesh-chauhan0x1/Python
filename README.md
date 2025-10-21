# Python Programming Course

Complete Python programming course covering fundamentals to intermediate concepts. This repository contains 24 progressive lessons with hands-on code examples and practice problems.

---

## Course Overview

This course is designed for beginners to learn Python programming through practical examples. Each file focuses on a specific topic and builds upon previous concepts.

**Total Files:** 24 Python files (1.py - 24.py)  
**Practice Problems:** 150+ exercises  
**Concepts Covered:** 50+ Python topics  
**Difficulty:** Beginner to Intermediate  

---

## Table of Contents

### Module 1: Python Basics
- [File 1: Input and Comparison Operators](#file-1-input-and-comparison-operators)
- [File 2: Strings and String Methods](#file-2-strings-and-string-methods)
- [File 3: Conditional Statements](#file-3-conditional-statements)
- [File 4: Lists and List Slicing](#file-4-lists-and-list-slicing)

### Module 2: Data Structures
- [File 5: List Operations and Methods](#file-5-list-operations-and-methods)
- [File 6: Tuples](#file-6-tuples)
- [File 7: User Input for Lists](#file-7-user-input-for-lists)
- [File 8: List and Tuple Practice](#file-8-list-and-tuple-practice)
- [File 9: Dictionaries](#file-9-dictionaries)
- [File 10: Sets](#file-10-sets)
- [File 11: Set Operations](#file-11-set-operations)
- [File 12: Dictionary from User Input](#file-12-dictionary-from-user-input)

### Module 3: While Loops
- [File 13: While Loop Basics](#file-13-while-loop-basics)
- [File 14: Number Sequences](#file-14-number-sequences)
- [File 15: Multiplication Tables](#file-15-multiplication-tables)
- [File 16: Iterating Lists with While](#file-16-iterating-lists-with-while)
- [File 17: Searching in Tuples](#file-17-searching-in-tuples)
- [File 18: Break and Continue](#file-18-break-and-continue)
- [File 19: Odd and Even Numbers](#file-19-odd-and-even-numbers)

### Module 4: For Loops
- [File 20: For Loops with Collections](#file-20-for-loops-with-collections)
- [File 21: Interactive Tuple and List Operations](#file-21-interactive-tuple-and-list-operations)
- [File 22: Range Function](#file-22-range-function)
- [File 23: Factorial Calculation](#file-23-factorial-calculation)

### Module 5: Advanced Concepts
- [File 24: Pattern Printing](#file-24-pattern-printing)

---

## Detailed Course Content

### File 1: Input and Comparison Operators

**Topics Covered:**
- Taking user input with `input()`
- Type conversion using `int()`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`

**Code Reference:**
```python
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
```

**Key Concepts:**
- Input always returns string, must convert to int for numbers
- Comparison operators return boolean values (True/False)
- Use == for equality, not single =

---

### File 2: Strings and String Methods

**Topics Covered:**
- String creation and manipulation
- String methods: `upper()`, `lower()`, `title()`, `capitalize()`
- String indexing and slicing
- Negative indexing

**Code Reference:**
```python
str1 = "ritesh chauhan"
print(str1.upper())        # RITESH CHAUHAN
print(str1[0])             # First character: 'r'
print(str1[0:6])           # Slice: 'ritesh'
print(str1[-7:])           # Negative index
```

**Key Concepts:**
- Strings are immutable (cannot be changed in place)
- Indexing starts at 0
- Slicing syntax: `[start:end]` (end is exclusive)
- Negative indices count from end of string

---

### File 3: Conditional Statements

**Topics Covered:**
- if, elif, else statements
- Nested conditionals
- Multiple conditions
- Boolean expressions
- Grade calculators and eligibility checks

**Code Reference:**
```python
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Multiple conditions
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
else:
    grade = "C"
```

**Key Concepts:**
- Use elif for multiple conditions
- Conditions are checked sequentially
- Only first matching condition executes
- Nested if statements for complex logic

---

### File 4: Lists and List Slicing

**Topics Covered:**
- List creation and accessing elements
- Mixed data type lists
- List mutability (can be changed)
- List slicing with various ranges

**Code Reference:**
```python
marks = [69, 66, 78, 65, 87, 89]
print(marks[0])      # First element
print(marks[1:4])    # Slice from index 1 to 3
print(marks[:4])     # From start to index 3
print(marks[2:])     # From index 2 to end

student = ["Name", 21, "India"]  # Mixed types
student[0] = "New Name"  # Modify element
```

**Key Concepts:**
- Lists are mutable, unlike tuples
- Can contain different data types
- Slicing creates new list
- Index out of range causes error

---

### File 5: List Operations and Methods

**Topics Covered:**
- List methods: `append()`, `insert()`, `remove()`, `pop()`
- Sorting: `sort()`, `reverse()`
- List manipulation and modification
- Counting occurrences with `count()`

**Code Reference:**
```python
list1 = [1, 3, 4, 5, 2]
list1.append(10)           # Add to end
list1.sort()               # Sort ascending
list1.sort(reverse=True)   # Sort descending
list1.insert(2, 0)         # Insert at index 2
list1.remove(0)            # Remove first occurrence
list1.pop(5)               # Remove at index 5
list1.count(1)             # Count occurrences
```

**Key Concepts:**
- append() adds to end, insert() adds at specific position
- sort() modifies list in place
- remove() deletes first occurrence of value
- pop() removes by index and returns value

---

### File 6: Tuples

**Topics Covered:**
- Tuple creation and immutability
- Accessing tuple elements
- Single element tuples
- Tuple methods: `index()`, `count()`
- Tuple vs List comparison

**Code Reference:**
```python
tup = (1, 2, 4, 3, 2, 4, 4, 1)
print(tup[1])              # Access by index
print(type(tup))           # <class 'tuple'>

tup1 = (1,)                # Single element tuple (comma required)
print(tup.index(4))        # Find index of 4
print(tup.count(2))        # Count occurrences of 2
```

**Key Concepts:**
- Tuples are immutable (cannot be changed)
- Single element tuples need trailing comma
- Faster than lists
- Use parentheses () instead of brackets []

---

### File 7: User Input for Lists

**Topics Covered:**
- Creating lists from user input
- Multiple input methods
- Using `append()` to build lists dynamically

**Code Reference:**
```python
# Method 1: Store in variables first
movie1 = input("Enter movie 1: ")
movie2 = input("Enter movie 2: ")
list1 = [movie1, movie2]

# Method 2: Append to empty list
movies = []
movies.append(input("Enter movie: "))
movies.append(input("Enter movie: "))
```

**Key Concepts:**
- Start with empty list []
- Use append() to add elements one by one
- Can use loops for multiple inputs
- input() always returns string

---

### File 8: List and Tuple Practice

**Topics Covered:**
- Palindrome list checking
- List copying with `copy()`
- Tuple to list conversion
- Counting elements in tuples
- Sorting lists

**Code Reference:**
```python
# Palindrome check
list1 = [1, 2, 3, 2, 1]
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("Palindrome")

# Count in tuple
grades = ("A", "B", "C", "A", "A")
print(grades.count("A"))

# Convert tuple to list and sort
list1 = list(grades)
list1.sort()
```

**Key Concepts:**
- Use copy() to avoid modifying original list
- Palindrome reads same forwards and backwards
- Convert tuple to list for sorting
- count() works on both lists and tuples

---

### File 9: Dictionaries

**Topics Covered:**
- Dictionary creation with key-value pairs
- Accessing values by key
- Nested dictionaries
- Dictionary methods: `keys()`, `values()`, `items()`
- Adding and updating dictionary entries

**Code Reference:**
```python
student = {
    "name": "Ritesh",
    "cgpa": 6.7,
    "marks": []
}
print(student["name"])

# Nested dictionary
student = {
    "name": "Ritesh",
    "subject": {
        "phy": 76,
        "chem": 67
    }
}
print(student["subject"]["phy"])

# Dictionary methods
print(student.keys())
print(student.values())
student.update({"city": "Bhubaneswar"})
```

**Key Concepts:**
- Dictionaries store key-value pairs
- Access values using keys in square brackets
- keys() returns all keys, values() returns all values
- update() adds or modifies multiple entries
- Nested dictionaries for complex data

---

### File 10: Sets

**Topics Covered:**
- Set creation and properties
- Automatic duplicate removal
- Set methods: `add()`, `pop()`, `clear()`
- Converting between sets and lists
- Unordered nature of sets

**Code Reference:**
```python
numbers = [1, 1, 2, 3, 4, 4, 5]
num_set = set(numbers)  # Removes duplicates
print(num_set)

num_set.add(11)         # Add element
num_set.pop()           # Remove random element
num_set.clear()         # Remove all elements

# Convert back to list
unique_list = list(num_set)
```

**Key Concepts:**
- Sets automatically remove duplicates
- Sets are unordered (no indexing)
- pop() removes random element (sets are unordered)
- Fast membership testing
- Use sets to find unique elements

---

### File 11: Set Operations

**Topics Covered:**
- Set union and intersection
- Mathematical set operations
- Combining multiple sets
- Dictionary with list and set values

**Code Reference:**
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))          # All unique elements
print(set1.intersection(set2))   # Common elements

# Dictionary with multiple values
words = {
    "table": ["furniture", "data table"],
    "cat": "animal"
}
```

**Key Concepts:**
- union() combines all unique elements
- intersection() returns only common elements
- difference() returns elements in one set but not other
- Sets useful for finding unique items in collections

---

### File 12: Dictionary from User Input

**Topics Covered:**
- Creating dictionaries from user input
- Using `update()` method
- Combining multiple dictionaries
- Processing dictionary values

**Code Reference:**
```python
a = int(input("Enter math marks: "))
b = int(input("Enter python marks: "))

marks_dict = {}
dict1 = {
    "math": a,
    "python": b
}
marks_dict.update(dict1)
print(marks_dict)
```

**Key Concepts:**
- Start with empty dictionary {}
- update() merges dictionaries
- Can add keys dynamically
- Access values using keys

---

### File 13: While Loop Basics

**Topics Covered:**
- While loop syntax and structure
- Counter variables
- Loop condition checking
- Incrementing counters with `+=`

**Code Reference:**
```python
count = 1
while count <= 5:
    print("Hello")
    count += 1

# Print numbers
a = 0
while a < 6:
    print(a)
    a = a + 1
```

**Key Concepts:**
- While loop continues until condition is False
- Must increment counter inside loop
- Forgetting to increment causes infinite loop
- Use while when number of iterations unknown

---

### File 14: Number Sequences

**Topics Covered:**
- Counting upward (1 to 100)
- Counting downward (100 to 1)
- Increment and decrement operations

**Code Reference:**
```python
# Count up
i = 1
while i <= 100:
    print(i)
    i = i + 1

# Count down
i = 100
while i >= 1:
    print(i)
    i = i - 1
```

**Key Concepts:**
- Increment: i = i + 1 or i += 1
- Decrement: i = i - 1 or i -= 1
- Change condition from <= to >= for countdown
- Initialize counter appropriately

---

### File 15: Multiplication Tables

**Topics Covered:**
- Generating multiplication tables
- User input for table number
- Formatted output
- Loop for repeated calculations

**Code Reference:**
```python
number = int(input("Enter number: "))
table = 1

while table <= 10:
    print(number, "x", table, "=", number * table)
    table += 1
```

**Key Concepts:**
- Loop from 1 to 10 for standard table
- Multiply number by counter in each iteration
- Format output for readability
- Can customize range for different tables

---

### File 16: Iterating Lists with While

**Topics Covered:**
- Looping through lists using index
- Using `len()` function
- Accessing elements by index in loop
- List traversal patterns

**Code Reference:**
```python
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(len(numbers))

i = 0
while i < len(numbers):
    element = numbers[i]
    print(element)
    i += 1
```

**Key Concepts:**
- Use len() to get list length
- Loop condition: i < len(list)
- Access element using list[i]
- Increment index to move to next element

---

### File 17: Searching in Tuples

**Topics Covered:**
- Linear search algorithm
- Searching for element in tuple
- Using found flag
- Breaking out of loop when found

**Code Reference:**
```python
tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number to search: "))

b = 0
found = False
while b < len(tuples):
    if tuples[b] == x:
        print("Found at index", b)
        found = True
        break
    b += 1

if not found:
    print("Not found")
```

**Key Concepts:**
- Linear search checks each element sequentially
- Use found flag to track if element was found
- break exits loop immediately
- Check found flag after loop completes

---

### File 18: Break and Continue

**Topics Covered:**
- break statement to exit loops
- continue statement to skip iterations
- Loop control flow
- Practical examples of both

**Code Reference:**
```python
# Break example
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

# Continue example
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
```

**Key Concepts:**
- break exits loop completely
- continue skips to next iteration
- Must increment before continue in while loops
- Use break when search is complete
- Use continue to skip unwanted values

---

### File 19: Odd and Even Numbers

**Topics Covered:**
- Modulo operator `%` for checking divisibility
- Filtering numbers using continue
- Printing odd and even numbers separately

**Code Reference:**
```python
# Print odd numbers
i = 0
while i <= 10:
    if i % 2 == 0:  # If even
        i += 1
        continue
    print(i)
    i += 1

# Print even numbers
i = 0
while i <= 10:
    if i % 2 != 0:  # If odd
        i += 1
        continue
    print(i)
    i += 1
```

**Key Concepts:**
- Modulo `%` returns remainder of division
- Even: number % 2 == 0
- Odd: number % 2 != 0 or number % 2 == 1
- Use continue to skip unwanted numbers

---

### File 20: For Loops with Collections

**Topics Covered:**
- For loop syntax
- Iterating through sets
- Automatic iteration over collections
- For vs while loops

**Code Reference:**
```python
num_set = {1, 2, 3, 4, 5}
for val in num_set:
    print(val)
```

**Key Concepts:**
- For loops iterate over collections automatically
- No need to manage index manually
- Works with lists, tuples, sets, strings
- More concise than while for known collections

---

### File 21: Interactive Tuple and List Operations

**Topics Covered:**
- Creating tuples from user input
- Using `split()` to parse input
- Using `strip()` to clean input
- Searching in tuples
- Creating lists from input

**Code Reference:**
```python
# Create tuple from input
tup_input = input("Enter items (comma-separated): ")
tup = tuple(tup_input.split(','))
for a in tup:
    print(a.strip())

# Search in tuple
search = input("Search for: ").strip()
if search in tup:
    print("Found")
else:
    print("Not found")

# Create list from input
list_input = input("Enter items: ")
num_list = list_input.split(',')
```

**Key Concepts:**
- split(',') divides string into list
- strip() removes leading/trailing spaces
- tuple() converts list to tuple
- in operator for membership testing

---

### File 22: Range Function

**Topics Covered:**
- range() function with different parameters
- range(stop), range(start, stop), range(start, stop, step)
- Even and odd number generation
- Counting forward and backward
- Multiplication tables with range

**Code Reference:**
```python
# range(stop)
for i in range(10):
    print(i)  # 0 to 9

# range(start, stop)
for i in range(2, 10):
    print(i)  # 2 to 9

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# Even numbers
for i in range(0, 101, 2):
    print(i)

# Countdown
for i in range(100, 0, -1):
    print(i)
```

**Key Concepts:**
- range(n) generates 0 to n-1
- stop value is exclusive (not included)
- step can be negative for countdown
- Use step=2 for even or odd numbers
- Very efficient for numeric sequences

---

### File 23: Factorial Calculation

**Topics Covered:**
- Calculating factorial using loops
- Accumulator pattern
- Multiplication in loops
- Mathematical operations

**Code Reference:**
```python
n = int(input("Enter number: "))
factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i += 1

print(factorial)
```

**Key Concepts:**
- Factorial: n! = n × (n-1) × ... × 2 × 1
- Start with 1 (not 0) for multiplication
- Multiply by each number from 1 to n
- Accumulator pattern: result = result * value

---

### File 24: Pattern Printing

**Topics Covered:**
- Printing star patterns
- String repetition with `*` operator
- Triangle patterns
- Pyramid patterns
- Nested loops for 2D patterns

**Code Reference:**
```python
# Right triangle
a = 5
for b in range(a):
    print("*" * b)

# Pattern with spaces
c = 5
for d in range(c):
    print(" " * c, "*" * d)
    c -= 1

# Pyramid
num = 5
for i in range(num):
    print(" " * (num - i), (2 * i - 1) * "*")
```

**Key Concepts:**
- String multiplication: "*" * 5 = "*****"
- Use spaces for alignment
- Calculate stars per row
- Pyramid uses odd numbers: 1, 3, 5, 7...
- Combine loops and string operations

---

## Additional Resources

### Summary File

**summary.py** - Contains all original code from files 1-24 with explanatory comments in a single file for quick reference.

### How to Use This Course

1. Start with File 1 and work sequentially through File 24
2. Read the code and comments carefully
3. Run each file to see output
4. Attempt the practice problems in each file
5. Experiment by modifying the code
6. Review the concept summaries at the end of each file

### Prerequisites

- Python 3.x installed
- Basic computer literacy
- Text editor or IDE (VS Code, PyCharm, etc.)
- No prior programming experience required

### Learning Path

**Week 1-2: Basics (Files 1-4)**
- Input/Output
- Strings
- Conditionals
- Lists

**Week 3-4: Data Structures (Files 5-12)**
- Lists and Tuples
- Dictionaries and Sets
- Data manipulation

**Week 5-6: Loops (Files 13-24)**
- While loops
- For loops
- Loop control
- Algorithms

### Tips for Success

- Practice daily for best results
- Type out code manually (don't just copy)
- Experiment with variations
- Read error messages carefully
- Review previous concepts regularly
- Build small projects combining multiple concepts

---

## File Structure

```
1.py  - Input and Comparison Operators
2.py  - Strings and String Methods
3.py  - Conditional Statements
4.py  - Lists and List Slicing
5.py  - List Operations and Methods
6.py  - Tuples
7.py  - User Input for Lists
8.py  - List and Tuple Practice
9.py  - Dictionaries
10.py - Sets
11.py - Set Operations
12.py - Dictionary from User Input
13.py - While Loop Basics
14.py - Number Sequences
15.py - Multiplication Tables
16.py - Iterating Lists with While
17.py - Searching in Tuples
18.py - Break and Continue
19.py - Odd and Even Numbers
20.py - For Loops with Collections
21.py - Interactive Tuple and List Operations
22.py - Range Function
23.py - Factorial Calculation
24.py - Pattern Printing
summary.py - Complete code compilation
```

---

## Concepts Quick Reference

### Basic Operations
- Input: `input()`, `int()`, `float()`
- Output: `print()`
- Operators: `+`, `-`, `*`, `/`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`

### Data Types
- Strings: Immutable text sequences
- Lists: Mutable ordered collections
- Tuples: Immutable ordered collections
- Dictionaries: Key-value pairs
- Sets: Unordered unique elements

### Control Flow
- Conditionals: `if`, `elif`, `else`
- While loops: Condition-based repetition
- For loops: Iteration over sequences
- Loop control: `break`, `continue`

### Common Methods

**String Methods:**
- `upper()`, `lower()`, `title()`, `capitalize()`
- `strip()`, `split()`, `replace()`

**List Methods:**
- `append()`, `insert()`, `remove()`, `pop()`
- `sort()`, `reverse()`, `count()`, `index()`

**Dictionary Methods:**
- `keys()`, `values()`, `items()`
- `update()`, `get()`, `pop()`

**Set Methods:**
- `add()`, `remove()`, `pop()`, `clear()`
- `union()`, `intersection()`, `difference()`

---

## Getting Started

1. Clone or download this repository
2. Open any Python file (start with 1.py)
3. Read the comments and code
4. Run the file: `python filename.py`
5. Complete the practice problems
6. Move to the next file

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This course material is free to use, modify, and distribute for educational and commercial purposes.

---

## Author

Ritesh Chauhan

---

## Acknowledgments

This course covers fundamental Python concepts with practical examples designed for hands-on learning.
