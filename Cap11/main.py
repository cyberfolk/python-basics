cities = {"Milano", "Torino", "Bologna", "Bologna"}
other_citied = {"Salerno", "Genova"}

# cities[1] # Error NOT Indexed

print(cities) # Printed in random order

cities.update(other_citied)
print(cities)

# cities.remove("Rome")   # Error: Rome don't exist
cities.discard("Rome")
