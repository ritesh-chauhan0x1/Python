# ===== FILE 19: Odd and Even Numbers with Continue =====
# Topic: Using continue to filter odd/even numbers
# Concepts: Modulo operator, continue statement, number filtering

# ===== PRINT ODD NUMBERS =====
print("=== Odd Numbers (0 to 10) ===")
i = 0
while i <= 10:
    if i % 2 == 0:  # If even (divisible by 2)
        i += 1
        continue  # Skip printing, go to next iteration
    print(i, end=" ")  # Only prints odd numbers
    i += 1
print()

# ===== PRINT EVEN NUMBERS =====
print("\n=== Even Numbers (0 to 10) ===")
i = 0
while i <= 10:
    if i % 2 != 0:  # If odd (NOT divisible by 2)
        i += 1
        continue  # Skip printing, go to next iteration
    print(i, end=" ")  # Only prints even numbers
    i += 1
print()

# ===== PRACTICE QUESTIONS =====

# Problem 1: Odd numbers in range
print("\n--- Practice: Odd Numbers from 1 to 50 ---")
num = 1
while num <= 50:
    if num % 2 == 0:
        num += 1
        continue
    print(num, end=" ")
    num += 1
print()

# Problem 2: Even numbers sum
print("\n--- Practice: Sum of Even Numbers (1-100) ---")
i = 1
even_sum = 0
while i <= 100:
    if i % 2 != 0:
        i += 1
        continue
    even_sum += i
    i += 1
print(f"Sum of even numbers 1-100: {even_sum}")

# Problem 3: Divisible by 3 and 5
print("\n--- Practice: Divisible by Both 3 and 5 ---")
num = 1
print("Numbers divisible by both 3 and 5 (1-100):")
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
    num += 1
print()

# Problem 4: Skip multiples of 3
print("\n--- Practice: Numbers NOT Divisible by 3 ---")
i = 1
while i <= 30:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print()

# Problem 5: Odd numbers in list
print("\n--- Practice: Filter Odd from List ---")
numbers = [12, 7, 19, 24, 31, 46, 53, 68, 75]
print("Original list:", numbers)
print("Odd numbers:", end=" ")

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
        continue
    print(numbers[i], end=" ")
    i += 1
print()

# Problem 6: Count odd and even
print("\n--- Practice: Count Odd and Even ---")
numbers = [10, 15, 23, 42, 37, 56, 81, 94]
odd_count = 0
even_count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print(f"Numbers: {numbers}")
print(f"Odd count: {odd_count}")
print(f"Even count: {even_count}")

# Problem 7: Separate odd and even
print("\n--- Practice: Separate Lists ---")
mixed = [11, 24, 33, 48, 55, 62, 77, 84, 99]
odd_list = []
even_list = []
i = 0

while i < len(mixed):
    if mixed[i] % 2 == 0:
        even_list.append(mixed[i])
    else:
        odd_list.append(mixed[i])
    i += 1

print("Original:", mixed)
print("Odd numbers:", odd_list)
print("Even numbers:", even_list)

# Problem 8: Print divisibility info
print("\n--- Practice: Divisibility Info ---")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(f"{num} is even", end="")
    else:
        print(f"{num} is odd", end="")
    
    if num % 3 == 0:
        print(", divisible by 3")
    else:
        print()
    
    num += 1

# Problem 9: Sum odd and even separately
print("\n--- Practice: Separate Sums ---")
i = 1
odd_sum = 0
even_sum = 0

while i <= 50:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print(f"Sum of odd numbers (1-50): {odd_sum}")
print(f"Sum of even numbers (1-50): {even_sum}")
print(f"Total sum: {odd_sum + even_sum}")

# Problem 10: User input filtering
print("\n--- Practice: Filter User Input ---")
numbers = []
print("Enter 10 numbers:")
count = 0

while count < 10:
    num = int(input(f"Number {count + 1}: "))
    numbers.append(num)
    count += 1

# Filter and display
print("\nEntered numbers:", numbers)

print("Odd numbers:", end=" ")
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
        continue
    print(numbers[i], end=" ")
    i += 1

print("\nEven numbers:", end=" ")
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        i += 1
        continue
    print(numbers[i], end=" ")
    i += 1
print()

# KEY CONCEPTS:
# 
# Odd numbers:  number % 2 != 0  OR  number % 2 == 1
# Even numbers: number % 2 == 0
#
# Pattern with continue:
# while condition:
#     if (unwanted condition):
#         counter += 1
#         continue  # Skip to next iteration
#     process_value()
#     counter += 1
#
# Alternative without continue:
# while condition:
#     if (wanted condition):
#         process_value()
#     counter += 1