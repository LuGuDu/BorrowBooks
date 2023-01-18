import pytest
import requests
import json

@pytest.mark.run(order=1)
def test_success_create_book():
    data = {
                "isbn": "0828", 
                "title": "El Quijote", 
                "author": "Miguel de Cervantes",
                "publisher": "DeBolsillo"
            }

    response = requests.post(
            "http://localhost:5000/create_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
    
    assert response.status_code == 200


@pytest.mark.run(order=2)
def test_success_update_book():
    data = {
                "isbn": "0828", 
                "title": "La celestina", 
                "author": "Fernando de rojas",
                "publisher": "DeBolsillo"
            }

    response = requests.put(
            "http://localhost:5000/update_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
    
    assert response.status_code == 200


@pytest.mark.run(order=2)
def test_success_get_books():
    response = requests.get("http://localhost:5000/get_books")
    assert response.status_code == 200


@pytest.mark.run(order=2)
def test_success_get_book():
    data = {
                "isbn": "0828",
            }
    response = requests.get("http://localhost:5000/get_book",
    data = json.dumps(data),
    headers={"Content-Type": "application/json"})

    assert response.status_code == 200


def test_failed_get_book():
    data = {
                "isbn": "9898"
            }
    response = requests.get("http://localhost:5000/get_book",
    data = json.dumps(data),
    headers={"Content-Type": "application/json"})

    res = json.loads(response.text)

    assert response.status_code == 500
    assert res["message"] == "Book doesnt exists"


@pytest.mark.run(order=3)
def test_success_delete_book():
    data = {
                "isbn": "0828", 
            }

    response = requests.delete(
            "http://localhost:5000/delete_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
    assert response.status_code == 200


def test_failed_delete_book():
    data = {
                "isbn": "8596", 
            }

    response = requests.delete(
            "http://localhost:5000/delete_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        
    res = json.loads(response.text)

    assert response.status_code == 500
    assert res["message"] == "Book doesnt exists"
