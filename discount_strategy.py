import logging
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

#Refined Exception Handling

class PercentageOffStrategy(DiscountStrategy):
    def __init__(self, percent):
        if not (0 <= percent <= 100):                       # defensive programming
            raise ValueError("Discount percentage must be between 0 and 100")
        
        self.percent = percent

    def apply(self, price):
        try:
            if price < 0:
                raise ValueError("Price cannot be negative")
            
            discounted_price = price * (1 - (self.percent / 100.0))
            return round(discounted_price, 2)
        except Exception as e:
            logging.error(f"Error in applying discount: {e}")       #Logging
            return price

