# Private means private no one can access even the child is also not allowed
# Protected variable - same as private but has access in child class
class Account:
    def __init__(self, name, balance):
        self._name = name # protected (1 %)
        self.__balance = balance # private (99 %)

    def get_balance(self):
        return self.__balance


class BankAccount(Account):
    def __init__(self, name, age, balance):
        super().__init__(name, balance)
        self.__age = age # private

    def get_name(self):
        return self._name


acc1 = BankAccount("John", 35, 1000)
print(acc1.get_balance())
print(acc1.get_name())
#
# acc1.__balance
# acc1.__age