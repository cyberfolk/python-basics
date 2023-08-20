import json

# --- From JSON to dict -------------------------

x = '{"name": "luca", "lastname": "rossi", "age": 25}'  # This is a str a format json
y = json.loads(x)   # cast to dict
print(x)
print(type(x))  # str
print(y)
print(type(y))  # dict

# --- From dict to JSON -------------------------

a = {
    "name": "luca",
    "lastname": "rossi",
    "age": 25,
    "hobby": ["code","RPG", "Motors", "Run"],
    "money": 234.45,
    "employed": False,
    "married": None
}  # dict
b = json.dumps(a, indent=4, sort_keys=True)   # cast to json

print(a)
print(type(a))  # dict
print(b)
print(type(b))  # str



