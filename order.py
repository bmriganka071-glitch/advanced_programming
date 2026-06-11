from abc import ABC, abstractmethod

# The Blueprint
class Order(ABC):
    def __init__(self, order_id: str, base_amount: float):
        self.order_id = order_id
        self.base_amount = base_amount

    @abstractmethod
    def calculate_total(self) -> float:
        """Every order type must know how to calculate its final price."""
        pass

# The Concrete Classes
class RegularOrder(Order):
    def calculate_total(self) -> float:
        # Regular orders just pay the base amount
        return self.base_amount

class DiscountedOrder(Order):
    def calculate_total(self) -> float:
        # Discounted orders get 10% off!
        return self.base_amount * 0.90

class PriorityOrder(Order):
    def calculate_total(self) -> float:
        # Priority orders pay a 50 gold express shipping fee
        return self.base_amount + 50.0