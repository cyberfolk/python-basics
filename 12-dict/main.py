persona = {
    "name": "Luca",
    "lastname": "Rossi",
    "age": "22",
    "address": {
        "nation": "Italia",
        "region": "Calabria",
        "city": "Catanzaro"
    }
}

print(persona.get("nome"))  # Luca
print(persona.keys())  # List of all keys
print(persona.items())  # List of tuple

print(persona['name'])

persona['school'] = "A. Moro"
print(persona)
persona.update({"school": "A. Moroso"})
print(persona)

persona.pop("name")
print(persona)

print("\nSHOW KEYS")
for x in persona:
    print(x)

print("\nSHOW VALUES")
for x in persona.values():
    print(x)

print(persona["address"]["city"])