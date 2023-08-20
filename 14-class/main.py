class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def greet(self, user):
        print("Hello " + user + " I'm " + self.name)


persona1 = Person("Luca", "Rossi")
persona2 = Person("Mario", "Verdi")
persona2.greet("User01")

del persona1.name
# persona1.greet("User01")  # Error name was deleted
