# 🧪 API testing 🧪

---

In order to develop the tests that have been able to test the different resources developed in the API, the well-known pytest framework has been used, which is generally used for Python projects. This framework allows the writing of small tests, very readable and scalable depending on the complexity of the test to be developed.

We have also used libraries such as requests, which have allowed us to make API calls via HTTP. In this way we can connect to the server and, using assert, we can check if the response is what we would expect or not.

An example of one of the tests developed is the following:

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


Tests have been written to test the functionality of MILESTONE 1, so that the controller in charge of the books is tested. You can see this file: [BookController_test.py](https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/borrowbooksapp/testingAPI/tests/BookController_test.py).

To run them and see that they work satisfactorily, we run the command:  `$pytest testingAPI/test/` in the folder where our tests are located or using the Make file. We get the following result after the execution:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/docs/resources/testing2.JPG" alt="Pytest execution result" style="width:600px;"/>

