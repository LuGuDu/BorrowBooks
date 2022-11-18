# ✔️ Assert's library ✔️

---

Asserts confirm the correctness of a line of code. As this project is developed using the Python programming language, it comes with a library of asserts by default.

So, assert is a keyword to confirm the correctness of a given statement that is often used to facilitate development, documenting code and debugging.
The syntax is very simple:
  ```
    assert some_condition, assert_message
  ```
The word 'assert' is followed by some_condition which will be tested. An optional assert_message can be added which will be printed once the assert error occurs.

An example from the project is shown below:

```
def test_failed_delete_book():
    data = {
                "isbn": "8596", 
            }

    response = requests.delete(
            "http://127.0.0.1:5000/delete_book",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        
    res = json.loads(response.text)

    assert response.status_code == 500
    assert res["message"] == "Book doesnt exists"
```

In this example a DELETE request will be sent to the REST API to delete a book with an isbn of 8596. However, there is no book in the database with that value, so an error 500 and a message will be returned. 

The assert keyword will be used to verify that an error code 500 is indeed returned and the specific message saying that the error does not exist.
