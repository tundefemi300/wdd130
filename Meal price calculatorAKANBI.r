Meal price calculator
# Meal Price Calculator
# Creativity: Added an optional tip percentage to calculate a full restaurant-style total.

# Ask for meal prices
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

# Ask for number of meals
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute subtotal
subtotal = (child_price * num_children) + (adult_price * num_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

# Ask for sales tax rate
tax_rate = float(input("\nWhat is the sales tax rate? "))

# Compute sales tax
sales_tax = subtotal * (tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Ask for tip (creative addition)
tip_rate = float(input("Enter tip percentage (enter 0 if none): "))
tip_amount = subtotal * (tip_rate / 100)
print(f"Tip: ${tip_amount:.2f}")

# Compute total
total = subtotal + sales_tax + tip_amount
print(f"Total: ${total:.2f}")

# Ask for payment
payment = float(input("\nWhat is the payment amount? "))

# Compute change
change = payment - total
print(f"Change: ${change:.2f}")

print("\nThank you for dining with us!")
