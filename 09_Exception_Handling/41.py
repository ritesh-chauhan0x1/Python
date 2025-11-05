"""
Python Exception Handling - Else and Finally
=============================================
- else: Executes if no exception occurs in try block
- finally: Always executes, whether exception occurs or not
"""

# Try-except-else
print("=== Try-Except-Else ===")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful! Result: {result}")

# Try-except-finally
print("\n=== Try-Except-Finally ===")
try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error occurred!")
finally:
    print("This always executes - cleanup code goes here")

# Finally executes even with exception
print("\n=== Finally with Exception ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero error!")
finally:
    print("Finally block executed despite error")

# Complete structure: try-except-else-finally
print("\n=== Complete Structure ===")
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid data types")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed\n")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")

# Practical example: File handling
print("\n=== File Handling Example ===")
def read_file_safe(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: {content[:50]}...")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
    else:
        print("File read successfully")
    finally:
        if file:
            file.close()
            print("File closed")
        else:
            print("No file to close")

# Test with non-existent file
read_file_safe("nonexistent.txt")

# Example: Database connection simulation
print("\n=== Database Connection Simulation ===")
class Database:
    def __init__(self, name):
        self.name = name
        self.connected = False
    
    def connect(self):
        print(f"Connecting to {self.name}...")
        self.connected = True
    
    def disconnect(self):
        print(f"Disconnecting from {self.name}...")
        self.connected = False

def perform_database_operation():
    db = Database("TestDB")
    try:
        db.connect()
        # Simulate some database operation
        print("Performing database operation...")
        # Simulate an error
        result = 10 / 2
        print(f"Operation result: {result}")
    except Exception as e:
        print(f"Error during operation: {e}")
    else:
        print("Operation completed successfully")
    finally:
        db.disconnect()
        print("Cleanup completed")

perform_database_operation()

# Example: Input validation with complete structure
print("\n=== Input Validation Example ===")
def get_age():
    try:
        age_str = "25"  # Simulating user input
        age = int(age_str)
        
        # Validate age range
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
            
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None
    else:
        print(f"Age {age} is valid")
        return age
    finally:
        print("Age validation completed")

get_age()

# Example: Resource management
print("\n=== Resource Management ===")
def process_data():
    resource_acquired = False
    try:
        print("Acquiring resource...")
        resource_acquired = True
        
        # Process data
        data = [1, 2, 3, 4, 5]
        result = sum(data) / len(data)
        print(f"Average: {result}")
        
    except Exception as e:
        print(f"Error processing data: {e}")
    else:
        print("Data processed successfully")
    finally:
        if resource_acquired:
            print("Releasing resource...")
        print("Process completed")

process_data()

# When to use each block
print("\n=== When to Use Each Block ===")
print("""
try:
    - Code that might raise an exception
    
except:
    - Handle specific exceptions
    - Log errors, show user-friendly messages
    
else:
    - Code that should run only if NO exception occurred
    - Useful for code that depends on try block success
    
finally:
    - Cleanup code that MUST run (close files, connections)
    - Release resources
    - Always executes regardless of exceptions
""")

"""
PRACTICE PROBLEMS:
1. Write a function with try-except-else to validate password length
2. Create a file reader with finally to ensure file closure
3. Write a calculator with complete error handling structure
4. Create a function that handles list operations with else and finally
5. Build a login system with try-except-else-finally
6. Write a function to connect/disconnect from API with finally
7. Create a data processor with cleanup in finally block
8. Build a transaction system with rollback in except and commit in else
9. Write a function to handle JSON parsing with complete structure
10. Create a resource allocator with try-except-else-finally

CHALLENGE:
Build a database manager class with:
- connect() and disconnect() methods
- execute_query() with try-except-else-finally
- Ensure connection always closes in finally
- Handle multiple exception types
"""
