
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, message):
        self.email_service.send(message)


notification = Notification()
notification.send_notification("Hello!")

