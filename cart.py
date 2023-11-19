import logging
from product import Product, SpecialProduct

class Cart:
    def __init__(self):
        self.items = []

#Refined Exception Handling

    def add_product(self, product):
        if not product:
            raise ValueError("Cannot add a null product")
        
        existing_product = next((item for item in self.items if item.name == product.name), None)
        if existing_product:
            existing_product.quantity += 2 if product.bogo else 1
        else:
            product.quantity = 2 if product.bogo else 1
            self.items.append(product)

    def update_quantity(self, product_name, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
         
        for item in self.items:
            if item.name.lower() == product_name.lower():
                # Check if the item is a BOGO product
                if item.bogo:
                    # Double the entered quantity for display in the cart
                    item.quantity = quantity * 2
                else:
                    item.quantity = quantity
                print(f"Updated {product_name} quantity to {item.quantity}.")
                return
        print(f"Product '{product_name}' not found in the cart.")
    
    def remove_product(self, product_name, remove_one_unit=False):
        
        try:
            for item in self.items:
                if item.name.lower() == product_name.lower():
                    if remove_one_unit:
                        decrement_amount = 2 if item.bogo else 1
                        item.quantity -= decrement_amount
                        if item.quantity <= 0:
                            self.items.remove(item)
                    else:
                        self.items.remove(item)
                    return
            print(f"Product '{product_name}' not found in the cart.")
        
        except Exception as e:
            logging.error(f"Error in removing product: {e}")            #Logging
    
    def total_bill(self):
        total = 0
        for item in self.items:
            if isinstance(item, SpecialProduct) and item.discount_strategy:
                # Apply discount if available
                discounted_price = item.discount_strategy.apply(item.price)
                total += discounted_price * item.quantity
            elif item.bogo:
                # Calculate for BOGO products
                total += (item.quantity // 2 + item.quantity % 2) * item.price
            else:
                # Regular pricing for non-discount, non-BOGO products
                total += item.quantity * item.price
        return round(total, 2)
