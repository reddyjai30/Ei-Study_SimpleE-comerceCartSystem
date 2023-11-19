import logging
from prettytable import PrettyTable
from product import SpecialProduct


def display_products(products):
    try:
        table = PrettyTable()
        table.field_names = ["Product Name", "Price", "Availability", "Discount", "BOGO Offer"]
        for product in products:
            discount_info = "N/A"
            bogo_info = "Yes" if product.bogo else "No"
            if isinstance(product, SpecialProduct) and product.discount_strategy:
                discount_info = f"{product.discount_strategy.percent}%"
                bogo_info = "N/A"

            table.add_row([product.name, f"${product.price}", "Yes" if product.available else "No", discount_info, bogo_info])
        print(table)
    
    except Exception as e:
        logging.error(f"Error in displaying products: {e}")     #Logging


def display_cart(cart):
    if cart is None or not cart.items:
        print("Cart is empty")
        return
    
    table = PrettyTable()
    table.field_names = ["Product Name", "Price", "Quantity"]
    for item in cart.items:
        table.add_row([item.name, f"${item.price}", getattr(item, 'quantity', 1)])
    print(table)

def display_checkout_summary(cart):
    if cart is None:
        raise ValueError("Cart is null")
    
    items_summary = ", ".join(f"{item.quantity} {item.name}{'s' if item.quantity > 1 else ''}" for item in cart.items)
    print(f"Cart Items: You have {items_summary} in your cart.")
    print(f"Total Bill: Your total bill is ${cart.total_bill()}.")
