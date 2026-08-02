from exception_handling.custom_exception import InsufficientBalanceError


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


    def withdraw(self, amount):
        if amount > self.__balance:
            # we are raising an exception 100%
            raise InsufficientBalanceError("Not enough balance")
        self.__balance -= amount
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            raise Exception("Amount cannot be negative")
        self.__balance += amount

    def check_balance(self):
        return self.__balance


# data first pulled from DB
# convert it into object (ORM)
account = BankAccount(100)
try:
    account.withdraw(1000)
except InsufficientBalanceError as e:
    print(e)
    # send email to user
    # send sms to user
except Exception as e:
    print(e)


try:
    account.deposit(-10)
except Exception as e: # user defined/ db error/ unknown error
    print(e)