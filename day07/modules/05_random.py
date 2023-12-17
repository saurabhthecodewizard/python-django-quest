import random

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

my_list = list(range(1, 20))

print(random.choice(my_list))
print(random.choices(population=my_list, k=7))

print(random.uniform(a=0, b=45))

random.seed(101)

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
