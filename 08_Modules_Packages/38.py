"""
Python Modules & Packages - OS Module
======================================
The os module provides functions to interact with the operating system.
It helps with file/directory operations, environment variables, and more.
"""

import os

# Get current working directory
print("=== Current Working Directory ===")
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# List files and directories
print("\n=== List Directory Contents ===")
contents = os.listdir('.')
print(f"Contents of current directory:")
for item in contents[:5]:  # Show first 5 items
    print(f"  - {item}")

# Check if path exists
print("\n=== Check Path Existence ===")
print(f"Does 'summary.py' exist? {os.path.exists('summary.py')}")
print(f"Does 'fake_file.txt' exist? {os.path.exists('fake_file.txt')}")

# Check if it's a file or directory
print("\n=== Check File vs Directory ===")
print(f"Is 'summary.py' a file? {os.path.isfile('summary.py')}")
print(f"Is '01_Basics' a directory? {os.path.isdir('01_Basics')}")

# Get file size
print("\n=== Get File Information ===")
if os.path.exists('summary.py'):
    size = os.path.getsize('summary.py')
    print(f"Size of summary.py: {size} bytes")

# Get absolute path
print("\n=== Get Absolute Path ===")
rel_path = "summary.py"
abs_path = os.path.abspath(rel_path)
print(f"Relative path: {rel_path}")
print(f"Absolute path: {abs_path}")

# Split path into directory and filename
print("\n=== Split Path ===")
directory, filename = os.path.split(abs_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")

# Join paths
print("\n=== Join Paths ===")
folder = "08_Modules_Packages"
file = "36.py"
full_path = os.path.join(folder, file)
print(f"Joined path: {full_path}")

# Get file extension
print("\n=== Get File Extension ===")
filename = "document.pdf"
name, extension = os.path.splitext(filename)
print(f"Name: {name}, Extension: {extension}")

# Environment variables
print("\n=== Environment Variables ===")
print(f"Username: {os.getenv('USERNAME', 'Not found')}")
print(f"Home directory: {os.getenv('USERPROFILE', 'Not found')}")

# Create directory (commented to avoid creating unwanted dirs)
print("\n=== Create/Remove Directory (Example) ===")
print("# os.mkdir('new_folder')  # Create single directory")
print("# os.makedirs('parent/child/grandchild')  # Create nested directories")
print("# os.rmdir('new_folder')  # Remove empty directory")

# Rename file/directory
print("\n=== Rename File/Directory (Example) ===")
print("# os.rename('old_name.txt', 'new_name.txt')")

# Get file stats
print("\n=== File Statistics (Example) ===")
if os.path.exists('summary.py'):
    stats = os.stat('summary.py')
    print(f"File size: {stats.st_size} bytes")
    print(f"Last modified: {stats.st_mtime}")

# Walk through directory tree
print("\n=== Walk Directory Tree (Example) ===")
print("# Traverse all directories and files:")
print("# for root, dirs, files in os.walk('.'):")
print("#     print(f'Directory: {root}')")
print("#     for file in files:")
print("#         print(f'  File: {file}')")

# Path operations
print("\n=== Path Operations ===")
path1 = "/home/user/documents/file.txt"
print(f"Directory name: {os.path.dirname(path1)}")
print(f"Base name: {os.path.basename(path1)}")

"""
PRACTICE PROBLEMS:
1. Print the current working directory
2. List all Python files in the current directory
3. Check if a file named 'test.txt' exists
4. Create a directory called 'temp_folder'
5. Get the size of 'summary.py' in KB (divide by 1024)
6. Join paths: 'folder', 'subfolder', 'file.txt'
7. Get the extension of 'image.png'
8. Print your username from environment variables
9. Count how many .py files are in the current directory
10. Create nested directories: 'data/raw/csv'
"""
