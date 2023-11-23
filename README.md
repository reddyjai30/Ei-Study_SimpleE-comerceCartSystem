# Ei-study Coding Assignment
##### Name: Jai Prakash Reddy D 
##### R.no: CB.EN.U4CSE20027
###### Mail: reddyjai30@gmail.com



# Simple E-commerce Cart System Programming Exercise [PYTHON]

## Overview

This Python program simulates a simple e-commerce cart system. Users can Add, Update, and Remove products, apply discounts or BOGO (Buy One Get One Free) offers, and checkout to see the total bill. The program uses a console-based interface.

------  


## Getting Started

### Prerequisites

- **Python 3.x**: Install from [python.org](https://www.python.org/downloads/).
- **PrettyTable Library**: A Python library for displaying tabular data in ASCII table format.

- **Install**: Install it using pip
  ```bash
  pip install prettytable

Ensure all the .py files (main.py, product.py, discount_strategy.py, cart.py, ui_helpers.py, product_input.py) are downloaded and saved in the same directory.


### Running the Program 

- **Execute the Program**: Run the following command
  ```bash
  python3 main.py
  OR
  python main.py
  ```
  
------  


## Usage

### Program Flow

- **Choose Product Source**: Decide to use either default products or input your own.
- **Product Management**:
    * For custom products, enter details(name, price, availability, promotion type).
    * Default products are loaded automatically if chosen.
- **Shopping Cart Operations**: Add, update quantities, or remove products from the cart.
- **Checkout**: View a summary of cart items and the total bill.
- **Repeat or Exit**: Decide to shop again or exit the program.



## Example Inputs and Outputs
* Start the Program:
  ```bash
  Would you like to use default products? (yes/no): yes
  ```
* Add a Product:
  ```bash
  Choose an option: Add/Update/Remove/Checkout/Quit: add
  Enter product name to add: Laptop
  ```
  ###### Expected Output:
  ```bash
  Added Laptop to the cart.
  ```
* Update Product Quantity:
  ```bash
  Choose an option: Add/Update/Remove/Checkout/Quit: update
  Enter product name to update quantity: Laptop
  Enter new quantity: 2
  ```
  ###### Expected Output:
  ```bash
  Updated Laptop quantity to 2.
  ```
* Remove a Product:
  ```bash
  Choose an option: Add/Update/Remove/Checkout/Quit: remove
  Enter product name to remove from cart: Headphones
  Remove one unit only? (yes/no): no
  ```
  ###### Expected Output:
  ```bash
  Updated cart after removing Headphones.
  ```
* Checkout:
  ```bash
  Choose an option: Add/Update/Remove/Checkout/Quit: checkout
  ```
  ###### Expected Output:
  ```bash
  Cart Items: You have 2 Laptops in your cart.
  Total Bill: Your total bill is $2000.0.
  ```
* Repeat or Exit:
  ```bash
  Would you like to shop again? (yes/no): no
  ```
  ###### Expected Output:
  ```bash
  Thank you for shopping, see you soon.
  ```


------

## Discounted Products and BOGO Strategies
- **Discounted Products**: Apply a percentage discount to products. For example, a 10% discount on a $1000 laptop makes its price $900.
- **BOGO (Buy One Get One Free)**:
  * Adding Products: When a BOGO product is added to the cart, its quantity is doubled for display but billed for only half (rounded up). For instance,          adding 1 BOGO product shows 2 in the cart but charges for 1.
  * Updating Quantity: Updating a BOGO product also updates in pairs. For example, setting the quantity to 2 actually adds 4 to the cart but bills for 2.
  * Checkout Calculation: The cart calculates the total considering the BOGO offer. Only half the quantity (rounded up) of BOGO products is charged.
  * Removing Products: Removing a BOGO product decreases it in pairs. Selecting to remove one unit of a BOGO product removes two from the cart.


## Example Inputs and Outputs
- **BOGO Example** :
  * Add a BOGO product named "Headphones" priced at $150.
  * On adding 1, the cart shows 2 Headphones but charges for 1 ($150).
  * On updating quantity to 2, the cart shows 4 Headphones but charges for 2 ($300).
  * On removing one unit, 2 Headphones are removed from the cart.

```bash
(base) jai@Jais-MacBook-Air ecom-test % python3 main.py
Would you like to use default products? (yes/no): no
How many products are available? 3
Enter product name: Headphones
Enter product price: 150
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): bogo
Enter product name: Laptop
Enter product price: 500
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): discount
Enter discount percentage: 10
Enter product name: Pendrive
Enter product price: 350
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): none
```
## ADD

### Here since Headphones is a Buy 1 Get 1 free product , if we add 1 then in the cart 1+1 is added as 1 is for free and the price will reamin same $150
```bash
Choose an option: Add/Update/Remove/Checkout/Quit: add
Enter product name to add: Headphones
Added Headphones to the cart.

Available Products:
+--------------+--------+--------------+----------+------------+
| Product Name | Price  | Availability | Discount | BOGO Offer |
+--------------+--------+--------------+----------+------------+
|  Headphones  | $150.0 |     Yes      |   N/A    |    Yes     |
|    Laptop    | $500.0 |     Yes      |  10.0%   |    N/A     |
|   Pendrive   | $350.0 |     Yes      |   N/A    |     No     |
+--------------+--------+--------------+----------+------------+

Your Cart:
+--------------+--------+----------+
| Product Name | Price  | Quantity |
+--------------+--------+----------+
|  Headphones  | $150.0 |    2     |
+--------------+--------+----------+

Choose an option: Add/Update/Remove/Checkout/Quit: checkout
Cart Items: You have 2 Headphoness in your cart.
Total Bill: Your total bill is $150.0.
```

## Update

### Since "Headphones" are a BOGO product, updating the quantity to 2 results in 4 units displayed in the cart, but only 2 units are billed.

```bash
Your Cart:
+--------------+--------+----------+
| Product Name | Price  | Quantity |
+--------------+--------+----------+
|  headphones  | $150.0 |    2     |
+--------------+--------+----------+
Choose an option: Add/Update/Remove/Checkout/Quit: update
Enter product name to update quantity: headphones
Enter new quantity: 2
Updated headphones quantity to 4.

Available Products:
+--------------+--------+--------------+----------+------------+
| Product Name | Price  | Availability | Discount | BOGO Offer |
+--------------+--------+--------------+----------+------------+
|  headphones  | $150.0 |     Yes      |   N/A    |    Yes     |
+--------------+--------+--------------+----------+------------+

Your Cart:
+--------------+--------+----------+
| Product Name | Price  | Quantity |
+--------------+--------+----------+
|  headphones  | $150.0 |    4     |
+--------------+--------+----------+
```



## Remove

### Here since we are removing a BOGO free product that means if we remove 1 then 1+1 qunatity will be removed since the other thing is FREE!!!

```bash
Your Cart:
+--------------+--------+----------+
| Product Name | Price  | Quantity |
+--------------+--------+----------+
|  Headphones  | $150.0 |    2     |
+--------------+--------+----------+
Choose an option: Add/Update/Remove/Checkout/Quit: remove
Enter product name to remove from cart: Headphones
Remove one unit only? (yes/no): yes
Updated cart after removing Headphones.

Your Cart:
+--------------+-------+----------+
| Product Name | Price | Quantity |
+--------------+-------+----------+
+--------------+-------+----------+
```


## Checkout

### Here is the checkout example where I have included all types of products (discount, BOGO, none) 

```bash
(base) jai@Jais-MacBook-Air ecom-test % python3 main.py
Would you like to use default products? (yes/no): no
How many products are available? 3
Enter product name: Headphones
Enter product price: 150
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): bogo
Enter product name: Laptop
Enter product price: 250
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): discount
Enter discount percentage: 15
Enter product name: TV
Enter product price: 450
Is the product available (yes/no)? yes
Choose promotion type (discount/bogo/none): none

Available Products:
+--------------+--------+--------------+----------+------------+
| Product Name | Price  | Availability | Discount | BOGO Offer |
+--------------+--------+--------------+----------+------------+
|  Headphones  | $150.0 |     Yes      |   N/A    |    Yes     |
|    Laptop    | $250.0 |     Yes      |  15.0%   |    N/A     |
|      TV      | $450.0 |     Yes      |   N/A    |     No     |
+--------------+--------+--------------+----------+------------+

Your Cart:
+--------------+-------+----------+
| Product Name | Price | Quantity |
+--------------+-------+----------+
+--------------+-------+----------+
Choose an option: Add/Update/Remove/Checkout/Quit: add
```
### AFTER ADDING ALL THE PRODUCTS TO THE CART AND CHECKING OUT !!
#### Total price is calculated including the DISCOUNTED product (Laptop - 15%) too calculated and shownen in the TOTAL BILL

##### Since Headphones is a BOGO (Buy 1 Get 1 Free Product) the quantity added in the cart is 2 but the total price is : $ 150
##### Laptop product have a discount of 15% of its price ($ 250) which is : 

```bash
Available Products:
+--------------+--------+--------------+----------+------------+
| Product Name | Price  | Availability | Discount | BOGO Offer |
+--------------+--------+--------------+----------+------------+
|  Headphones  | $150.0 |     Yes      |   N/A    |    Yes     |
|    Laptop    | $250.0 |     Yes      |  15.0%   |    N/A     |
|      TV      | $450.0 |     Yes      |   N/A    |     No     |
+--------------+--------+--------------+----------+------------+

Your Cart:
+--------------+--------+----------+
| Product Name | Price  | Quantity |
+--------------+--------+----------+
|  Headphones  | $150.0 |    2     |
|    Laptop    | $250.0 |    1     |
|      TV      | $450.0 |    1     |
+--------------+--------+----------+

Choose an option: Add/Update/Remove/Checkout/Quit: checkout
Cart Items: You have 2 Headphoness, 1 Laptop, 1 TV in your cart.
Total Bill: Your total bill is $812.5.
```

## Exiting

```bash
Would you like to shop again? (yes/no): no
Thank you for shopping, see you soon.
```

# Shop Again Feature
The program includes a `shop again` feature, enhancing the user experience by allowing for continuous shopping sessions without the need to restart the program. This feature is particularly user-friendly and simulates a real-world shopping scenario.

## Choosing Cart Items for the New Session
After completing a shopping session and checking out, users are prompted with the question:

```bash
Would you like to shop again? (yes/no):
```
If the user chooses `yes`, they are presented with two options:
- **Start with a Fresh Cart**:
  * If the user wants to start over with an empty cart, they can choose this option.
This is useful if the user wishes to have a completely new shopping experience without the influence of previous selections.

  * This is useful if the user wishes to have a completely new shopping experience without the influence of previous selections.

- **Continue with Existing Cart Items**:
  * Users can choose to retain the items from their previous shopping session in their cart.
  * This option is practical if the user wants to add more items to their existing selection or wasn't ready to checkout during the previous session.


## Choosing Available Products for the New Session
Furthermore, users have the choice to select the type of products available for the new session:

- **Use Default Products**:
  * The program offers a set of default products that users can choose to shop from again.
  * This option saves time for users who prefer shopping from a predefined list of items.

- **Add New Available Products**:
  * Users can opt to enter new products, enhancing the diversity of available items.
  * This option caters to users who seek a customized shopping experience or want to explore different product combinations.


## Example Interaction

```bash
Would you like to shop again? (yes/no): yes
Start with a fresh cart? (yes/no): no
Would you like to use default products for the new session? (yes/no): yes

Available Products:
+--------------+-------+--------------+----------+------------+
| Product Name | Price | Availability | Discount | BOGO Offer |
+--------------+-------+--------------+----------+------------+
|    Laptop    | $1000 |     Yes      |   10%    |    N/A     |
|  Headphones  |  $150 |     Yes      |   N/A    |    Yes     |
|  Smartphone  |  $800 |     Yes      |    5%    |    N/A     |
|   Charger    |  $20  |     Yes      |   N/A    |     No     |
|    Camera    |  $500 |     Yes      |   N/A    |    Yes     |
+--------------+-------+--------------+----------+------------+

Your Cart:
+--------------+-------+----------+
| Product Name | Price | Quantity |
+--------------+-------+----------+
|    Laptop    | $1000 |    1     |
|    Camera    |  $500 |    2     |
+--------------+-------+----------+
Choose an option: Add/Update/Remove/Checkout/Quit: quit
Happy Shopping!!!!
```
###### The cart and available products are then displayed, allowing the user to continue shopping based on their selections.



-------


# CONCLUSION

## Implementation of Design Patterns and OOP Principles
- **Strategy Pattern (Behavioral Pattern)**: The use of `DiscountStrategy` and its subclasses like `PercentageOffStrategy` exemplifies the Strategy Pattern. This pattern allows for the flexible application of different discount strategies, adhering to the open/closed principle by being open for extension but closed for modification.
  
- **Prototype Pattern (Creational Pattern)**: The `clone` method in the `Product` class demonstrates the Prototype Pattern. It allows for cloning product objects, especially useful when adding products to the cart, ensuring that each cart item is a separate instance.
  
- **Encapsulation and Inheritance**: The base Product class and its subclass SpecialProduct demonstrate encapsulation and inheritance. SpecialProduct inherits from Product and extends its functionality to handle discounts, thus promoting code reusability and the single responsibility principle.


## Functional Requirements Fulfillment
- **Product Display**: The program displays a list of products with their attributes, meeting the first functional requirement.
  
- **Cart Functionality**: Users can `add products to the cart`, `view the cart`, `update product quantities`, and `remove items from the cart`, addressing the core functionalities of an e-commerce system.
  
- **Total Bill Calculation**: The cart calculates and displays the total bill, considering discounts and BOGO offers, aligning with the requirement to provide a checkout functionality.


## Global Convention and Code Quality
- **Code Conventions**: The code follows `PEP 8` standards, Python's primary coding convention, ensuring readability and maintainability.

- **Logging and Exception Handling**: While the provided snippets show explicit logging or complex exception handling, robust logging mechanism and comprehensive error handling would further align the project with best practices.


## Performance and Edge Case Handling
- **Performance**: The code is optimized for performance in typical use cases, with efficient loops and condition checks. However, for very large numbers of products or cart items, further optimization and testing may be required.

- **Edge Case Handling**: The program handles various edge cases, such as updating the quantity of BOGO products and ensuring the cart displays the correct number of items. Additional edge cases, especially around invalid user inputs and product availability, are more rigorously handled to enhance robustness.


## Time Complexity and Accuracy
- **Time Complexity**: Most operations (like adding, updating, or removing products) are linear in time complexity `(O(n))`, which is efficient for typical use-case scenarios of an `e-commerce cart system`.

- **Accuracy**: The calculations for discounts and Buy 1 Get 1 Free `BOGO offers` are accurate, ensuring that the total bill reflects the correct amounts.


## Code Walkthrough and SOLID Principles
- **Code Walkthrough**: The structured and modular design of the code makes it easier to walk through and explain the architectural decisions and design patterns used.

- **SOLID Principles**: The program largely adheres to SOLID principles, with clear examples of single responsibility, open/closed, and `Liskov` substitution principles through its class design and pattern usage.
