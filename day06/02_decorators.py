def decorator(func):
    def wrap():
        print('Some extra code before the original function')

        func()

        print('Some extra code after the original function')

    return wrap


def hello():
    print('Hello')


decorator(hello)()


@decorator
def need_decorator():
    print('Need a decorator')


need_decorator()
