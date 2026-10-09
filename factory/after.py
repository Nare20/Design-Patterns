
class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")


notification = NotificationFactory.create_notification("email")
notification.send("Hello!")

notification = NotificationFactory.create_notification("sms")
notification.send("Hello!")

