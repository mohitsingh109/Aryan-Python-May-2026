# Hide the internal data and allow access though method only

class BankAccount:
    def __init__(self, name, balance):
        self.name = name # public
        self.balance = balance # public


acc1 = BankAccount("Aryan", 1000)
acc1.balance = 200 # Anyone can change the value
acc1.name = "Hacked"
print(acc1.name)
print(acc1.balance)