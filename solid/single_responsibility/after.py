class Order:
    def __init__(self, product, price, email):
        self.product = product
        self.price = price
        self.email = email

    def calculate_total(self):
        return self.price * 1.2


class OrderRepository:
    def save(self, order):
        print(f"Saving order for {order.product} to database...")


class EmailService:
    def send_confirmation(self, order):
        print(f"Sending confirmation email to {order.email}...")


class InvoiceGenerator:
    def generate(self, order):
        print(f"Invoice: {order.product} - {order.price}")


order = Order("Laptop", 1000, "customer@example.com")

repository = OrderRepository()
email_service = EmailService()
invoice_generator = InvoiceGenerator()

print("Total:", order.calculate_total())

repository.save(order)
email_service.send_confirmation(order)
invoice_generator.generate(order)
