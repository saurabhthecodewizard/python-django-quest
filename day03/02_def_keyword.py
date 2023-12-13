def say_hello():
    print("Hello")


def say_name(name = 'Default'):
    print(f'{name}')


def add(p, q):
    return p + q


say_hello()

say_name('Saurabh')
say_name()

print(add(3, 4))

result = add(10, 11)

print(result)

print(add('10', '11'))

print(say_hello)
