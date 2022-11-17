"""BookDAO class"""

class BookDAO:
    """Class with methods for books persistance"""

    def save(self, mongo, book):
        """Takes a book and save it on mongoDB"""
        mongo.books.insert_one(book)


    def get_all(self, mongo):
        """Returns all the books as list"""
        return list(mongo.books.find({}))


    def delete_by_isbn(self, mongo, isbn):
        """Takes a isbn and delete the book from mongoDB"""
        mongo.books.delete_one({"isbn": isbn})


    def get_by_isbn(self, mongo, isbn):
        """Returns all the books with same isbn"""
        return mongo.books.find_one({"isbn": isbn})


    def get_by_title(self, mongo, title):
        """Returns all the books with same title"""
        return list(mongo.books.find({"title": {"$regex" : title, "$options": "i"}}, sort=[("author", -1)]))


    def get_by_author(self, mongo, author):
        """Returns all the books with same author"""
        return list(mongo.books.find({"author": {"$regex" : author, "$options": "i"}}, sort=[("author", -1)]))


    def get_by_publisher(self, mongo, publisher):
        """Returns all the books with same publisher"""
        return list(mongo.books.find({"publisher": {"$regex" : publisher, "$options": "i"}}, sort=[("publisher", -1)]))


    def update(self, mongo, book):
        """Takes a book and update it on mongoDB"""
        mongo.books.update_one({'isbn': book['isbn']}, 
        {'$set': {'title': book['title'], 'author': book['author'], 
        'publisher': book['publisher'],}})
