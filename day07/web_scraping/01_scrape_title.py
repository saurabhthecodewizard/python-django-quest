import requests
import bs4

result = requests.get("https://www.example.com/")

# print(type(result))

soup = bs4.BeautifulSoup(result.text, 'lxml')

# print(soup)

print(soup.select('title')[0].getText())

print(type(soup.select('p')[0]))
