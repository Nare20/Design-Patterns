
class MessageService:
    def send(self, message):
        raise NotImplementedError


class EmailService(MessageService):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSService(MessageService):
    def send(self, message):
        print(f"Sending SMS: {message}")


class Notification:
    def __init__(self, service: MessageService):
        self.service = service

    def send_notification(self, message):
        self.service.send(message)


email_service = EmailService()
notification = Notification(email_service)
notification.send_notification("Hello!")

sms_service = SMSService()
notification = Notification(sms_service)
notification.send_notification("Hello!")

