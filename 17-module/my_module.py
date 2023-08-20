class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def greet(self, user):
        print("Hello " + user + " I'm " + self.name)


person1 = Person("luca", "rossi")
