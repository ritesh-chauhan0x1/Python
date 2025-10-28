# ===== FILE 10: Sets - Unique Collections =====
# Topic: Creating sets, removing duplicates, set operations
# Concepts: Unordered collection, no duplicates, .pop(), .add(), .clear()

# ===== CREATING A SET FROM LIST =====
# Sets automatically remove duplicate values
num = [1, 1, 2, 3, 4, 4, 5, 4, 3, 2, 5, 6, 7, 8, 1, 1, 9, 10, 9, 9, 9, 10]
print("Original list:", num)
print("List length:", len(num))

# Convert list to set (removes duplicates)
num_set = set(num)
print("\nType:", type(num_set), "Value:", num_set)
# Note: Sets are unordered, elements may appear in any order

# ===== CONVERTING BACK TO LIST =====
unique_list = list(num_set)
print("Type:", type(unique_list), "Value:", unique_list)
print("Unique elements count:", len(unique_list))

# ===== SET OPERATIONS =====
print("\n=== Set Operations ===")

# .pop() - removes and returns a random element
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())

# .add() - adds an element to set
num_set.add(11)
print("After adding 11, popped:", num_set.pop())

num_set.add(22)
print("After adding 22, popped:", num_set.pop())

num_set.add(9)
print("After adding 9, popped:", num_set.pop())

num_set.add(3)
print("After adding 3:", num_set)

# Remove more elements
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())
print("Popped:", num_set.pop())

# .clear() - removes all elements
num_set.clear()
print("After clear:", num_set)  # set()

# ===== PRACTICE QUESTIONS =====

# Problem 1: Remove duplicates from user input
print("\n--- Practice: Remove Duplicates ---")
numbers = [5, 2, 8, 2, 9, 5, 1, 8, 3, 5]
print("Original list:", numbers)
print("Length:", len(numbers))

unique = list(set(numbers))
unique.sort()  # Sort for better readability
print("Unique values:", unique)
print("Unique count:", len(unique))
print("Duplicates removed:", len(numbers) - len(unique))

# Problem 2: Set operations
print("\n--- Practice: Basic Set Operations ---")
fruits = {"apple", "banana", "cherry"}
print("Initial set:", fruits)

# Add element
fruits.add("orange")
print("After adding orange:", fruits)

# Add duplicate (no effect)
fruits.add("apple")
print("After adding apple again:", fruits)  # No change

# Remove specific element
fruits.remove("banana")
print("After removing banana:", fruits)

# Discard (won't error if not found)
fruits.discard("grape")  # No error even though grape not in set
print("After discard grape:", fruits)

# Problem 3: Check membership
print("\n--- Practice: Set Membership ---")
vowels = {'a', 'e', 'i', 'o', 'u'}
letter = 'a'

if letter in vowels:
    print(f"'{letter}' is a vowel")
else:
    print(f"'{letter}' is not a vowel")

# Check multiple letters
word = "hello"
word_vowels = {char for char in word if char in vowels}
print(f"Vowels in '{word}':", word_vowels)

# Problem 4: Set from string
print("\n--- Practice: Unique Characters in String ---")
text = "hello world"
unique_chars = set(text)
print(f"Text: '{text}'")
print("Unique characters:", unique_chars)
print("Unique count:", len(unique_chars))

# Remove space
unique_chars.discard(' ')
print("Without space:", unique_chars)

# Problem 5: Find common elements
print("\n--- Practice: Common Elements ---")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert to sets and find intersection
set1 = set(list1)
set2 = set(list2)
common = set1 & set2  # Or set1.intersection(set2)
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)

# SET METHODS SUMMARY:
# .add(element)        - Add element to set
# .remove(element)     - Remove element (error if not found)
# .discard(element)    - Remove element (no error if not found)
# .pop()               - Remove and return random element
# .clear()             - Remove all elements
# .copy()              - Return a copy of set
# element in set       - Check membership
# len(set)             - Number of elements
# .update(iterable)    - Add multiple elements

# KEY FEATURES OF SETS:
# 1. No duplicate elements
# 2. Unordered (no indexing)
# 3. Mutable (can add/remove)
# 4. Fast membership testing
# 5. Mathematical set operations (union, intersection, etc.)