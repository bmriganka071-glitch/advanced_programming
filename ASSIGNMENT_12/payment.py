from abc import ABC , abstractmethod

class Paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount:float):
        pass
class Creditcard_Payment(Paymentmethod):
    def pay(self, amount:float):
        print(f"💳 Swiping plastic... {amount} gold successfully charged to Credit Card!")
class UPI_Payment(Paymentmethod):
    def pay(self, amount:float):
        print(f"📱 Beep boop! Scanning QR code... {amount} gold transferred via UPI!")
class Wallet_Payment(Paymentmethod):
    def pay(self, amount: float):
        print(f"💰 Opening digital coin pouch... {amount} gold deducted from Wallet!")
