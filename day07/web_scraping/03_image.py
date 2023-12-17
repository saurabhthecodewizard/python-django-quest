import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)")

soup = bs4.BeautifulSoup(result.text, 'lxml')

image = soup.select('.mw-file-element')[1]

print(image['src'])

image_url = image['src']

image_link = requests.get('https:' + image_url)

print(image_link.content)

f = open('scraped_image.jpg', 'wb')
f.write(image_link.content)
f.close()
