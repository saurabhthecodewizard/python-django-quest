class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Override the address sharing method
    # Called whenever asked str(Book Instance)
    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book object has been deleted')


book = Book('Autobiography', 'Saurabh', 50)

print(str(book))

print(book)

print(len(book))

del book
9156062769