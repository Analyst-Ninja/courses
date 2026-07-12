from pprint import pprint

from langchain.text_splitter import Language, RecursiveCharacterTextSplitter

python_text = """
# Base class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner              # Public attribute
        self.__balance = balance        # Private attribute (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account holder: {self.owner}, Balance: ₹{self.__balance}"


# Inherited class
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)  # Inheritance
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest ₹{interest:.2f} applied at rate {self.interest_rate * 100}%.")


# Polymorphism example
def print_account_details(account):
    print(account)


# Creating objects
acc1 = BankAccount("Rohit", 5000)
acc2 = SavingsAccount("Neha", 10000)

# Using functions
acc1.deposit(1500)
acc1.withdraw(2000)
print_account_details(acc1)

acc2.apply_interest()
print_account_details(acc2)
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=1000, chunk_overlap=0, language=Language.PYTHON
)

res = splitter.split_text(text=python_text)

print(res)
pprint(len(res))
