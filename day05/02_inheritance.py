class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am an Dog")

    def bark(self):
        print("Barking!")


my_dog = Dog()

my_dog.who_am_i()
my_dog.eat()
my_dog.bark()
