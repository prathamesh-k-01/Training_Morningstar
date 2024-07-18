class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class child(Person):
    def __init__(self, firstname, lastname, year) -> None:
        super().__init__(firstname, lastname)
        self.graduation_year = year

baccha1 = child("Pratham", "Rawat")
baccha1.printname()
