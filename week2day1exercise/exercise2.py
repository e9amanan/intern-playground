class BankAccount:

    def __init__(self,owner:str,balance:float = 0.0):
        self.owner =owner
        self._balance=balance

    @property
    def balance(self)-> float:
        return self._balance
    
    def deposit(self,amount:float)-> None:
        if amount>0:
            self._balance+= amount
        else:
            raise ValueError("Deposit amount must be greater than 0")
    
    def withdraw(self,amount:float)-> bool:
        if 0< amount<self._balance:
            self._balance-=amount
            return True
        return False
    
    def __repr__(self)-> str:
        return f"BankAccount(owner='{self.owner}',balance={self._balance})"

        