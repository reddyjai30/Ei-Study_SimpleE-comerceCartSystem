from product import Product, SpecialProduct
from discount_strategy import PercentageOffStrategy


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Incorrect format, please enter a valid number.")

def input_txt(prompt):
    while True:
        try:
            return (input(prompt))
        except ValueError:
            print("Incorrect format, please enter a valid string from above.")

def input_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("Please enter 'yes' or 'no'.")


def get_default_products():
    default_products = [
        SpecialProduct("Laptop", 1000, True, PercentageOffStrategy(10)),  # Discounted
        Product("Headphones", 150, True, bogo=True),                      # BOGO(Buy 1Get 1 Free)Offer
        SpecialProduct("Smartphone", 800, True, PercentageOffStrategy(5)),# Discounted
        Product("Charger", 20, True),                                     # No Offer
        Product("Camera", 500, True, bogo=True)                           # BOGO Offer
    ]
    return default_products


def input_product():

    try:
        name = input("Enter product name: ")
        price = float(input_float("Enter product price: "))
        available = input("Is the product available (yes/no)? ") == 'yes'
        
        promo_type = input_txt("Choose promotion type (discount/bogo/none): ").lower()

        if promo_type == 'discount':
            percent = float(input_float("Enter discount percentage: "))
            return SpecialProduct(name, price, available, PercentageOffStrategy(percent))

        if promo_type == 'bogo':
            return Product(name, price, available, bogo=True)
        
        return Product(name, price, available)
    
    except Exception as e:
        print(f"Error during product input: {e}")