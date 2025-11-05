"""
Python Exception Handling - Raising Exceptions
===============================================
You can raise exceptions manually using the 'raise' keyword.
This is useful for validating input and enforcing business rules.
"""

# Basic raise
print("=== Basic Raise Exception ===")
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive!")
    return number

try:
    check_positive(10)
    print("10 is positive")
    check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")

# Raising different exception types
print("\n=== Different Exception Types ===")
def check_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age {age} is valid"

try:
    print(check_age(25))
    print(check_age(-5))
except (TypeError, ValueError) as e:
    print(f"Validation error: {e}")

# Re-raising exceptions
print("\n=== Re-raising Exceptions ===")
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Logging error: Division by zero")
        raise  # Re-raise the same exception

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Caught re-raised exception in outer handler")

# Custom exception classes
print("\n=== Custom Exception Classes ===")
class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    pass

class InvalidAccountError(Exception):
    """Custom exception for invalid account"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Balance: ${self.balance}, Requested: ${amount}"
            )
        self.balance -= amount
        return self.balance

account = BankAccount(1000)
try:
    print(f"Withdrawing $500...")
    account.withdraw(500)
    print(f"Success! New balance: ${account.balance}")
    
    print(f"Withdrawing $700...")
    account.withdraw(700)
except InsufficientFundsError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")

# Exception with custom attributes
print("\n=== Custom Exception with Attributes ===")
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_user(username, email):
    if len(username) < 3:
        raise ValidationError("username", "Must be at least 3 characters")
    if "@" not in email:
        raise ValidationError("email", "Must contain @ symbol")
    return True

try:
    validate_user("ab", "test@email.com")
except ValidationError as e:
    print(f"Validation failed!")
    print(f"Field: {e.field}")
    print(f"Message: {e.message}")

# Assert statement (raises AssertionError)
print("\n=== Assert Statement ===")
def calculate_percentage(score, total):
    assert total > 0, "Total must be greater than 0"
    assert score <= total, "Score cannot exceed total"
    return (score / total) * 100

try:
    print(f"Percentage: {calculate_percentage(85, 100)}%")
    print(f"Percentage: {calculate_percentage(110, 100)}%")
except AssertionError as e:
    print(f"Assertion error: {e}")

# Practical example: Form validation
print("\n=== Form Validation Example ===")
class RegistrationError(Exception):
    pass

def register_user(username, password, email, age):
    errors = []
    
    if len(username) < 3:
        errors.append("Username must be at least 3 characters")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    if "@" not in email or "." not in email:
        errors.append("Invalid email format")
    if age < 18:
        errors.append("Must be 18 or older")
    
    if errors:
        raise RegistrationError("\n".join(errors))
    
    return f"User {username} registered successfully!"

try:
    print(register_user("john_doe", "secure123", "john@email.com", 25))
except RegistrationError as e:
    print("Registration failed:")
    print(e)

try:
    print(register_user("ab", "weak", "invalid-email", 16))
except RegistrationError as e:
    print("Registration failed:")
    print(e)

# Practical example: API response validation
print("\n=== API Response Validation ===")
class APIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")

def process_api_response(status_code, data):
    if status_code == 404:
        raise APIError(404, "Resource not found")
    if status_code == 500:
        raise APIError(500, "Internal server error")
    if status_code != 200:
        raise APIError(status_code, "Unknown error")
    
    return f"Success: {data}"

try:
    print(process_api_response(200, {"user": "John"}))
    print(process_api_response(404, None))
except APIError as e:
    print(f"Status: {e.status_code}, Message: {e.message}")

"""
PRACTICE PROBLEMS:
1. Create a function that raises ValueError for negative numbers
2. Write a custom exception for invalid email addresses
3. Create an ATM withdrawal function with custom exceptions
4. Build a grade validator that raises exception for invalid grades (0-100)
5. Write a custom exception for duplicate username registration
6. Create a password validator with multiple custom exceptions
7. Build a temperature converter that raises exception for invalid scales
8. Write a custom exception hierarchy for a library system
9. Create a function that raises TypeError for wrong input types
10. Build a shopping cart with custom exceptions for stock/quantity

CHALLENGE:
Create a complete user management system with:
- Custom exceptions: UserExistsError, InvalidCredentialsError, PermissionError
- Functions: register(), login(), delete_user()
- Each function should raise appropriate custom exceptions
- Include proper error messages and validation
"""
