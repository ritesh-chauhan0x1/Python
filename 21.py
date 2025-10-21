# ===== FILE 21: Interactive Tuple and List Operations =====
# Topic: User input for tuple and list, string methods, searching
# Concepts: .split(), .strip(), tuple creation, 'in' operator

# ===== CREATE TUPLE FROM USER INPUT =====
print("=== Create Tuple from Input ===")
tup_input = input("Enter elements for tuple (comma-separated): ")
# split(',') converts string to list, then tuple() converts to tuple
tup = tuple(tup_input.split(','))

print("\nTuple elements:")
for a in tup:
    print(a.strip())  # .strip() removes leading/trailing spaces

# ===== SEARCH IN TUPLE =====
print("\n=== Search in Tuple ===")
search_element = input("Enter an element to find in the tuple: ").strip()

# Use 'in' operator for membership test
if search_element in tup:
    print("Element Found")
    # Find position
    # Need to check stripped versions
    for i, elem in enumerate(tup):
        if elem.strip() == search_element:
            print(f"Position: {i}")
            break
else:
    print("Not Found")

print()  # Empty line for spacing

# ===== CREATE LIST FROM USER INPUT =====
print("=== Create List from Input ===")
list_input = input("Enter elements for list (comma-separated): ")
num = list_input.split(',')  # Creates a list

print("\nList elements:")
for element in num:
    print(element.strip())

# ===== PRACTICE QUESTIONS =====

# Problem 1: Numeric tuple from input
print("\n--- Practice: Numeric Tuple ---")
num_input = input("Enter numbers (space-separated): ")
num_tuple = tuple(map(int, num_input.split()))  # Convert to integers
print("Tuple:", num_tuple)
print("Sum:", sum(num_tuple))
print("Average:", sum(num_tuple) / len(num_tuple))

# Problem 2: List with type conversion
print("\n--- Practice: Integer List ---")
str_input = input("Enter integers (comma-separated): ")
int_list = [int(x.strip()) for x in str_input.split(',')]
print("List:", int_list)
print("Maximum:", max(int_list))
print("Minimum:", min(int_list))

# Problem 3: Multiple operations on tuple
print("\n--- Practice: Tuple Operations Menu ---")
input_str = input("Enter words (space-separated): ")
word_tuple = tuple(input_str.split())

print("\nTuple:", word_tuple)
print("Length:", len(word_tuple))
print("First element:", word_tuple[0])
print("Last element:", word_tuple[-1])

# Search
search = input("Search for word: ")
if search in word_tuple:
    print(f"'{search}' found at index {word_tuple.index(search)}")
    print(f"Appears {word_tuple.count(search)} times")
else:
    print(f"'{search}' not found")

# Problem 4: Clean and process input
print("\n--- Practice: Clean Input ---")
messy_input = input("Enter items (any separator): ")
# Replace multiple separators with comma
clean = messy_input.replace(';', ',').replace('|', ',')
items = [item.strip() for item in clean.split(',') if item.strip()]
print("Cleaned items:", items)

# Problem 5: Tuple unpacking from input
print("\n--- Practice: Tuple Unpacking ---")
data = input("Enter name, age, city (comma-separated): ")
parts = data.split(',')
if len(parts) == 3:
    name, age, city = [p.strip() for p in parts]
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
else:
    print("Please enter exactly 3 values")

# Problem 6: Filter and create tuple
print("\n--- Practice: Filter Input ---")
numbers_str = input("Enter numbers (space-separated): ")
numbers = [int(x) for x in numbers_str.split()]

# Create tuples for even and odd
even_tuple = tuple(x for x in numbers if x % 2 == 0)
odd_tuple = tuple(x for x in numbers if x % 2 != 0)

print("Even numbers:", even_tuple)
print("Odd numbers:", odd_tuple)

# Problem 7: Multiple search
print("\n--- Practice: Multiple Searches ---")
data_str = input("Enter data items (comma-separated): ")
data = tuple(data_str.split(','))

while True:
    search = input("Search for (or 'quit'): ").strip()
    if search.lower() == 'quit':
        break
    
    count = 0
    positions = []
    for i, item in enumerate(data):
        if item.strip() == search:
            count += 1
            positions.append(i)
    
    if count > 0:
        print(f"Found {count} time(s) at positions: {positions}")
    else:
        print("Not found")

# Problem 8: Build list interactively
print("\n--- Practice: Interactive List Building ---")
my_list = []
print("Enter items (type 'done' to finish):")

while True:
    item = input("Item: ")
    if item.lower() == 'done':
        break
    my_list.append(item)

print("\nYour list:", my_list)
print("As tuple:", tuple(my_list))

# STRING METHODS USED:
# • .split(separator) - Split string into list
# • .strip() - Remove leading/trailing whitespace
# • .replace(old, new) - Replace substring
# • .lower() - Convert to lowercase
# • .upper() - Convert to uppercase
# • .join(iterable) - Join list into string
#
# INPUT PROCESSING PATTERNS:
#
# Comma-separated to list:
#   items = input().split(',')
#
# Space-separated to tuple:
#   items = tuple(input().split())
#
# Convert to integers:
#   numbers = [int(x) for x in input().split()]
#   # or
#   numbers = list(map(int, input().split()))
#
# Clean input:
#   cleaned = [x.strip() for x in input().split(',')]
#
# MEMBERSHIP TESTING:
# • 'element in collection' - Fast, pythonic
# • .index(element) - Returns position, raises error if not found
# • .count(element) - Returns number of occurrences
#
# BEST PRACTICES:
# • Always .strip() user input to remove extra spaces
# • Use .lower() for case-insensitive comparison
# • Validate input length before unpacking
# • Use list comprehension for filtering/transforming
# • Handle errors with try-except for conversions