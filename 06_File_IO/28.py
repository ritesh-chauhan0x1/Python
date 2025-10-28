# ===== FILE 28: File I/O - Reading and Writing Files =====
# Topic: Working with files - creating, reading, writing, and modifying
# Concepts: open(), write(), read(), with statement, file modes, string methods

# ORIGINAL CODE - File operations

# Task 1: Create a new file "pratice.txt" with specific content
# Write mode ('w+') creates new file or overwrites existing
with open("pratice.txt", "w+") as f:
    f.write(" hi everyone\n we are learning file i/o\n using java\n i like programming in java")

# Task 2: Read the file content
with open("pratice.txt", "r") as f:
    data = f.read()

print(data)

# Task 3: Replace all occurrences of "java" with "Python"
new_data = data.replace("java", "Python")
print(new_data)

# Task 4: Write the modified data back to file
with open("pratice.txt", "w") as f:
    f.write(new_data)

# Task 5: Search for a specific word in the file
word = "learning"
with open("pratice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):  # find() returns -1 if not found
        print("found")
    else:
        print("not found")

# ===== PRACTICE QUESTIONS =====

# Problem 1: Count the number of lines in a file
print("\n--- Problem 1: Count lines ---")
with open("pratice.txt", "r") as f:
    lines = f.readlines()
    print(f"Number of lines: {len(lines)}")

# Problem 2: Count total words in the file
print("\n--- Problem 2: Count words ---")
with open("pratice.txt", "r") as f:
    content = f.read()
    words = content.split()
    print(f"Total words: {len(words)}")

# Problem 3: Append text to existing file
print("\n--- Problem 3: Append to file ---")
with open("pratice.txt", "a") as f:
    f.write("\nThis line was appended!")

# Problem 4: Read file line by line
print("\n--- Problem 4: Read line by line ---")
with open("pratice.txt", "r") as f:
    line_num = 1
    for line in f:
        print(f"Line {line_num}: {line.strip()}")
        line_num += 1

# Problem 5: Count specific character occurrences
print("\n--- Problem 5: Count character 'i' ---")
with open("pratice.txt", "r") as f:
    content = f.read()
    count = content.lower().count('i')
    print(f"Character 'i' appears {count} times")

# Problem 6: Convert file content to uppercase
print("\n--- Problem 6: Convert to uppercase ---")
with open("pratice.txt", "r") as f:
    data = f.read()

uppercase_data = data.upper()
with open("pratice_upper.txt", "w") as f:
    f.write(uppercase_data)
print("Created pratice_upper.txt with uppercase content")

# Problem 7: Check if file contains a list of words
print("\n--- Problem 7: Check multiple words ---")
words_to_find = ["Python", "learning", "xyz"]
with open("pratice.txt", "r") as f:
    content = f.read()
    for word in words_to_find:
        if word in content:
            print(f"'{word}' found!")
        else:
            print(f"'{word}' not found")

# Problem 8: Copy content from one file to another
print("\n--- Problem 8: Copy file ---")
with open("pratice.txt", "r") as source:
    content = source.read()

with open("pratice_copy.txt", "w") as destination:
    destination.write(content)
print("File copied to pratice_copy.txt")

# CONCEPT SUMMARY:
# FILE MODES:
# - 'r'  : Read (default) - file must exist
# - 'w'  : Write - creates new or overwrites
# - 'a'  : Append - adds to end of file
# - 'r+' : Read and write
# - 'w+' : Write and read (overwrites)
#
# IMPORTANT METHODS:
# - read()      : Read entire file
# - readline()  : Read one line
# - readlines() : Read all lines as list
# - write()     : Write string to file
# - with statement : Automatically closes file