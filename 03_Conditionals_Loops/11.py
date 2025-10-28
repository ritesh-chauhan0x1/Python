# ===== FILE 11: Set Operations & Dictionary Practice =====
# Topic: Union, intersection, dictionary with multiple values
# Concepts: Mathematical set operations, storing lists in dictionaries

# ===== SET OPERATIONS =====
print("=== Set Union and Intersection ===")
set1 = {1, 2, 3, 4, 5, 6, 7}  # Duplicates automatically removed
set2 = {0, 2, 3, 4, 5, 8, 9, 10, 11}

print("Set 1:", set1)
print("Set 2:", set2)

# .union() - combines all unique elements from both sets
union_result = set1.union(set2)
print("Union:", union_result)
# Alternative: set1 | set2

# .intersection() - elements common to both sets
intersection_result = set1.intersection(set2)
print("Intersection:", intersection_result)
# Alternative: set1 & set2

# ===== DICTIONARY WITH MULTIPLE DEFINITIONS =====
print("\n=== Dictionary - Multiple Meanings ===")

# Method 1: Using set (unordered, but values are unique)
words = {
    "table": {
        "a piece of furniture",
        "list of facts & figures"
    },
    "cat": "animals",
}
print("Dictionary with set:", words)

# Method 2: Using list (ordered, can have duplicates)
word_dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "animals",
}
print("Dictionary with list:", word_dict)

# Access definitions
print("\nMeanings of 'table':", word_dict["table"])
print("First meaning:", word_dict["table"][0])

# ===== PRACTICAL EXAMPLE =====
print("\n=== Classroom Allocation ===")
# Sets automatically remove duplicate subjects
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print("All subjects (with duplicates removed):", subjects)
print("Classrooms needed:", len(subjects))

# ===== PRACTICE QUESTIONS =====

# Problem 1: More set operations
print("\n--- Practice: Advanced Set Operations ---")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)
print("Union (A ∪ B):", A.union(B))
print("Intersection (A ∩ B):", A.intersection(B))
print("Difference (A - B):", A.difference(B))  # In A but not in B
print("Difference (B - A):", B.difference(A))  # In B but not in A
print("Symmetric Difference (A △ B):", A.symmetric_difference(B))  # In A or B, not both

# Problem 2: English dictionary
print("\n--- Practice: Complete Dictionary ---")
dictionary = {
    "python": [
        "a programming language",
        "a large snake"
    ],
    "mouse": [
        "a small rodent",
        "a computer input device"
    ],
    "date": [
        "a day of the month",
        "a sweet fruit",
        "a social appointment"
    ]
}

# Look up word
word_to_find = "python"
print(f"\nDefinitions of '{word_to_find}':")
for i, definition in enumerate(dictionary[word_to_find], 1):
    print(f"  {i}. {definition}")

# Problem 3: Student course enrollment
print("\n--- Practice: Course Enrollment ---")
semester1 = {"Math", "Physics", "English", "Chemistry"}
semester2 = {"Physics", "Computer", "English", "Biology"}

print("Semester 1 courses:", semester1)
print("Semester 2 courses:", semester2)

# Common courses
common = semester1 & semester2
print("Common courses:", common)

# All unique courses
all_courses = semester1 | semester2
print("All unique courses:", all_courses)

# Only in semester 1
only_sem1 = semester1 - semester2
print("Only in semester 1:", only_sem1)

# Problem 4: Email domain analysis
print("\n--- Practice: Email Domains ---")
emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "charlie@gmail.com",
    "diana@outlook.com",
    "eve@gmail.com",
    "frank@yahoo.com"
]

# Extract unique domains
domains = {email.split('@')[1] for email in emails}
print("Emails:", emails)
print("Unique domains:", domains)
print("Number of domains:", len(domains))

# Count emails per domain
print("\nEmails per domain:")
for domain in domains:
    count = sum(1 for email in emails if domain in email)
    print(f"  {domain}: {count}")

# Problem 5: Compare two lists
print("\n--- Practice: List Comparison ---")
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

set_a = set(list_a)
set_b = set(list_b)

print("List A:", list_a)
print("List B:", list_b)
print("Common elements:", set_a & set_b)
print("Unique to A:", set_a - set_b)
print("Unique to B:", set_b - set_a)
print("All unique elements:", set_a | set_b)

# SET OPERATIONS SUMMARY:
# .union(set2)              - All elements from both sets (|)
# .intersection(set2)       - Common elements (&)
# .difference(set2)         - Elements in set1 but not set2 (-)
# .symmetric_difference(set2) - Elements in either set, not both (^)
# .issubset(set2)           - Check if all elements are in set2
# .issuperset(set2)         - Check if contains all elements of set2
# .isdisjoint(set2)         - Check if no common elements