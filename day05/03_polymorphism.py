class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'


tom = Dog('Tom')
niko = Cat('Niko')

print(tom.speak())
print(niko.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(tom)
pet_speak(niko)
