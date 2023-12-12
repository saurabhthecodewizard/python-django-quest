my_file = open('file.txt')

# my_file = open('file_not_found.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 'file_not_found.txt'

print(my_file.read())

print(my_file.read())

print(my_file.seek(0))

print(my_file.read())

print(my_file.seek(0))

print(my_file.readlines())

my_file.close()

with open('file.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('file.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)

# with open('file.txt', mode='w') as my_new_file:
#     contents = my_new_file.read()  # io.UnsupportedOperation: not readable
#
# print(contents)

# r -> read only
# w -> write only (will overwrite files or create new)
# a -> append only
# r+ -> reading and writing
# w+ -> overwriting and reading
