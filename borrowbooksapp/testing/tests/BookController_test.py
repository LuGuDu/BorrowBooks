# INTEGRATION TESTS
#
#     import pytest
#     import requests
#     import json
# 
#     from flask import Flask
#     from flask_pymongo import PyMongo


#     @pytest.mark.run(order=1)
#     def test_success_create_book():
#         data = {
#                     "isbn": "0828", 
#                     "title": "El Quijote", 
#                     "author": "Miguel de Cervantes",
#                     "publisher": "DeBolsillo"
#                 }

#         response = requests.post(
#                 "http://127.0.0.1:5000/create_book",
#                 data=json.dumps(data),
#                 headers={"Content-Type": "application/json"},
#             )
        
#         assert response.status_code == 200


#     @pytest.mark.run(order=2)
#     def test_success_update_book():
#         data = {
#                     "isbn": "0828", 
#                     "title": "La celestina", 
#                     "author": "Fernando de rojas",
#                     "publisher": "DeBolsillo"
#                 }

#         response = requests.put(
#                 "http://127.0.0.1:5000/update_book",
#                 data=json.dumps(data),
#                 headers={"Content-Type": "application/json"},
#             )
        
#         assert response.status_code == 200


#     @pytest.mark.run(order=2)
#     def test_success_get_books():
#         response = requests.get("http://127.0.0.1:5000/get_books")
#         assert response.status_code == 200


#     @pytest.mark.run(order=2)
#     def test_success_get_book():
#         data = {
#                     "isbn": "0828",
#                 }
#         response = requests.get("http://127.0.0.1:5000/get_book",
#         data = json.dumps(data),
#         headers={"Content-Type": "application/json"})

#         assert response.status_code == 200


#     def test_failed_get_book():
#         data = {
#                     "isbn": "9898"
#                 }
#         response = requests.get("http://127.0.0.1:5000/get_book",
#         data = json.dumps(data),
#         headers={"Content-Type": "application/json"})

#         res = json.loads(response.text)

#         assert response.status_code == 500
#         assert res["message"] == "Book doesnt exists"


#     @pytest.mark.run(order=3)
#     def test_success_delete_book():
#         data = {
#                     "isbn": "0828", 
#                 }

#         response = requests.delete(
#                 "http://127.0.0.1:5000/delete_book",
#                 data=json.dumps(data),
#                 headers={"Content-Type": "application/json"},
#             )
#         assert response.status_code == 200


#     def test_failed_delete_book():
#         data = {
#                     "isbn": "8596", 
#                 }

#         response = requests.delete(
#                 "http://127.0.0.1:5000/delete_book",
#                 data=json.dumps(data),
#                 headers={"Content-Type": "application/json"},
#             )
            
#         res = json.loads(response.text)

#         assert response.status_code == 500
#         assert res["message"] == "Book doesnt exists"
# ###

import pytest
import json

from flask import Flask
import unittest
from app import app

class TestMyAPI(unittest.TestCase):

    @pytest.mark.run(order=1)
    def setUp(self):
            self.app = Flask(__name__)
            self.client = app.test_client()

    @pytest.mark.run(order=1)
    def test_success_create_book(self):
        data = {
                    "isbn": "0828", 
                    "title": "El Quijote", 
                    "author": "Miguel de Cervantes",
                    "publisher": "DeBolsillo"
                }
        response = self.client.post(
                "/create_book",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 200


    @pytest.mark.order1
    def test_success_update_book(self):
        data = {
                    "isbn": "0828", 
                    "title": "La celestina", 
                    "author": "Fernando de rojas",
                    "publisher": "DeBolsillo"
                }

        response = self.client.put(
                "/update_book",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
        
        assert response.status_code == 200

        data = {
                    "isbn": "0828", 
                }

        response = self.client.delete(
                "/delete_book",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 200


    @pytest.mark.run(order=3)
    def test_success_get_books(self):
        response = self.client.get("/get_books")
        assert response.status_code == 200


    @pytest.mark.run(order=4)
    def test_success_get_book(self):
        data = {
                    "isbn": "0828",
                }
        response = self.client.get("/get_book",
        data = json.dumps(data),
        headers={"Content-Type": "application/json"})

        assert response.status_code == 200


    def test_failed_get_book(self):
        data = {
                    "isbn": "9898"
                }
        response = self.client.get("/get_book",
        data = json.dumps(data),
        headers={"Content-Type": "application/json"})

        res = json.loads(response.data)

        assert response.status_code == 500
        assert res["message"] == "Book doesnt exists"


    def test_failed_delete_book(self):
        data = {
                    "isbn": "8596", 
                }

        response = self.client.delete(
                "/delete_book",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
            
        res = json.loads(response.data)

        assert response.status_code == 500
        assert res["message"] == "Book doesnt exists"


if __name__ == '__main__':
    unittest.main()