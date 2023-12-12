my_dictionary = {
    'apple': 50,
    'grape': 60,
    'orange': 20,
    'milk, curd': [30, 25],
    'nested': {
        'cream': 40,
        'skim milk': 80
    }
}

print(my_dictionary)  # {'apple': 50, 'grape': 60, 'orange': 20, 'milk, curd': [30, 25], 'nested': {'cream': 40,
# 'skim milk': 80}}

print(my_dictionary['grape'])  # 60

print(my_dictionary['milk, curd'])  # [30, 25]

print(my_dictionary['milk, curd'][1])  # 25

print(my_dictionary['nested']['cream'])  # 40

my_dictionary[20] = 'new'

print(my_dictionary)  # {'apple': 50, 'grape': 60, 'orange': 20, 'milk, curd': [30, 25], 'nested': {'cream': 40,
# 'skim milk': 80}, 20: 'new'}

print(my_dictionary.keys())  # dict_keys(['apple', 'grape', 'orange', 'milk, curd', 'nested', 20])

print(my_dictionary.values())  # dict_values([50, 60, 20, [30, 25], {'cream': 40, 'skim milk': 80}, 'new'])

print(my_dictionary.items())  # dict_items([('apple', 50), ('grape', 60), ('orange', 20), ('milk, curd', [30, 25]), ('nested', {'cream': 40, 'skim milk': 80}), (20, 'new')])
