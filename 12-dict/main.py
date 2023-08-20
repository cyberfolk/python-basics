person = {
    "name": "Luca",
    "lastname": "Rossi",
    "age": "22",
    "address": {
        "nation": "Italia",
        "region": "Calabria",
        "city": "Catanzaro"
    }
}

print(person.get("nome"))  # Luca
print(person.keys())  # List of all keys
print(person.items())  # List of tuple

print(person['name'])

person['school'] = "A. Moro"
print(person)
person.update({"school": "A. Moroso"})
print(person)

person.pop("name")
print(person)

print("\nSHOW KEYS")
for x in person:
    print(x)

print("\nSHOW VALUES")
for x in person.values():
    print(x)

print(person["address"]["city"])