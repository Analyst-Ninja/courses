"""
Example for behaviour type class
"""


class BankAccount:
    """
    Class for representing bank account
    """

    def __init__(self, account_holder: str, balance: int = 0) -> None:
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: int):
        """
        Deposit method
        """
        self.balance += amount

    def withdraw(self, amount: int):
        """
        Withdraw method
        """
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    # Comparison based on account balance
    def __lt__(self, other: "BankAccount"):
        return self.balance < other.balance

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            raise NotImplementedError
        return self.balance == other.balance


def main():
    account1 = BankAccount("Rohit", 1000)
    account2 = BankAccount("Ajay", 1000)

    print(account1 < account2)
    print(account1 == account2)


if __name__ == "__main__":
    main()
