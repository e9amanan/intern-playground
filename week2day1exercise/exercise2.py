"""
Module providing the BankAccount class for financial transactions.
"""


class BankAccount:
    """Represents a bank account with deposit and withdrawal capabilities."""

    def __init__(self, owner: str, balance: float = 0.0):
        """Initializes a new bank account."""
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        """Returns the current account balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Adds a positive amount to the account balance."""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be greater than 0")

    def withdraw(self, amount: float) -> bool:
        """Subtracts a valid amount if funds are sufficient."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def __repr__(self) -> str:
        """Returns the official string representation of the account."""
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"
