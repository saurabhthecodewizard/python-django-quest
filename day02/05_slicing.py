mystring = 'abcdefghijklmnopqrstuvwxyz'

print(mystring)

print(mystring[3:])  # skip first 3 -> start_index = 3

print(mystring[:3])  # take first 3 -> until index < 3

print(mystring[3:6])  # start  = 3 and start < 6

print(mystring[::])  # whole string -> same as mystring

print(mystring[::2])  # jump to every 2nd index from current index

print(mystring[3:9:2])  # start from index 3, until index less than 9 and get every 2nd index from current

print(mystring[::-1])  # start to end with negative 1st index
