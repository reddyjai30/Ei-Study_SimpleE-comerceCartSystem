import copy

class Product:
    def __init__(self, name, price, available, bogo=False):
        self.name = name
        self.price = price
        self.available = available
        self.bogo = bogo

    def clone(self):
        return copy.deepcopy(self)

    def get_final_price(self, quantity=1):
        if self.bogo and quantity > 1:
            return self.price * (quantity // 2 + quantity % 2)
        return self.price * quantity

class SpecialProduct(Product):
    def __init__(self, name, price, available, discount_strategy=None, bogo=False):
        super().__init__(name, price, available, bogo)
        self.discount_strategy = discount_strategy

    def get_final_price(self, quantity=1):
        if self.discount_strategy:
            return self.discount_strategy.apply(self.price, quantity)
        return super().get_final_price(quantity)
