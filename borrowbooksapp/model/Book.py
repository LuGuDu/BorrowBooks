class Book:

    def __init__ (self, isbn, name, publisher):
        self.isbn = isbn
        self.name = name
        self.publisher = publisher

    def get_json(self):
        return {
            'isbn': self.isbn,
            'name': self.name,
            'publisher': self.publisher
        }

    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_publisher(self):
        return self.publisher
    
    def set_publisher(self, publisher):
        self.publisher = publisher

    def to_string(self):
        return "Book [id: " + self.isbn + ", name: " + self.name + ", publisher: " + self.publisher + "]"
    
