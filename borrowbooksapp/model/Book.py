class Book:

    def __init__ (self, isbn, title, author, publisher):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher

    def get_json(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'publisher': self.publisher
        }

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_publisher(self):
        return self.publisher
    
    def set_publisher(self, publisher):
        self.publisher = publisher

    def to_string(self):
        return "Book [isbn: " + self.isbn + ", title: " + self.title + ", author: " + self.author +", publisher: " + self.publisher + "]"
    
