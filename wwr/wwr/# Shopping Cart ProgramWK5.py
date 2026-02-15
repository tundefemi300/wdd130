# Shopping Cart Program
# Creativity: This version shows the number of items in the cart each time it is displayed
# and prevents crashes by handling invalid number or price inputs.

print("Welcome to the Shopping Cart Program!")

items = []
prices = []

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    # Add item
    if choice == "1":
        item = input("What item would you like to add? ")
        try:
            price = float(input(f"What is the price of '{item}'? "))
            items.append(item)
            prices.append(price)
            print(f"'{item}' has been added to the cart.")
        except ValueError:
            print("Invalid price. Item not added.")

    # View cart
    elif choice == "2":
        if len(items) == 0:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")
            print(f"Total items: {len(items)}")

    # Remove item
    elif choice == "3":
        if len(items) == 0:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")

            try:
                remove_index = int(input("Which item would you like to remove? "))
                remove_index -= 1  # convert to 0-based index

                if 0 <= remove_index < len(items):
                    items.pop(remove_index)
                    prices.pop(remove_index)
                    print("Item removed.")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Invalid input.")

    # Compute total
    elif choice == "4":
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    # Quit
    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid option. Please try again.")
