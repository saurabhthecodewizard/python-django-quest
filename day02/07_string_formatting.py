string = 'This is a string {} {}{}'.format('with', 'format', '.')

print(string)

string_index_format = 'This is a string {2} {1} {0}'.format('with', 'format', '.')

print(string_index_format)

string_same_index_format = 'This is a string {2} {2} {2}'.format('with', 'format', '.')

print(string_same_index_format)

string_format_with_variable = 'This is a string {format} {format}'.format(with_var='with', format='format')

print(string_format_with_variable)

x, y = 'some', 'more'

print('Give me %s %s.' % (x, y))
