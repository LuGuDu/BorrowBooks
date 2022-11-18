# 🧪 Test framework 🧪

---

In order to run all the tests developed at the same time, a framework is used. The framework chosen in this project was [pytest](https://docs.pytest.org/en/7.2.x/). 

The pytest framework facilitates the writing of small, readable tests, and can scale to support complex functional tests for applications and libraries.

Un ejemplo de test desarrollado en este proyecto es el siguiente:

```
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
            "http://127.0.0.1:5000/create_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
    
    assert response.status_code == 200
```

This test is responsible for creating a book. The data is specified and sent in json format to the REST API with an http POST request. This test will pass successfully if the assert is confirmed. The condition will be that the response of the request will be a code 200, indicating that everything went well.

You can see the rest of the tests created in the file [BookController_test.py](https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/borrowbooksapp/testing/tests/BookController_test.py)

---

To run pytest you only need to execute the command followed by the file or directory where your tests are located:
 `$pytest test/`

Result after running the developed tests:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/testing.JPG" alt="Pytest execution result" style="width:600px;"/>

