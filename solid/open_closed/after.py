class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} with card")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} with PayPal")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} with cash")


class Payment:
    def process(self, payment_method, amount):
        payment_method.pay(amount)


payment = Payment()

payment.process(CardPayment(), 100)
payment.process(PayPalPayment(), 200)
payment.process(CashPayment(), 50)
