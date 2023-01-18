# Choosing a Framework 

---

From the beginning, the development of the code has been oriented towards the creation of a REST API. Thus, the implementation of a microservice is already in place. The API has been developed in Python using the Flask framework. This framework is very simple and intuitive to use, especially for applications whose functionality does not require much complexity. 

An example of a resource created is the following:

```
@app.route('/get_books', methods=['GET'])
def get_books():
    """Method to obtain a list of all books"""
    if request.method == "GET":
        books_list = book_controller.get_books(mongo)
        return {"message": 200, "books": books_list}
    return {"message": 500}
```

In a few simple lines you can create an endpoint where you can indicate the path and the http verb with which to access it. Within the method that we establish, a request object will be recognised on which we can check different things, such as the call method (GET, POST, DELETE, ...) or the content of the body, the data, etc. In the case of this application, the body of the request sends the data in JSON format.

For the server to work, it is necessary to include a main method that commands the application to run, so that when the file is executed, the server can be deployed, in this case on localhost:5000.

```
if __name__ == '__main__':
    app.run()
```
