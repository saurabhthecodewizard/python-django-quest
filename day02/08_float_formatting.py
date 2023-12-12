result = 100/777

print(result)  # 0.1287001287001287

print("The result is: {}".format(result))  # The result is: 0.1287001287001287

print("The result is: {result:1.3}".format(result=result))  # The result is: 0.129

print("The result is: {result:10.3}".format(result=result))  # The result is:      0.129

print("The result is: {result:10.7}".format(result=result))  # The result is:  0.1287001

print('The result is %s' % result)  # 0.1287001287001287

print('The result is %d' % result)  # 0

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))  # Fruit    | Quantity

print('{0:8} | {1:9}'.format('Apples', 3.))  # Apples   |       3.0

print('{0:8} | {1:9}'.format('Oranges', 10))  # Oranges  |        10
