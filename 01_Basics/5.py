# ===== FILE 5: Lists - Operations and Methods =====
# Topic: List manipulation, sorting, adding/removing elements
# Concepts: Lists are mutable (can be changed), list methods

# Creating a list with duplicate values
my_list = [1, 3, 4, 5, 2, 5, 6, 6, 1]
print("Original list:", my_list)

# ===== ADDING ELEMENTS =====
# .append() - adds element at the end
my_list.append(10)
print("After append(10):", my_list)

# ===== SORTING =====
# .sort() - arranges in ascending order (modifies original list)
my_list.sort()
print("After sort():", my_list)

# .sort(reverse=True) - descending order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# Adding more elements
my_list.append(11)
my_list.append(15)
print("After adding 11 and 15:", my_list)

# .reverse() - reverses the list order
my_list.reverse()
print("After reverse():", my_list)

my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# .insert(index, element) - inserts element at specific position
my_list.insert(2, 0)  # Insert 0 at index 2
print("After insert(2, 0):", my_list)

# ===== REMOVING ELEMENTS =====
# .remove(element) - removes first occurrence of element
my_list.remove(0)
print("After remove(0):", my_list)

# .pop(index) - removes and returns element at index
removed = my_list.pop(5)  # Removes element at index 5
print("After pop(5), removed:", removed)
print("List now:", my_list)

my_list.sort()
print("Final sorted list:", my_list)

# .count(element) - counts how many times element appears
print("Count of 1:", my_list.count(1))
print("Count of 5:", my_list.count(5))

# ===== PRACTICE QUESTIONS =====

print("\n--- Practice: Create your own list ---")
# Problem 1: Create list from user input
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)  # Add each number to list

print("Your list:", numbers)
print("Sorted list:", sorted(numbers))  # sorted() returns new sorted list
print("Original unchanged:", numbers)  # Original list not modified

# Problem 2: List operations
print("\n--- Practice: List statistics ---")
if len(numbers) > 0:
    print("Largest number:", max(numbers))  # max() finds largest
    print("Smallest number:", min(numbers))  # min() finds smallest
    print("Sum of numbers:", sum(numbers))  # sum() adds all elements
    print("Average:", sum(numbers) / len(numbers))

# Problem 3: List slicing
print("\n--- Practice: List slicing ---")
sample = [10, 20, 30, 40, 50, 60, 70, 80]
print("Full list:", sample)
print("First 3 elements:", sample[0:3])  # or sample[:3]
print("Last 3 elements:", sample[-3:])
print("Every 2nd element:", sample[::2])  # [start:end:step]
print("Reversed list:", sample[::-1])  # Reverse using slicing

# LIST METHODS SUMMARY:
# .append(x)    - Add x to end
# .extend(list) - Add multiple elements
# .insert(i, x) - Add x at index i
# .remove(x)    - Remove first x
# .pop(i)       - Remove and return element at index i
# .clear()      - Remove all elements
# .sort()       - Sort list in place
# .reverse()    - Reverse list in place
# .count(x)     - Count occurrences of x
# .index(x)     - Find index of first x
