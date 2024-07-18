class Base:
    def __init__(self) -> None:
        self._a = 2

    
class Derived(Base):
    def __init__(self):
        Base.__init__(self)

        print("Calling the protected attribute from outside the class: ",self._a)

        self._a = 3
        print("Modify the variable outside the class: ",self._a)


obj1 = Derived()
obj2 = Base()


print(obj1._a)
print(obj2._a)
        