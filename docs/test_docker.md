# 🐳 Testing with Docker 🐳

---

First of all, the default Python container has been chosen which can be found on DockerHub [(see here)](https://hub.docker.com/_/python). 

Next, the following Dockerfile has been written, which will be built in order to create an image to be able to run the tests.

```
FROM python

COPY /testingDocker /test

RUN pip install pytest && pip install requests

WORKDIR /test

CMD ["make"]
```

In order for the tests to work and be able to find the machine's localhost address and port 5000 (which is where the flask server listens) the tests have been modified, so that the address to which the different HTTP requests are sent is the following:

`host.docker.internal:5000`

So, to build the image we will use the following command:

```
docker build --tag python .
```

The following image shows the result of the build:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/DockerTestBuild.png" alt="Docker Test Image Build" style="width:700px;"/>


To run the image we will use the following command:

```
docker run -it python
```

The following image shows the result of the tests:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/DockerTestRun.png" alt="Docker Test Image Run" style="width:600px;"/>



