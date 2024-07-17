'''
PROBLEM STATEMENT

Scenario:

You are tasked with developing a basic ecommerce application that handles various operations such as adding items to a cart, 
removing items from the cart, checking out. The application should also handle various types of exceptions gracefully, 
such as when a user tries to add a negative quantity of items remove items that are not in cart, or check out with empty cart.

Requirements:

Implement function for adding items to the cart, removing items from the cart, and checking out.
Handle exceptions for the following cases:

Adding a negative quantity of items.
Removing items that are not in the cart
Checking out with empty cart

Ensure that the application continues to run smoothly after an exception.

'''



'''
___________         _________                                                                           .__  .__               __  .__               
\_   _____/         \_   ___ \  ____   _____   _____   ___________   ____  ____    _____  ______ ______ |  | |__| ____ _____ _/  |_|__| ____   ____  
 |    __)_   ______ /    \  \/ /  _ \ /     \ /     \_/ __ \_  __ \_/ ___\/ __ \   \__  \ \____ \\____ \|  | |  |/ ___\\__  \\   __\  |/  _ \ /    \ 
 |        \ /_____/ \     \___(  <_> )  Y Y  \  Y Y  \  ___/|  | \/\  \__\  ___/    / __ \|  |_> >  |_> >  |_|  \  \___ / __ \|  | |  (  <_> )   |  \
/_______  /          \______  /\____/|__|_|  /__|_|  /\___  >__|    \___  >___  >  (____  /   __/|   __/|____/__|\___  >____  /__| |__|\____/|___|  /
        \/                  \/             \/      \/     \/            \/    \/        \/|__|   |__|                \/     \/                    \/ 

'''

print("\n\nWelcome to the E-Commerce store, Enjoy your shopping.")

def add_to_cart(cart, item, quantity):
    try:
        if quantity <= 0:
            raise ValueError
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item} to the cart.")
    except ValueError as e:
        print(f"Quantity of a item cannot be negative")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_from_cart(cart, item, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if item in cart:
            if cart[item] >= quantity:
                cart[item] -= quantity
                print(f"Removed {quantity} {item} from the cart.")
            else:
                print(f"Number of {item} in the cart is less than the specified quantity")
        else:
            print(f"{item} is not in the cart.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def checkout(cart):
    try:
        if not cart:
            raise ValueError("Cannot checkout with an empty cart.")
        

        total_items = sum(cart.values())
        total_cost = sum([prices[item] * cart[item] for item in cart])
        
        print(f"Checked out {total_items} items. Total cost: Rs{total_cost: }")
        cart.clear()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example prices dictionary (for reference)
prices = {
    "Laptop": 30000,
    "Smartphone": 15000,
    "Headphones": 1500,
    "Tablet": 50000,
    "Printer": 7000,
    "Camera": 7000,
    "Smartwatch": 2500,
    "External Hard Drive": 1000,
    "Gaming Console": 4000,
    "Wireless Router": 800,
    "Notebook": 10,
    "Pens": 50,
    "Sticky Notes": 300,
    "Calculator": 300,
    "Filing Folders": 100,
    "Scissors": 50,
    "Stapler": 25,
    "Marker": 25,
    "Whiteboard": 300
}

# Example usage with user input

cart = {}

while True:
    print(f"\n\nWe have the following items and the prices of the products:\n{prices}")
    print("\nPlease choose from the following operations:\n")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        item = input("Enter item name: ")
        try:
            if item not in prices:
                raise ValueError
        except ValueError as e:
            print("We dont have it currently")
            continue

        quantity = int(input("Enter quantity: "))
        add_to_cart(cart, item, quantity)
    elif choice == '2':
        try:
            if not cart:
                raise ValueError
        except ValueError as e:
            print("Cannot remove from empty cart")
            continue
    
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        remove_from_cart(cart, item, quantity)
    elif choice == '3':
        checkout(cart)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
