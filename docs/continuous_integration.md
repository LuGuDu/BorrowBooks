# 🔄 Continuous integration 🔄

---

The goal this time is to be able to run the tests continuously every time a special event occurs, which in our case will be a push to the main branch. Every time that happens, what we will do is run the tests that we have hosted in the Docker container that we saved in DockerHub in the previous point.

So a new github action has been developed with a workflow that will be in charge of doing a pull from that docker container and executing it to check that all the tests pass.

You can view the file created from the following link: [Testing CI](https://github.com/LuGuDu/BorrowBooks/blob/main/.github/workflows/deploy.yml)

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/testingCI.JPG" alt="Success Testing CI Action" style="width:800px;"/>

A change had to be made in the tests, because until now integration tests of the developed REST API had been carried out instead of unit tests for the controller methods. The changes have not been very big, but they have meant hours of work.

