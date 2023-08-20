cities = ["Milano", "Torino", "Bologna", "Bologna"]

print(cities)

cities[2] = "Venezia"
print(cities)

print(cities[1:3])

cities.insert(1,"Salerno")
print(cities)

cities.remove("Bologna")
print(cities)

cities.pop(1)
print(cities)

print(cities[-3])   # Start to end list

print(len(cities))
