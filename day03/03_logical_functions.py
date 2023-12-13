def is_even(num):
    result = num % 2 == 0
    return result


def all_even(num):
    result = []
    for i in range(num):
        if i % 2 == 0:
            result.append(i)
        else:
            pass
    return result


print(is_even(78))
print(is_even(79))

print(all_even(20))
