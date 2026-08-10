# Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


# Creating an object

account = BankAccount("Riya", 5000)

print("Owner:", account.owner)
print("Initial balance:", account.get_balance())

account.deposit(1000)
print("Balance:", account.get_balance())

account.withdraw(2000)
print("Balance:", account.get_balance())
