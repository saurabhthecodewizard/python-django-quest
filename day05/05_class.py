class Line:

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        return (((self.coordinate2[0] - self.coordinate1[0]) ** 2) + ((self.coordinate2[1] - self.coordinate1[1]) ** 2)) ** 0.5

    def slope(self):
        return (self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)

print(line.distance())
print(line.slope())


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def area(self):
        return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * (self.radius ** 2)


cylinder = Cylinder(2, 3)

print(cylinder.volume())
print(cylinder.area())


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f'{self.owner}: {self.balance}')


account = Account('Saurabh', 100)

account.show_balance()

account.deposit(550)

account.show_balance()

account.withdraw(600)

account.show_balance()
