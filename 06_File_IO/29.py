# ===== FILE 29: File I/O - Advanced Operations =====
# Topic: Working with files - searching specific lines and processing data
# Concepts: readline(), file iteration, line numbers, string methods

# ORIGINAL CODE - Find word in specific line

def check_for_line():
    """Find the first line number where a word appears"""
    word = "learning"  # Note: was "learnning" (typo fixed)
    data = True
    line_no = 1
    with open("pratice.txt", "r") as f:
        while data:
            data = f.readline()  # Read one line at a time
            if (word in data):
                print(line_no)
                return line_no
            line_no += 1
    return -1  # Return -1 if word not found

print(check_for_line())

# ===== PRACTICE QUESTIONS =====

# Problem 1: Find all line numbers where a word appears
print("\n--- Problem 1: Find all occurrences ---")
def find_all_lines(filename, word):
    """Find all lines containing a specific word"""
    lines_found = []
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if word in line:
                lines_found.append(line_num)
    return lines_found if lines_found else [-1]

print(f"'Python' found in lines: {find_all_lines('pratice.txt', 'Python')}")

# Problem 2: Count occurrences of a word in entire file
print("\n--- Problem 2: Count word occurrences ---")
def count_word_in_file(filename, word):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            count += line.lower().count(word.lower())
    return count

print(f"'learning' appears {count_word_in_file('pratice.txt', 'learning')} times")

# Problem 3: Get the longest line in a file
print("\n--- Problem 3: Find longest line ---")
def find_longest_line(filename):
    longest = ""
    with open(filename, "r") as f:
        for line in f:
            if len(line) > len(longest):
                longest = line
    return longest.strip()

print(f"Longest line: {find_longest_line('pratice.txt')}")

# Problem 4: Print lines containing a specific character
print("\n--- Problem 4: Lines with 'i' ---")
def print_lines_with_char(filename, char):
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if char in line:
                print(f"Line {line_num}: {line.strip()}")

print_lines_with_char('pratice.txt', 'i')

# Problem 5: Reverse the order of lines in a file
print("\n--- Problem 5: Reverse file lines ---")
def reverse_file_lines(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    with open(output_file, "w") as f:
        for line in reversed(lines):
            f.write(line)
    print(f"Reversed lines written to {output_file}")

reverse_file_lines('pratice.txt', 'pratice_reversed.txt')

# Problem 6: Find line with maximum words
print("\n--- Problem 6: Line with most words ---")
def line_with_most_words(filename):
    max_words = 0
    max_line_num = 0
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            word_count = len(line.split())
            if word_count > max_words:
                max_words = word_count
                max_line_num = line_num
    return max_line_num, max_words

line_num, word_count = line_with_most_words('pratice.txt')
print(f"Line {line_num} has the most words ({word_count})")

# Problem 7: Extract specific lines (e.g., lines 2-4)
print("\n--- Problem 7: Extract specific lines ---")
def extract_lines(filename, start, end):
    """Extract lines from start to end (inclusive)"""
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines[start-1:end]

extracted = extract_lines('pratice.txt', 1, 3)
print("Lines 1-3:")
for line in extracted:
    print(line.strip())

# CONCEPT SUMMARY:
# - readline() reads one line at a time
# - enumerate() provides line numbers while iterating
# - 'in' operator checks if substring exists in string
# - readlines() reads all lines into a list
# - reversed() reverses any iterable
# - File iteration is memory-efficient for large files
# - Always return -1 or None for "not found" scenarios

