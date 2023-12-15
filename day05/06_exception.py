try:
    result = 10 + '10'
except TypeError:
    print('Incorrect values!!')
else:
    print('Result is rendered')
finally:
    print('I am always gonna run')
