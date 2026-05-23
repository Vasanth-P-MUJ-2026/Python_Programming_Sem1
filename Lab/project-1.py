# Custom Exception
class InsufficientBalanceError(Exception):
    pass

# Bank account class
class BankAccount:
    def __init__(self):
        self.balance = 5000

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance to withdraw!")
        else:
            self.balance -= amount
            print("Withdrawal sucessful")
            print("Updated Balance:",self.balance)

#Execution
try:
    amount = int(input())
    account = BankAccount()
    account.withdraw(amount)
except InsufficientBalanceError as e:
    print(e)
