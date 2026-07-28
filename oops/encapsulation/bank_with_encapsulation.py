# Hide the internal data and allow access though method/function only
# Data member, and it's operation should be in same class

class BankAccount:
    def __init__(self, name, balance):
        self.name = name # public
        self.__balance = balance # private

    def get_balance(self):
        return self.__balance

    # these type of function are helper or utility function
    def __check_transaction_rule(self):
        if self.__balance == 0:
            print("You have low balance, please deposit some amount")
            return False
        else:
            return True


    def deposit(self, amount):
        if not self.__check_transaction_rule():
            return

        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if not self.__check_transaction_rule():
            return

        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdraw amount must be positive and less than or equal to balance")



acc1 = BankAccount("Aryan", 1000)
# acc1.balance = -200 # This will not work as balance is private
acc1.name = "Hacked"
print(acc1.name)
print(acc1.get_balance())
acc1.deposit(-100)
acc1.deposit(100)
print(acc1.get_balance())
acc1.withdraw(-100) # negative
acc1.withdraw(5100)
acc1.withdraw(250)
print(acc1.get_balance())
# print(acc1.balance) # This will not work as balance is private