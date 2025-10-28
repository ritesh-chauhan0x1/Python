# ===== FILE 7: User Input Lists =====
# Topic: Building lists from user input
# Concepts: input(), append(), creating empty lists

# ===== METHOD 1: Create variables then make list =====
print("=== Method 1: Variables to List ===")
movie1 = input("Enter your 1st favorite movie: ")
movie2 = input("Enter your 2nd favorite movie: ")
movie3 = input("Enter your 3rd favorite movie: ")

# Store in list
movie_list = [movie1, movie2, movie3]
print("Type:", type(movie_list))  # <class 'list'>
print("Your movies:", movie_list)

# ===== METHOD 2: Append to empty list =====
print("\n=== Method 2: Append to Empty List ===")
movies = []  # Start with empty list
movies.append(input("Enter your 1st movie: "))
movies.append(input("Enter your 2nd movie: "))
movies.append(input("Enter your 3rd movie: "))
print("Your movies:", movies)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Dynamic list with loop
print("\n--- Practice: Build List with Loop ---")
count = int(input("How many movies to add? "))
movie_collection = []

for i in range(count):
    movie = input(f"Enter movie {i+1}: ")
    movie_collection.append(movie)

print(f"\nYou entered {len(movie_collection)} movies:")
for idx, movie in enumerate(movie_collection, 1):
    print(f"{idx}. {movie}")

# Problem 2: Numbers list from input
print("\n--- Practice: List of Numbers ---")
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

print("\nYour numbers:", numbers)
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Problem 3: Single line input to list
print("\n--- Practice: Split Input into List ---")
text = input("Enter multiple items separated by commas: ")
items = text.split(",")  # Split string by comma
items = [item.strip() for item in items]  # Remove extra spaces
print("Your items:", items)

# Problem 4: Shopping cart
print("\n--- Practice: Shopping Cart ---")
cart = []
while True:
    item = input("Add item to cart (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    cart.append(item)

print("\nYour shopping cart:")
for i, item in enumerate(cart, 1):
    print(f"{i}. {item}")
print(f"Total items: {len(cart)}")

# Problem 5: Filter list based on criteria
print("\n--- Practice: Student Names Starting with 'A' ---")
students = []
print("Enter 5 student names:")
for i in range(5):
    name = input(f"Student {i+1}: ")
    students.append(name)

# Filter names starting with 'A'
a_names = [name for name in students if name.upper().startswith('A')]
print("\nAll students:", students)
print("Students starting with 'A':", a_names)

# USEFUL METHODS FOR USER INPUT LISTS:
# .append(item)      - Add item to end of list
# .insert(idx, item) - Add item at specific index
# .extend(list)      - Add multiple items from another list
# .split(",")        - Convert string to list (split by delimiter)
# input().split()    - Get multiple inputs separated by space