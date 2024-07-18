class Animal:
    def make_sound(self):
        return "some sound"

class Dog(Animal):
    def make_sound(self):
        return "bark"
    

doggy = Dog()

print(doggy.make_sound())
