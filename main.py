import logging
from cart import Cart
from ui_helpers import display_products, display_cart, display_checkout_summary
from product_input import get_default_products, input_product, input_yes_no, input_float


# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    products = []
    cart = Cart()

    try:
        # Defensive programming: Validate number input and handle exceptions
        use_default = input_yes_no("Would you like to use default Shopping products? (yes/no): ") 
        if use_default:
            products = get_default_products()
        else:
            num_products = int(input("How many Shopping products you wanted to Add? "))
            for _ in range(num_products):
                products.append(input_product())

        while True:
            print("\nAvailable Products:")
            display_products(products)

            print("\nYour Cart:")
            display_cart(cart)

            choice = input("Choose an option: Add/Update/Remove/Checkout/Quit: ").lower()

            if choice == "add":
                product_name = input("Enter product name from Available Products to add: ").strip()
                selected_product = next((p for p in products if p.name.lower() == product_name.lower()), None)
                if selected_product:
                    if selected_product.available:
                        cart.add_product(selected_product)
                        print(f"Added {product_name} to the cart.")
                    else:
                        print(f"Product '{product_name}' is not available.")
                else:
                    print("Product not found.")

            elif choice == "update":
                product_name = input("Enter product name to update quantity: ").strip()
                quantity = int(input("Enter new quantity: "))
                found = False
                for item in cart.items:
                    if item.name.lower() == product_name.lower():
                        if item.bogo:
                            #BOGO : BUY 1 GET 1 FREE
                            # Double the entered quantity for BOGO products
                            item.quantity = quantity * 2
                            print(f"Updated {product_name} quantity to {item.quantity}.")
                        else:
                            # Set as entered for non-BOGO products
                            item.quantity = quantity
                            print(f"Updated {product_name} quantity to {quantity}.")
                        found = True
                        break
                if not found:
                    print("Product not found in the cart.")

            elif choice == "remove":
                product_name = input("Enter product name to remove from cart: ").strip()
                remove_one_unit = input("Remove one unit only? (yes/no): ").lower() == 'yes'
                cart.remove_product(product_name, remove_one_unit)
                print(f"Updated cart after removing {product_name}.")

            elif choice == "checkout":
                display_checkout_summary(cart)
                shop_again = input_yes_no("\nWould you like to shop again? (yes/no): ")
                if not shop_again:
                    print("Thank you for shopping, see you soon.")
                    break   # Exit the program

                # Determine if a new cart should be started
                cart_option = input("Start with a fresh cart? (yes/no): ").lower()
                if cart_option == "yes":
                    cart = Cart()  # Start a fresh cart

                # Determine if default products should be used again
                use_default = input("Would you like to use default Shopping products for the new session? (yes/no): ").lower()
                if use_default != "yes":
                    products = []  # Reset products
                    num_products = int(input("How many Shopping products are available? "))
                    for _ in range(num_products):
                        products.append(input_product())
                else :
                    products = get_default_products()

            elif choice == "quit":
                    print("Happy Shopping!!!!")
                    break

            else:
                print("Invalid option. Please try again.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
       

if __name__ == "__main__":
    main()



