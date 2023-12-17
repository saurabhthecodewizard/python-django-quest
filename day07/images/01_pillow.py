from PIL import Image

mac = Image.open('example.jpg')

print(type(mac))
print(mac.size)
print(mac.format_description)
# print(mac.show())

pencils = Image.open('pencils.jpg')

x = 0
y = 0
w = 1950 / 3
h = 1300 / 10

pencils = pencils.crop((x, y, int(w), int(h)))

pencils.show()

pencils.rotate(90)
