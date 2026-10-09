class Payment:
    def pay(self, payment_type, amount):
        if payment_type == "card":
            print(f"Paying {amount} with card")
        elif payment_type == "paypal":
            print(f"Paying {amount} with PayPal")
        elif payment_type == "cash":
            print(f"Paying {amount} with cash")


payment = Payment()

payment.pay("card", 100)
payment.pay("paypal", 200)
payment.pay("cash", 50)
