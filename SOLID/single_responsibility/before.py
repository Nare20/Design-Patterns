class Order:
    def __init__(self, product, price, email):
        self.product = product
        self.price = price
        self.email = email

    def calculate_total(self):
        return self.price * 1.2

    def save_to_database(self):
        print(f"Saving order for {self.product} to database...")

    def send_email(self):
        print(f"Sending confirmation email to {self.email}...")

    def print_invoice(self):
        print(f"Invoice: {self.product} - {self.price}")


order = Order("Laptop", 1000, "customer@example.com")

print("Total:", order.calculate_total())
order.save_to_database()
order.send_email()
order.print_invoice()
