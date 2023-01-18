# :see_no_evil: API Logger :see_no_evil:

---

A log has also been included in the server in order to record everything that happens during the execution of the server. This way we have a detailed control of all the calls made against the backend.

In order to implement this log we have used the Python module called "loggin". Once imported, the following configuration has been set to format the output message in the log:

```
logging.basicConfig(filename='api.log', level=logging.DEBUG, 
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
```

This way, when starting the server, a file called 'api.log' is created in which all the movements will be registered. After making some calls to the API, the log shows the following:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/docs/resources/logger.JPG" alt="Pytest execution result" style="width:600px;"/>

