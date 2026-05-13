from abc import ABC , abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"📧 Sending (Email): {message}")
class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"💬 Sending (SMS): {message}")
class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"🔔 Sending (Push): {message}")

