# ===== FILE 18: Break and Continue Statements =====
# Topic: Loop control with break and continue
# Concepts: Exit loop early (break), skip iteration (continue)

# ===== BREAK STATEMENT =====
# break: Exits the loop immediately
print("=== Break Statement ===")
i = 1
while i <= 5:
    print(i)
    if i == 3:  # When i equals 3
        break  # Exit loop immediately
    i += 1
print("End of loop")
# Output: 1, 2, 3 (loop stops at 3)

# ===== CONTINUE STATEMENT =====
# continue: Skips rest of current iteration, goes to next
print("\n=== Continue Statement ===")
i = 1
while i <= 5:
    if i == 3:  # When i equals 3
        i += 1  # IMPORTANT: Increment before continue
        continue  # Skip print, go to next iteration
    print(i)
    i += 1
# Output: 1, 2, 4, 5 (skips printing 3)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Find first divisible number
print("\n--- Practice: Break When Found ---")
number = 1
while number <= 100:
    if number % 13 == 0:
        print(f"First number divisible by 13: {number}")
        break
    number += 1

# Problem 2: Skip negative numbers
print("\n--- Practice: Continue to Skip ---")
numbers = [5, -3, 8, -1, 10, -7, 15]
print("Original list:", numbers)
print("Positive numbers only:")

i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue  # Skip negative numbers
    print(numbers[i], end=" ")
    i += 1
print()

# Problem 3: Password checker with limited attempts
print("\n--- Practice: Break on Success ---")
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1
    
    if password == correct_password:
        print("Login successful!")
        break
    else:
        if attempts < 3:
            print(f"Wrong! {3 - attempts} attempts left")
        else:
            print("Account locked!")

# Problem 4: Skip multiples of 5
print("\n--- Practice: Skip Multiples of 5 ---")
num = 1
print("Numbers 1-20 (except multiples of 5):")
while num <= 20:
    if num % 5 == 0:
        num += 1
        continue
    print(num, end=" ")
    num += 1
print()

# Problem 5: Search and break
print("\n--- Practice: Search in List ---")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search_fruit = "cherry"

i = 0
while i < len(fruits):
    if fruits[i] == search_fruit:
        print(f"Found '{search_fruit}' at position {i}")
        break
    i += 1
else:  # Executes if loop completes without break
    print(f"'{search_fruit}' not found")

# Problem 6: Sum until condition
print("\n--- Practice: Sum Until Exceeds 100 ---")
total = 0
num = 1
while True:  # Infinite loop
    total += num
    if total > 100:
        print(f"Sum exceeded 100 at number {num}")
        print(f"Final sum: {total}")
        break
    num += 1

# Problem 7: Skip vowels
print("\n--- Practice: Print Consonants Only ---")
word = "programming"
print(f"Word: {word}")
print("Consonants:", end=" ")

i = 0
vowels = "aeiou"
while i < len(word):
    if word[i] in vowels:
        i += 1
        continue
    print(word[i], end="")
    i += 1
print()

# Problem 8: Break on user input
print("\n--- Practice: Interactive Loop ---")
count = 0
while True:
    user_input = input("Type 'quit' to exit or press Enter: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    count += 1
    print(f"You've entered {count} times")

# Problem 9: Skip even, break at 15
print("\n--- Practice: Combined break and continue ---")
i = 1
print("Odd numbers until 15:")
while i <= 20:
    if i > 15:
        print("\nStopped at 15")
        break
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1

# Problem 10: Validate input with continue
print("\n\n--- Practice: Input Validation ---")
valid_numbers = []
count = 0

while count < 5:
    try:
        num = int(input(f"Enter number {count + 1}: "))
        if num < 0:
            print("Negative numbers not allowed")
            continue  # Don't count this attempt
        valid_numbers.append(num)
        count += 1
    except ValueError:
        print("Invalid input! Please enter a number")
        continue  # Don't count this attempt

print("Valid numbers entered:", valid_numbers)

# BREAK vs CONTINUE:
# 
# break:
# • Exits loop completely
# • No more iterations
# • Control moves to code after loop
# • Use when search is complete or condition met
#
# continue:
# • Skips rest of current iteration
# • Loop continues with next iteration
# • Must update counter BEFORE continue
# • Use to skip unwanted values
#
# IMPORTANT:
# When using continue with while loop:
# • Always increment counter BEFORE continue
# • Otherwise infinite loop (counter never changes)

