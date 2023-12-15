myset = set()

print(type(myset))


class Sample():
    pass


my_sample = Sample()

print(type(my_sample))


class Dog():
    # Class Object Attribute
    # Same for any instance of the class
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Method is a function inside the class
    def bark(self):
        print(f'{self.name} barked!!')

    def bark_times(self, number):
        print(f'{self.name} barked {number} times!!')


my_dog = Dog(breed='German Shepherd', name='Tom')

print(my_dog.name)

print(my_dog.species)

my_dog.bark()

my_dog.bark_times(4)


class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = radius + radius

    def circumference(self):
        return self.radius * Circle.pi * 2

    def area(self):
        return Circle.pi * self.radius * self.radius


my_circle = Circle(10)

print(my_circle.diameter)

print(my_circle.area())

print(my_circle.circumference())
