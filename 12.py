# ===== FILE 12: Dictionary Update Method =====
# Topic: Creating and updating dictionaries
# Concepts: Empty dict, .update(), combining dictionaries

# ===== GETTING USER INPUT =====
print("=== Student Marks Entry ===")
a = int(input("Enter marks of Math: "))
b = int(input("Enter marks of Python: "))
c = int(input("Enter marks of JavaScript: "))

# ===== CREATING DICTIONARIES =====
# Empty dictionary
dict = {}

# Dictionary with marks
dict1 = {
    "math": a,
    "python": b,  # Note: Fixed typo from "pyhton"
    "javascript": c,
}

# ===== UPDATE METHOD =====
# .update() adds dict1 items to dict
# Returns None (not the dictionary)
dict.update(dict1)
print("\nUpdated dictionary:", dict)

# Calculate total and average
total = sum(dict.values())
average = total / len(dict)
print(f"Total marks: {total}")
print(f"Average: {average:.2f}")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Build dictionary gradually
print("\n--- Practice: Step-by-Step Dictionary ---")
student = {}
student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["grade"] = input("Enter grade: ")
print("Student:", student)

# Problem 2: Merge multiple dictionaries
print("\n--- Practice: Merge Dictionaries ---")
personal = {"name": "Alice", "age": 20}
academic = {"grade": "A", "gpa": 3.8}
contact = {"email": "alice@example.com", "phone": "123-456-7890"}

# Merge all into one
complete = {}
complete.update(personal)
complete.update(academic)
complete.update(contact)
print("Complete record:", complete)

# Problem 3: Update existing values
print("\n--- Practice: Update Values ---")
scores = {"math": 85, "science": 90}
print("Original scores:", scores)

# Update with new values
new_scores = {"math": 95, "english": 88}  # math will be updated
scores.update(new_scores)
print("Updated scores:", scores)

# Problem 4: Alternative merge methods
print("\n--- Practice: Different Merge Methods ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: .update()
merged1 = dict1.copy()
merged1.update(dict2)
print("Using .update():", merged1)

# Method 2: ** unpacking (Python 3.5+)
merged2 = {**dict1, **dict2}
print("Using ** unpacking:", merged2)

# Method 3: | operator (Python 3.9+)
merged3 = dict1 | dict2
print("Using | operator:", merged3)

# Problem 5: Conditional update
print("\n--- Practice: Conditional Update ---")
existing = {"math": 85, "science": 90}
new_data = {"math": 75, "english": 88}  # math is lower

print("Existing:", existing)
print("New data:", new_data)

# Update only if new value is higher
for key, value in new_data.items():
    if key not in existing or value > existing[key]:
        existing[key] = value

print("After conditional update:", existing)

# Problem 6: Update with user choice
print("\n--- Practice: Interactive Update ---")
inventory = {"apples": 50, "bananas": 30, "oranges": 40}
print("Current inventory:", inventory)

item = input("Item to update: ")
if item in inventory:
    quantity = int(input(f"New quantity for {item}: "))
    inventory[item] = quantity
else:
    add = input(f"{item} not in inventory. Add it? (yes/no): ")
    if add.lower() == "yes":
        quantity = int(input(f"Quantity for {item}: "))
        inventory[item] = quantity

print("Updated inventory:", inventory)

# Problem 7: Bulk update from input
print("\n--- Practice: Bulk Update ---")
subjects = {}
num_subjects = int(input("How many subjects? "))

for i in range(num_subjects):
    subject = input(f"Subject {i+1} name: ")
    marks = int(input(f"Marks for {subject}: "))
    subjects[subject] = marks

print("\nAll subjects:", subjects)
print(f"Total: {sum(subjects.values())}")
print(f"Average: {sum(subjects.values()) / len(subjects):.2f}")

# Problem 8: Update with default values
print("\n--- Practice: setdefault() Method ---")
config = {"theme": "dark", "font": "Arial"}
print("Original config:", config)

# setdefault adds key only if it doesn't exist
config.setdefault("font_size", 12)  # Added
config.setdefault("theme", "light")  # NOT changed (already exists)
print("After setdefault:", config)

# DICTIONARY UPDATE METHODS:
#
# .update(dict):
# • Adds all key-value pairs from dict
# • Overwrites existing keys
# • Returns None (modifies in place)
#
# .setdefault(key, default):
# • Adds key with default value if key doesn't exist
# • Returns value (existing or new)
# • Doesn't overwrite existing keys
#
# dict1 | dict2 (Python 3.9+):
# • Creates NEW dictionary
# • Combines both dictionaries
# • dict2 values overwrite dict1 if keys match
#
# {**dict1, **dict2}:
# • Dictionary unpacking
# • Creates NEW dictionary
# • Works in Python 3.5+
#
# IMPORTANT NOTES:
# • .update() returns None, not the dictionary
# • Use dict.update() on separate line, then print(dict)
# • For creating new combined dict, use | or **
# • To preserve original, use .copy() first