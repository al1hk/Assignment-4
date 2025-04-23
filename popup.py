# Dictionary of fruits and their prices
fruit_prices = {
    "apple": 2.0,
    "banana": 1.5,
    "orange": 1.2,
    "grapes": 3.0,
    "mango": 2.5
}

total_cost = 0

# Loop through each fruit and ask how many the user wants
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many {fruit}s would you like to buy? "))
    cost = price * quantity
    total_cost += cost

# Print the total cost
print(f"\nThe total cost of your fruits is ${total_cost:.2f}")
