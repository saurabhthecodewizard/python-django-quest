import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# print(base_url.format(20))

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')

products = soup.select('.product_pod')

# print(products[0].select('a')[1]['title'])

two_star_titles = []

for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    books = soup.select('.product_pod')

    for book in books:
        if len(soup.select('.star-rating.Two')):
            book_title = book.select('a')[1]['title']
            print(book_title)
            two_star_titles.append(book_title)


print(two_star_titles)
