import csv

data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)

for line in data_lines[:20]:
    print(line)


csv_output = open('csv_output.csv', 'w', newline='')
csv_writer = csv.writer(csv_output, delimiter=',')

csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
csv_output.close()
