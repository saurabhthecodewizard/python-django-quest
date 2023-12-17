from PIL import Image

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

blue.putalpha(100)

blue.paste(im=red, box=(0, 0), mask=red)

blue.save('purple_color.png')
