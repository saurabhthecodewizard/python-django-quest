my_list = [1, 2, 3, 'STRING', 100.001]

print(my_list)  # [1, 2, 3, 'STRING', 100.001]

print(len(my_list))

print(my_list[3])

new_list = ['new', 'list']

concatenated_list = my_list + new_list

print(concatenated_list)  # [1, 2, 3, 'STRING', 100.001, 'new', 'list']

concatenated_list[0] = 'NEW IN CAPS'

print(concatenated_list)  # ['NEW IN CAPS', 2, 3, 'STRING', 100.001, 'new', 'list']

concatenated_list.append('appended item')

print(concatenated_list)  # ['NEW IN CAPS', 2, 3, 'STRING', 100.001, 'new', 'list', 'appended item']

popped_item = concatenated_list.pop()

print(popped_item)  # appended item

print(concatenated_list)  # ['NEW IN CAPS', 2, 3, 'STRING', 100.001, 'new', 'list']

popped_item_index = concatenated_list.pop()

print(popped_item_index)  # list

print(concatenated_list)  # ['NEW IN CAPS', 2, 3, 'STRING', 100.001, 'new']

char_list = ['a', 'd', 'f', 'g', 'h', 'b', 'c']
num_list = [4, 6, 5, 7, 8, 1, 3, 2, 9]

print(char_list)  # ['a', 'd', 'f', 'g', 'h', 'b', 'c']

none_list = char_list.sort()

print(none_list)  # None

print(char_list)  # ['a', 'b', 'c', 'd', 'f', 'g', 'h']

num_list.sort()

print(num_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_list.reverse()

print(num_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
