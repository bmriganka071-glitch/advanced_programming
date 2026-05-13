from payment import Paymentmethod, Creditcard_Payment, UPI_Payment, Wallet_Payment
from notifier import Notifier, EmailNotifier,SMSNotifier,PushNotifier
from storage import OrderStorage, DatabaseStorage
from order import Order, RegularOrder, DiscountedOrder, PriorityOrder

class Order_service:
    def __init__(self, PAYMENTMETHOD: Paymentmethod, NOTIFIER: Notifier , STORAGE: OrderStorage):
        self.PAYMENTMETHOD = PAYMENTMETHOD
        self.NOTIFIER = NOTIFIER
        self.STORAGE =STORAGE

    def process_order(self, order: Order):
        print(f"\n --- INITIATING ORDER: {order.order_id} --- ")
        
        # 1. Ask the order to calculate its own total!
        final_amount = order.calculate_total()
        
        # 2. Process everything using the calculated amount
        self.PAYMENTMETHOD.pay(final_amount)
        self.STORAGE.save(order.order_id, f"Final Amount: {final_amount} gold")
        self.NOTIFIER.send(f"Success! Your order {order.order_id} is on its way.")
        
        print(" --- ORDER COMPLETE --- \n")


        
if __name__ == "__main__":
    print("Welcome to the Indestructible E-Commerce Kingdom!\n")

    # Let's create our Commander
    commander = Order_service(
       PAYMENTMETHOD=UPI_Payment(),
        NOTIFIER=PushNotifier(),
        STORAGE=DatabaseStorage()
    )
    
    # 1. A Regular Order (Base: 1000) -> Should charge 1000
    regular_order = RegularOrder("ORD-001", 1000.0)
    commander.process_order(regular_order)

    # 2. A Discounted Order (Base: 1000) -> Should charge 900
    discount_order = DiscountedOrder("ORD-002", 1000.0)
    commander.process_order(discount_order)

    # 3. A Priority Order (Base: 1000) -> Should charge 1050
    priority_order = PriorityOrder("ORD-003", 1000.0)
    commander.process_order(priority_order)