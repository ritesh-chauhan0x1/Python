# ===== FILE 9: Dictionaries - Key-Value Pairs =====
# Topic: Creating dictionaries, accessing values, nested dictionaries
# Concepts: Key-value pairs, .keys(), .values(), .items(), .update()

# ===== CREATING A DICTIONARY =====
# Dictionary stores data as key-value pairs
student_dict = {
    "name": "Ritesh",
    "cgpa": 6.7,
    "marks": [],  # Empty list as value
}

print("=== Simple Dictionary ===")
print("Full dictionary:", student_dict)
print("Accessing 'name':", student_dict["name"])

# ===== ADDING NEW KEY-VALUE PAIRS =====
# Add a new key after creation
student_dict["subject"] = ("Python", "Java")  # Tuple as value
print("After adding subject:", student_dict["subject"])

# ===== NESTED DICTIONARY =====
# Dictionary inside another dictionary
student = {
    "name": "Ritesh",
    "subject": {
        "phy": 76,
        "chem": 67,
        "math": 100
    }
}

print("\n=== Nested Dictionary ===")
print("Full nested dict:", student)
print("All subjects:", student["subject"])
print("Physics marks:", student["subject"]["phy"])  # Access nested value

# ===== DICTIONARY METHODS =====
print("\n=== Dictionary Methods ===")

# .keys() - returns all keys
print("Keys:", student.keys())  # dict_keys(['name', 'subject'])

# .values() - returns all values
print("Values:", student.values())

# .items() - returns key-value pairs as tuples
print("Items:", student.items())

# len() - number of key-value pairs
print("Length:", len(student))

# Access nested dictionary keys
print("Subject keys:", list(student["subject"]))

# Specific nested value
print("Physics marks:", student["subject"]["phy"])

# Convert to lists for iteration
print("\n=== Converting to Lists ===")
print("Keys as list:", list(student.keys()))
print("Values as list:", list(student.values()))
print("Items as list:", list(student.items()))
print("Dictionary length:", len(student))

# ===== UPDATING DICTIONARY =====
# .update() - add or modify multiple key-value pairs
student.update({"city": "Bhubaneswar"})
print("\nAfter update:", student)

# Update multiple at once
student.update({"age": 21, "country": "India"})
print("After multiple updates:", student)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Create student database
print("\n--- Practice: Student Database ---")
students_db = {
    "S001": {"name": "Alice", "grade": "A", "age": 20},
    "S002": {"name": "Bob", "grade": "B", "age": 21},
    "S003": {"name": "Charlie", "grade": "A", "age": 19}
}

# Access specific student
print("Student S002:", students_db["S002"])
print("Bob's grade:", students_db["S002"]["grade"])

# Add new student
students_db["S004"] = {"name": "Diana", "grade": "A", "age": 20}
print("Total students:", len(students_db))

# Problem 2: Phone book
print("\n--- Practice: Phone Book ---")
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}

# Search for a contact
name = "Bob"
if name in phonebook:
    print(f"{name}'s number: {phonebook[name]}")
else:
    print(f"{name} not found")

# Add new contact
phonebook["Diana"] = "456-789-0123"
print("Updated phonebook:", phonebook)

# Problem 3: Calculate total marks
print("\n--- Practice: Total Marks Calculator ---")
marks_dict = {
    "Math": 85,
    "Physics": 90,
    "Chemistry": 78,
    "English": 88,
    "Computer": 95
}

print("All subjects:", list(marks_dict.keys()))
print("All marks:", list(marks_dict.values()))

total = sum(marks_dict.values())
average = total / len(marks_dict)
print(f"Total marks: {total}")
print(f"Average: {average:.2f}")

# Find highest and lowest marks
print(f"Highest marks: {max(marks_dict.values())}")
print(f"Lowest marks: {min(marks_dict.values())}")

# Problem 4: Dictionary comprehension
print("\n--- Practice: Dictionary Comprehension ---")
# Create dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)

# Filter students with grade 'A'
students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}
a_students = {name: grade for name, grade in students.items() if grade == "A"}
print("A grade students:", a_students)

# Problem 5: Merge dictionaries
print("\n--- Practice: Merge Dictionaries ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: .update()
merged = dict1.copy()
merged.update(dict2)
print("Merged dict:", merged)

# Method 2: ** unpacking (Python 3.5+)
merged2 = {**dict1, **dict2}
print("Merged using **:", merged2)

# DICTIONARY METHODS SUMMARY:
# .get(key)           - Get value (returns None if not found)
# .keys()             - Get all keys
# .values()           - Get all values
# .items()            - Get all key-value pairs
# .update(dict)       - Add/update multiple items
# .pop(key)           - Remove and return value
# .clear()            - Remove all items
# key in dict         - Check if key exists
# dict[key] = value   - Add or update item
