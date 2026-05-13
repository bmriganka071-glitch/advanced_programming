from abc import ABC , abstractmethod

class OrderStorage(ABC):
    @abstractmethod
    def save(self , order_ID : str , data : str):
        pass
class DatabaseStorage(OrderStorage):
    def save(self, order_id: str, data: str):
        print(f"🗄️ Saving... Order {order_id} saved to Database!")
class FileStorage(OrderStorage):
    def save(self, order_id: str, data: str):
        print(f"📜 Saving... Order {order_id} saved to File!")
