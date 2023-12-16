def hello(name='Python'):
    print(f'Hello function has been executed')

    def greet():
        return '\tThis is the greet function inside hello'

    def welcome():
        return '\tThis is the welcome function inside hello'

    # print(greet())
    # print(welcome())
    # print('End of the hello function')

    if name == 'Python':
        return greet
    else:
        return welcome


# greet = hello
#
# print(greet())
#
# del hello
#
# print(greet())

my_func = hello()

print(my_func())


def func_as_param(func):
    print('In function as a parameter function')
    print(func()())


func_as_param(hello)
