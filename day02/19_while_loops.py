x = 0

while x < 3:
    print(f'Current value: {x}')
    x += 1
else:
    print(f'Value: {x} is excxeeded')

y = 0

while y < 5:
    if y == 1:
        y += 1
        continue
    elif y >= 3:
        break
    else:
        print(f'Value: {y}')
        y += 1
