from collections import Counter, defaultdict, namedtuple

my_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4]

c = Counter(my_list)
print(c)
print(c.most_common())
print(c.most_common(2))

print(Counter('aaaagrrgfgasdfgsfgdfs'))


dict = {
    'a': 10
}

print(dict['a'])

def_dec = defaultdict(lambda : 0)
def_dec['a'] = 10

print(def_dec['a'])
print(def_dec['f'])


my_tuple = (10, 20, 30)
print(my_tuple[1])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sam = Dog(age=5, breed='Husky', name='Sam')
print(sam)
