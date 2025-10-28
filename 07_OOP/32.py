# ===== FILE 32: OOP - Bank Account with Methods =====
# Topic: Creating a practical class with multiple methods
# Concepts: Constructor, methods, instance variables, method chaining

# ORIGINAL CODE - Account class with debit and credit

class Acount:
    """Class to represent a bank account with balance and account number"""
    
    def __init__(self, bal, acc):
        """Initialize account with balance and account number"""
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        """Deduct amount from balance"""
        self.balance -= amount
        print("Rs", amount, "Debited From Acc -", self.account_no, 
              "Your Total Balance is :", self.get_balance())
    
    def credit(self, amount):
        """Add amount to balance"""
        self.balance += amount
        print("Rs", amount, "Credited To Acc -", self.account_no,
              "Your Total Balance is :", self.get_balance())
    
    def get_balance(self):
        """Return current balance"""
        return self.balance

# Create account and perform transactions
acc1 = Acount(10000, 12122001100210005645)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(500)
acc1.credit(100)
acc1.credit(500)

# ===== PRACTICE QUESTIONS =====

# Problem 1: Add minimum balance check
print("\n--- Problem 1: Account with minimum balance ---")
class BankAccount:
    MIN_BALANCE = 1000  # Class variable
    
    def __init__(self, name, balance, account_no):
        self.name = name
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print(f"Transaction failed! Minimum balance of Rs {self.MIN_BALANCE} required")
        else:
            self.balance -= amount
            print(f"Rs {amount} debited. Balance: Rs {self.balance}")
    
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} credited. Balance: Rs {self.balance}")

acc2 = BankAccount("Ritesh", 5000, 123456)
acc2.debit(3500)  # Should fail
acc2.debit(2000)  # Should succeed

# Problem 2: Add transaction history
print("\n--- Problem 2: Account with transaction history ---")
class AccountWithHistory:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
    
    def debit(self, amount):
        self.balance -= amount
        self.transactions.append(f"Debit: Rs {amount}")
        print(f"Rs {amount} debited. Balance: Rs {self.balance}")
    
    def credit(self, amount):
        self.balance += amount
        self.transactions.append(f"Credit: Rs {amount}")
        print(f"Rs {amount} credited. Balance: Rs {self.balance}")
    
    def show_history(self):
        print(f"\nTransaction History for {self.name}:")
        for transaction in self.transactions:
            print(f"  - {transaction}")
        print(f"Current Balance: Rs {self.balance}")

acc3 = AccountWithHistory("Alice", 10000)
acc3.credit(2000)
acc3.debit(1500)
acc3.credit(500)
acc3.show_history()

# Problem 3: Add interest calculation
print("\n--- Problem 3: Savings account with interest ---")
class SavingsAccount:
    INTEREST_RATE = 0.04  # 4% annual interest
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def add_interest(self):
        interest = self.balance * self.INTEREST_RATE
        self.balance += interest
        print(f"Interest of Rs {interest:.2f} added. New balance: Rs {self.balance:.2f}")
    
    def display(self):
        print(f"Account: {self.name}, Balance: Rs {self.balance:.2f}")

savings = SavingsAccount("Bob", 50000)
savings.display()
savings.add_interest()

# Problem 4: Add transfer money between accounts
print("\n--- Problem 4: Transfer between accounts ---")
class Account2:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient funds for transfer!")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Rs {amount} transferred from {self.name} to {recipient.name}")
    
    def show(self):
        print(f"{self.name}: Rs {self.balance}")

acc_a = Account2("John", 5000)
acc_b = Account2("Mary", 3000)
print("Before transfer:")
acc_a.show()
acc_b.show()
acc_a.transfer(1000, acc_b)
print("After transfer:")
acc_a.show()
acc_b.show()

# Problem 5: Create a credit card account with limit
print("\n--- Problem 5: Credit card account ---")
class CreditCard:
    def __init__(self, holder, credit_limit):
        self.holder = holder
        self.credit_limit = credit_limit
        self.balance = 0  # Amount owed
    
    def charge(self, amount):
        if self.balance + amount > self.credit_limit:
            print(f"Charge denied! Exceeds credit limit of Rs {self.credit_limit}")
        else:
            self.balance += amount
            print(f"Rs {amount} charged. Amount owed: Rs {self.balance}")
    
    def pay(self, amount):
        self.balance -= amount
        print(f"Payment of Rs {amount} received. Amount owed: Rs {self.balance}")
    
    def available_credit(self):
        return self.credit_limit - self.balance

card = CreditCard("Alice", 50000)
card.charge(10000)
card.charge(5000)
print(f"Available credit: Rs {card.available_credit()}")
card.pay(3000)
print(f"Available credit: Rs {card.available_credit()}")

# CONCEPT SUMMARY:
# - Methods can modify instance variables (self.variable)
# - Methods can call other methods using self.method()
# - Class variables (like MIN_BALANCE) shared by all instances
# - Good practice: Validate input before modifying data
# - Encapsulation: Keep related data and operations together
# - Real-world modeling: Classes represent real objects/concepts