repeat = True
person = {
    "name": "luca",
    "lastname": "rossi"
}
operations = ("Add", "Modify", "Delete", "Stop", "Read")


def start():
    print("Operation list: Add, Modify, Delete, Stop, Read")
    operation = input("> What do you do? ").capitalize()
    if operation == operations[0]:
        add(input("> Add new field. (key:value) "))
    if operation == operations[1]:
        modify(input("> Which field do you want modify? (key:new-value)  "))
    if operation == operations[2]:
        delete(input("> Which field do you want delete? (key) "))
    if operation == operations[3]:
        global repeat
        repeat = False
    if operation == operations[4]:
        print(person)


def add(params):
    splitted = params.split(":")
    key = splitted[0]
    value = splitted[1]
    person[key] = value


def modify(params):
    splitted = params.split(":")
    key = splitted[0]
    value = splitted[1]
    person[key] = value


def delete(param):
    person.pop(param)


while repeat:
    start()
