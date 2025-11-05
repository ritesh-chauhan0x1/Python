"""
Python Modules & Packages - Random Module
==========================================
The random module is used to generate random numbers and make random choices.
"""

import random

# Generate random numbers
print("=== Random Numbers ===")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1-10: {random.randint(1, 10)}")
print(f"Random integer from range: {random.randrange(0, 100, 5)}")  # Step of 5

# Random float in range
print("\n=== Random Float in Range ===")
print(f"Random float between 1.5 and 5.5: {random.uniform(1.5, 5.5)}")

# Random choice from sequence
print("\n=== Random Choice ===")
colors = ["red", "blue", "green", "yellow", "purple"]
print(f"Random color: {random.choice(colors)}")

fruits = ["apple", "banana", "orange", "mango"]
print(f"Random fruit: {random.choice(fruits)}")

# Random sample (multiple items without replacement)
print("\n=== Random Sample ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample = random.sample(numbers, 3)  # Pick 3 random numbers
print(f"Random sample of 3 numbers: {sample}")

# Shuffle a list
print("\n=== Shuffle List ===")
cards = ["A", "K", "Q", "J", "10", "9"]
print(f"Original deck: {cards}")
random.shuffle(cards)  # Shuffles in-place
print(f"Shuffled deck: {cards}")

# Random choices with replacement
print("\n=== Random Choices (with replacement) ===")
dice_rolls = random.choices([1, 2, 3, 4, 5, 6], k=5)  # Roll dice 5 times
print(f"Five dice rolls: {dice_rolls}")

# Weighted random choice
print("\n=== Weighted Random Choice ===")
outcomes = ["Win", "Lose", "Draw"]
weights = [10, 70, 20]  # Win: 10%, Lose: 70%, Draw: 20%
result = random.choices(outcomes, weights=weights, k=1)[0]
print(f"Game result: {result}")

# Setting seed for reproducibility
print("\n=== Random Seed ===")
random.seed(42)  # Set seed
print(f"Random number with seed 42: {random.randint(1, 100)}")
random.seed(42)  # Reset same seed
print(f"Same random number: {random.randint(1, 100)}")  # Same result

# Practical example: Generate OTP
print("\n=== Practical Example: Generate OTP ===")
otp = random.randint(100000, 999999)
print(f"Your OTP is: {otp}")

# Practical example: Password generator
print("\n=== Practical Example: Simple Password Generator ===")
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(8))
print(f"Generated password: {password}")

"""
PRACTICE PROBLEMS:
1. Generate a random number between 50 and 100
2. Simulate rolling two dice and print their sum
3. Create a list of 5 random colors from ["red", "blue", "green", "yellow"]
4. Generate a random 4-digit PIN code
5. Pick 3 random students from a list of 10 students
6. Shuffle a deck of cards (create a list of 52 cards)
7. Simulate a coin toss (Heads/Tails) 10 times
8. Generate a random float between 10.5 and 20.5
9. Create a lottery number picker (6 numbers from 1-49)
10. Generate a random password with 12 characters (letters + digits + symbols)
"""
