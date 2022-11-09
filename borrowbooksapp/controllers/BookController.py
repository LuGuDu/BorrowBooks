import json

from model.Book import Book
from dao.BookDAO import BookDAO

book_dao = BookDAO()

def create_book(data, mongo):
    """Method to create a new book"""
    isbn = json.loads(data.decode())["isbn"]
    title = json.loads(data.decode())["title"]
    author = json.loads(data.decode())["author"]
    publisher = json.loads(data.decode())["publisher"]

    # Exceptions

    book = Book(isbn, title, author, publisher)
    book_dao.save(mongo, book.get_json())


def delete_book(data, mongo):
    """Method to delete an existing book"""
    isbn = json.loads(data.decode())["isbn"]

    #Exceptions

    book_dao.delete_by_isbn(mongo, isbn)


def update_book(data, mongo):
    """Method to update an existing book"""
    book_json = json.loads(data.decode())

    isbn = book_json["isbn"]
    title = book_json["title"]
    author = book_json["author"]
    publisher = book_json["publiser"]

    book = book_dao.get_by_isbn(mongo, isbn)

    #Exceptions

    book["title"] = title
    book["author"] = author
    book["publisher"] = publisher

    book_dao.update(mongo, book)


def get_books(mongo):
    """Method to obtains the books list"""
    book_list = book_dao.get_all(mongo)
    return book_list


def get_book(data, mongo):
    """Method to obtain a book"""
    isbn = json.loads(data.decode())["isbn"]
    book = book_dao.get_by_isbn(mongo, isbn)
    return book


def search_by(data, mongo):
    search_type = json.loads(data.decode())["type"]
    search_data = json.loads(data.decode())["data"]

    if search_type == "title":
        return_list = book_dao.get_by_title(mongo, search_data)
    elif search_type == "author":
        return_list = book_dao.get_by_author(mongo, search_data)
    else:
        return_list = book_dao.get_by_publisher(mongo, search_data)



