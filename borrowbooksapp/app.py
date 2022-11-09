from flask import Flask, request
from flask_pymongo import PyMongo
import json
import controllers.BookController as book_controller


app = Flask(__name__)

MONGO_STRING = "mongodb+srv://borrowbooks:tOKlwpoiQan7Nt60@cluster0.gozlc.mongodb.net/borrowbooksdb"
app.config["MONGO_URI"] = MONGO_STRING
mongodb_client = PyMongo(app)
mongo = mongodb_client.db


@app.route('/get_books', methods=['GET'])
def get_books():
    """Method to obtain a list of all books"""
    if request.method == "GET":
        books_list = book_controller.get_books(mongo)
        return {"message": 200, "books": books_list}
    return {"message": 500}


@app.route('/get_book', methods=['GET'])
def get_book():
    """Method to obtain a book"""
    if request.method == "GET":
        book = book_controller.get_book(request.data, mongo)
        return {"message": 200, "book": book}
    return {"message": 500}


@app.route('/create_book', methods=['POST'])
def create_book():
    """Method to create a new book"""
    if request.method == "POST":
        book_controller.create_book(request.data, mongo)
        return {"message": 200}

    return {"message": 500}


@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    """Method to delete a book"""
    if request.method == 'DELETE':
        book_controller.delete_book(request.data, mongo)
        return {"message": 200}
    return {"message": 500}


@app.route('/update_book', methods=['PUT'])
def update_book():
    """Method to update a book"""
    if request.method == 'PUT':
        book_controller.update_book(request.data, mongo)
        return {"message": 200}
    return {"message": 500}


@app.route('/search', methods=['GET'])
def search_books():
    """Method to search books by parameters"""
    if request.method == 'GET':
        books_list = book_controller.search_by(request.data, mongo)
        return {"message": 200, "book_list": books_list}
    return {"message": 500}


if __name__ == '__main__':
    app.run()
