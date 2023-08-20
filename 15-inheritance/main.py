class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def greet(self, user):
        print("Hello " + user + " I'm " + self.name)


class Teacher(Person):
    def __init__(self, name, lastname, course):
        super().__init__(name, lastname)
        self.course = course

    def greet(self, user):
        print("Hello " + user + " I'm " + self.name + " your " + self.course + "teacher")


persona1 = Person("Luca", "Rossi")
teacher1 = Teacher("Mario", "Verdi", "math")
teacher1.greet("User01")

del persona1.name
# persona1.greet("User01")  # Error name was deleted
