cities = ("Milano", "Torino", "Bologna", "Bologna")  # List of constant element
print(cities)
print(cities[1])

# cities[0] = "Napoli" # Error cant modify
# cities[0].append("Napoli")    # Error cant modify

x = list(cities)
x.append("Napoli")
print(x)

cities = tuple(x)  # rewrite tuple with new tuple who contains new element
print(cities)

# Unpack
(a, b, c, d, e) = cities
print(a)
print(b)
print(c)
print(d)
print(e)

print(cities.index("Bologna"))  # return index of Bologna: 4
print(cities.index("Bologna"))  # count repetition of Bologna: 2
