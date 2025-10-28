# ===== FILE 30: File I/O - Processing CSV Data =====
# Topic: Reading and processing comma-separated values
# Concepts: split(), type conversion, filtering data, list operations

# ORIGINAL CODE - Working with CSV data

# Step 1: Create a file with comma-separated numbers
with open("pratice1.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,99,11,12,13,23,24,35,354,646,5,57,345,32323,523,5,235")

# Step 2: Read the data from file
with open("pratice1.txt", "r") as f:
    data = f.read()

# Step 3: Split the string by commas into a list
new_data = data.split(",")
print(new_data)  # Still strings at this point

# Step 4: Convert all strings to integers
new_data1 = []
for item in new_data:
    a = int(item)
    new_data1.append(a)
print(new_data1)  # Now integers

# Step 5: Separate even and odd numbers
even = []
odd = []
for item in new_data1:
    if (item % 2 == 0):
        even.append(item)
    else:
        odd.append(item)

print("Even numbers:", even)
print("Odd numbers:", odd)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Count even and odd numbers
print("\n--- Problem 1: Count even and odd ---")
print(f"Total even numbers: {len(even)}")
print(f"Total odd numbers: {len(odd)}")

# Problem 2: Find sum of all even numbers
print("\n--- Problem 2: Sum of even numbers ---")
sum_even = sum(even)
print(f"Sum of even numbers: {sum_even}")

# Problem 3: Find largest and smallest numbers
print("\n--- Problem 3: Max and Min ---")
print(f"Largest number: {max(new_data1)}")
print(f"Smallest number: {min(new_data1)}")

# Problem 4: Calculate average of all numbers
print("\n--- Problem 4: Average ---")
average = sum(new_data1) / len(new_data1)
print(f"Average: {average:.2f}")

# Problem 5: Find numbers greater than 100
print("\n--- Problem 5: Numbers > 100 ---")
large_numbers = [num for num in new_data1 if num > 100]
print(f"Numbers greater than 100: {large_numbers}")

# Problem 6: Remove duplicates
print("\n--- Problem 6: Unique numbers ---")
unique_numbers = list(set(new_data1))
unique_numbers.sort()
print(f"Unique numbers: {unique_numbers}")

# Problem 7: Process a CSV file with multiple columns
print("\n--- Problem 7: Multi-column CSV ---")
csv_data = "John,25,Math\nAlice,22,Science\nBob,24,History"
with open("students.txt", "w") as f:
    f.write(csv_data)

students = []
with open("students.txt", "r") as f:
    for line in f:
        name, age, subject = line.strip().split(",")
        students.append({
            "name": name,
            "age": int(age),
            "subject": subject
        })

for student in students:
    print(f"{student['name']}: {student['age']} years, studies {student['subject']}")

# Problem 8: Write filtered data to new file
print("\n--- Problem 8: Write even numbers to file ---")
with open("even_numbers.txt", "w") as f:
    for num in even:
        f.write(str(num) + "\n")
print("Even numbers written to even_numbers.txt")

# Problem 9: Count occurrences of each number
print("\n--- Problem 9: Number frequency ---")
from collections import Counter
frequency = Counter(new_data1)
print("Number frequencies:")
for num, count in frequency.most_common(5):
    print(f"{num} appears {count} times")

# Problem 10: Find numbers divisible by 5
print("\n--- Problem 10: Divisible by 5 ---")
div_by_5 = [num for num in new_data1 if num % 5 == 0]
print(f"Numbers divisible by 5: {div_by_5}")

# CONCEPT SUMMARY:
# - split() converts string to list using delimiter
# - Type conversion: int(), float(), str()
# - List comprehension: [x for x in list if condition]
# - set() removes duplicates
# - Counter helps count occurrences
# - CSV format: Comma-Separated Values
# - strip() removes whitespace from strings
# - Always convert data types when processing files

