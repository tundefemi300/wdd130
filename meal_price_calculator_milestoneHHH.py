# Meal Price Calculator - Milestone Version
# This program asks for meal prices and quantities, then computes the subtotal.

# Ask for the price of a child's and an adult's meal
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for the number of children and adults
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Display the subtotal
print("Subtotal:", subtotal)
