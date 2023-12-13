def myfunc(p, q):
    return sum((p, q)) * 0.05


def myfunc_more(p, q, r=0, s=0):
    return sum((p, q, r, s)) * 0.05


def args_func(*arguments):
    """
    arguments are tuple
    """
    return sum(arguments) * 0.05


def print_args(*arguments):
    for arg in arguments:
        print(arg)


def print_dictionary_kwargs(**kwargs):
    """
    kwargs are dictionary
    """
    print(kwargs)


def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


print(myfunc(50, 50))

print(myfunc_more(50, 20, 30))

print(args_func(30, 30, 40))

print_args(30, 30, 40)

print(print_dictionary_kwargs(first=10, second=20, third=30))

args_and_kwargs(10, 20, 30, first=10, second=20, third=30)
