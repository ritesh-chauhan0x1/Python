"""
Mini Project: CLI Calculator
=============================
A command-line calculator with basic operations and error handling.
Features: Add, Subtract, Multiply, Divide, Power, Square Root, Percentage
"""

import math

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("          PYTHON CALCULATOR")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")
    print("8. History")
    print("9. Clear History")
    print("0. Exit")
    print("="*50)

def get_number(prompt):
    """Get valid number from user with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def add(a, b):
    """Addition operation"""
    result = a + b
    print(f"\n✅ {a} + {b} = {result}")
    return result

def subtract(a, b):
    """Subtraction operation"""
    result = a - b
    print(f"\n✅ {a} - {b} = {result}")
    return result

def multiply(a, b):
    """Multiplication operation"""
    result = a * b
    print(f"\n✅ {a} × {b} = {result}")
    return result

def divide(a, b):
    """Division operation with error handling"""
    try:
        result = a / b
        print(f"\n✅ {a} ÷ {b} = {result}")
        return result
    except ZeroDivisionError:
        print("\n❌ Error: Cannot divide by zero!")
        return None

def power(a, b):
    """Power operation"""
    result = a ** b
    print(f"\n✅ {a}^{b} = {result}")
    return result

def square_root(a):
    """Square root operation with error handling"""
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(a)
        print(f"\n✅ √{a} = {result}")
        return result
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return None

def percentage(a, b):
    """Calculate percentage: a is what percent of b"""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot calculate percentage with zero base")
        result = (a / b) * 100
        print(f"\n✅ {a} is {result}% of {b}")
        return result
    except ZeroDivisionError as e:
        print(f"\n❌ Error: {e}")
        return None

def display_history(history):
    """Display calculation history"""
    if not history:
        print("\n📋 No calculations in history.")
        return
    
    print("\n" + "="*50)
    print("          CALCULATION HISTORY")
    print("="*50)
    for i, calc in enumerate(history, 1):
        print(f"{i}. {calc}")
    print("="*50)

def calculator():
    """Main calculator function"""
    history = []
    
    print("\n🎉 Welcome to Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using the calculator!")
                print(f"Total calculations performed: {len(history)}")
                break
            
            elif choice == '1':  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = add(a, b)
                if result is not None:
                    history.append(f"{a} + {b} = {result}")
            
            elif choice == '2':  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = subtract(a, b)
                if result is not None:
                    history.append(f"{a} - {b} = {result}")
            
            elif choice == '3':  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = multiply(a, b)
                if result is not None:
                    history.append(f"{a} × {b} = {result}")
            
            elif choice == '4':  # Division
                a = get_number("Enter numerator: ")
                b = get_number("Enter denominator: ")
                result = divide(a, b)
                if result is not None:
                    history.append(f"{a} ÷ {b} = {result}")
            
            elif choice == '5':  # Power
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = power(a, b)
                if result is not None:
                    history.append(f"{a}^{b} = {result}")
            
            elif choice == '6':  # Square Root
                a = get_number("Enter number: ")
                result = square_root(a)
                if result is not None:
                    history.append(f"√{a} = {result}")
            
            elif choice == '7':  # Percentage
                a = get_number("Enter number: ")
                b = get_number("Enter base (percent of): ")
                result = percentage(a, b)
                if result is not None:
                    history.append(f"{a} is {result}% of {b}")
            
            elif choice == '8':  # History
                display_history(history)
            
            elif choice == '9':  # Clear History
                history.clear()
                print("\n🗑️  History cleared!")
            
            else:
                print("\n❌ Invalid choice! Please enter 0-9.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Calculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()

"""
FEATURES IMPLEMENTED:
✅ Basic arithmetic operations (add, subtract, multiply, divide)
✅ Advanced operations (power, square root, percentage)
✅ Error handling for all operations
✅ Input validation
✅ Calculation history
✅ User-friendly menu interface
✅ Clear display with emojis

ENHANCEMENT IDEAS:
1. Add scientific functions (sin, cos, tan, log)
2. Add memory functions (M+, M-, MR, MC)
3. Save history to file
4. Add expression evaluation (e.g., "2+3*4")
5. Add unit conversions
6. Implement undo/redo functionality
7. Add graphing capabilities
8. Create GUI version with tkinter
9. Add complex number support
10. Implement matrix operations
"""
