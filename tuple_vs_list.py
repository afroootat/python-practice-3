# A list of colors
colors = ["Blue", "Green", "Red"]

# A tuple of animals
animals = ("Dog", "Cat", "Rabbit")

# Changing the second item in the list (allowed)
colors[1] = "Purple"

# Attempting to change the second item in the tuple (not allowed – will cause error)
# animals[1] = "Donkey"  #  This line will cause an error because tuples are immutable

# Printing the modified list
print(colors)

# Printing the original tuple (still unchanged)
print(animals)