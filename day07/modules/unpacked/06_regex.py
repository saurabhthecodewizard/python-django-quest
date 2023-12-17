import re

text = 'The phone number is 9999888877 phone'

print('phone' in text)

pattern = 'phone'

print((re.search(pattern, text)))

pattern = 'NOT IN TEXT'

print((re.search(pattern, text)))

pattern = 'phone'

match = re.search(pattern, text)

print(match)
print(match.span())
print(match.start())
print(match.end())

matches = re.findall('phone', text)

print(matches)

for match in re.finditer('phone', text):
    print(match.group())

phone = re.search(r'\d\d\d\d\d\d\d\d\d\d', text)

print(phone)
print(phone.group())

phone = re.search(r'\d{10}', text)

print(phone)
print(phone.group())

phone_pattern = re.compile(r'(...s) (\d{10}) (phone)')

phone = re.search(phone_pattern, text)
print(phone.group(1))
print(phone.group(2))

print(re.findall(r'^\d', '2 is a number'))  # starts with
print(re.findall(r'\d$', 'The number is 2'))  # ends with

phrase = 'A string 2 with random 345 numbers 56'
pattern = r'[^\d]+'

print(re.findall(pattern, phrase))
