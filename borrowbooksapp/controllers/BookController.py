import json
from flask import abort as fabort, make_response

from model.Book import Book
from dao.BookDAO import BookDAO

from exceptions.BookNoExistsException import BookNoExistsException
from exceptions.BookAlreadyExistsException import BookAlreadyExistsException

book_dao = BookDAO()


def abort(status_code, message):
    """Method to abort the request"""
    data = {"message": message, "status_code": status_code}
    response = make_response(json.dumps(data))
    response.status_code = status_code
    response.content_type = 'application/json'
    fabort(response)


def create_book(data, mongo):
    """Method to create a new book"""
    isbn = json.loads(data.decode())["isbn"]
    title = json.loads(data.decode())["title"]
    author = json.loads(data.decode())["author"]
    publisher = json.loads(data.decode())["publisher"]

    try:
        if book_dao.get_by_isbn(mongo, isbn) is not None:
            raise BookAlreadyExistsException
    except BookAlreadyExistsException:
        print("Book already exists")
        abort(500, "Book already exists")

    book = Book(isbn, title, author, publisher)
    book_dao.save(mongo, book.get_json())


def delete_book(data, mongo):
    """Method to delete an existing book"""
    isbn = json.loads(data.decode())["isbn"]

    try:
        if book_dao.get_by_isbn(mongo, isbn) is None:
            raise BookNoExistsException
    except BookNoExistsException:
        print("Book doesnt exists")
        abort(500, "Book doesnt exists")
    
    book_dao.delete_by_isbn(mongo, isbn)


def update_book(data, mongo):
    """Method to update an existing book"""
    book_json = json.loads(data.decode())

    isbn = book_json["isbn"]
    title = book_json["title"]
    author = book_json["author"]
    publisher = book_json["publisher"]

    book = book_dao.get_by_isbn(mongo, isbn)


    book["title"] = title
    book["author"] = author
    book["publisher"] = publisher

    book_dao.update(mongo, book)


def get_books(mongo):
    """Method to obtains the books list"""
    book_list = book_dao.get_all(mongo)

    for book in book_list:
        book['_id'] = str(book['_id'])
    return book_list


def get_book(data, mongo):
    """Method to obtain a book"""
    isbn = json.loads(data.decode())["isbn"]
    book = book_dao.get_by_isbn(mongo, isbn)
    try:
        if book is None:
            raise BookNoExistsException
    except BookNoExistsException:
        print("Book doesnt exists")
        abort(500, "Book doesnt exists")

    book['_id'] = str(book['_id'])
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

    for book in return_list:
        book['_id'] = str(book['_id'])

    return return_list



