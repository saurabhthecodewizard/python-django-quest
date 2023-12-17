import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(result.text, 'lxml')

for item in soup.select('.vector-toc-text'):
    print(item.text)
