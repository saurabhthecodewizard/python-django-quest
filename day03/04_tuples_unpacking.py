stock_prices = [('Google', 300), ('Apple', 700), ('Microsoft', 500)]

for company, price in stock_prices:
    print(f'{company} -> {price}')


def highest_stock_price(my_list: list[tuple[str, int]]):
    max_price = 0
    company_name_max = ''
    for company_name, stock_price in my_list:
        if stock_price > max_price:
            max_price = stock_price
            company_name_max = company_name
        else:
            pass
    return company_name_max, max_price


name, stock_prices = highest_stock_price(stock_prices)

print(f'Highest Stock: {name} -> {stock_prices}')
