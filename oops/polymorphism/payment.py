# Polymorphism -> "many forms" -> same function name but different implementation

# e-commerce application
# Customer can pay using (Credit card, UPI, PayPal)
# Every payment has a method called pay()

class Payment:
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


payments = [
    CreditCard(),
    UPI(),
    PayPal()
]

for payment in payments:
    payment.pay(100) # ?