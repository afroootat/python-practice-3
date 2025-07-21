# A dictionary with fruit names and a tuple of (price per unit, quantity)
fruit_stock = {
    "apple": (200, 5),
    "banana": (100, 8),
    "watermelon": (300, 10),
    "orange": (150, 7),
    "strawberry": (250, 9)
}

# Looping through the dictionary to calculate and print the cost of each fruit
for key, value in fruit_stock.items():
    # value[0] is the price, value[1] is the quantity
    print(f"{key} costs {value[0] * value[1]}")