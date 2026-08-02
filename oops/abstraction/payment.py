# ATM Machine

"""
User can:
- withdraw money
- check balance
- deposit money

User can't do:
- How bank server is validates my PIN
- How database is updating my balance
- How transaction is processed
"""
# How to implement it in python
# ABC class, abstractmethod annotation

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    # transaction()
    def pay(self, amount):
        print(f"Paying {amount} using credit card")


class UPI(Payment):
    # send_money()
    def pay(self, amount):
        print(f"Paying {amount} using UPI")


class PayPal(Payment):
    # make_payment()
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")

class DebitCard(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using DebitCard")


payments = [
    CreditCard(),
    UPI(),
    PayPal(),
    DebitCard()
]

for payment in payments:
    payment.pay(100)