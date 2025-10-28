# ===== FILE 2: Strings & String Methods =====
# Topic: Working with strings, string length, and string methods
# Concepts: len(), .count(), string indexing, string methods

# Problem 1: Find length of a string
print("--- Problem 1: String length ---")
name = input("Enter your first name: ")
print("Your name has", len(name), "characters")  # len() returns number of characters

# Problem 2: Count specific characters in a string
print("\n--- Problem 2: Count characters ---")
text = "hi i am $ the $100"
print("Text:", text)
print("Number of '$' symbols:", text.count("$"))  # .count() finds occurrences
print("Number of spaces:", text.count(" "))
print("Number of 'i' letters:", text.count("i"))

# ===== PRACTICE QUESTIONS =====

# Problem 3: String indexing and slicing
print("\n--- Problem 3: String indexing ---")
word = input("Enter a word: ")
if len(word) > 0:
    print("First character:", word[0])  # Index starts at 0
    print("Last character:", word[-1])  # Negative index from end
    if len(word) >= 3:
        print("First 3 characters:", word[0:3])  # Slicing: [start:end]
        print("Last 3 characters:", word[-3:])

# Problem 4: More string methods
print("\n--- Problem 4: String methods ---")
sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())  # Convert to uppercase
print("Lowercase:", sentence.lower())  # Convert to lowercase
print("Title Case:", sentence.title())  # Capitalize each word
print("Count of 'a':", sentence.lower().count('a'))  # Case-insensitive count

# Problem 5: String operations
print("\n--- Problem 5: String operations ---")
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
combined = word1 + " " + word2  # Concatenation (joining strings)
print("Combined:", combined)
print("Repeated 3 times:", word1 * 3)  # String multiplication
print("Is word1 in combined?", word1 in combined)  # Membership test

# USEFUL STRING METHODS:
# .upper()     - Convert to uppercase
# .lower()     - Convert to lowercase
# .title()     - Capitalize first letter of each word
# .count(x)    - Count occurrences of x
# .replace(old, new) - Replace text
# .strip()     - Remove whitespace from ends
# .split()     - Split into list