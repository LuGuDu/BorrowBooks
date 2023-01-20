# Service composition

---

## Mongo DB

First, what was done was to migrate the MongoDB Atlas database to a mongo Docker container. However, as the database is actually empty, it was not necessary to extract data and put it into the new database. 

What was done was to download a mongo image and change the db call in the server code. Now, instead of calling a remote one, it calls localhost:27017, which is where mongo listens locally by default. A container was executed binding the ports and that's it.

`$docker pull mongo`

`$docker run --name mongoCC -p 27017:27017 -d mongo`

## Flask App

The next step was to put the API inside a docker image. To do this, the [Dockerfile](https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/Dockerfile) in the root folder was modified. Now it doesn't build an image thinking in the execution of the tests, but in the execution of the API. When creating the container by binding the ports, there were two problems: 
1. when calling localhost:5000, no response was received, 
2. the server did not connect to the db. 

The first problem was solved by explicitly telling the server to listen on 0.0.0.0 using the following line of code in the server run:

```
if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

The second problem is not new, it happened a few tasks ago with the tests. If from inside a container you want to tell it to call the localhost of the machine and not of the container, you should specify 'host.docker.internal' instead of 'localhost'. So the calls to the db are made by calling 'host.docker.internal:27017'.

After these changes, you can have both the db and the API in different containers, and everything is functional.

## SonarQube

A sonarqube image has also been downloaded in order to deploy a server to measure the quality of the code. For this purpose, the following lines are executed:

`$docker pull sonarqube`

`$docker run --name sonarCC -p 9000:9000 -d sonarqube`

Now we can launch a command with sonar-scanner in our project folder so that this container performs a quality scan and returns the results from the interface at localhost:9000. It is important to say that if you run it for the first time in a machine you have to configure some things of this server, because you have to enter for the first time with the admin/admin credentials, change them and assign a token to the user to be able to perform the scanner. 

The command to perform the scanner will have the following form:

`$sonar-scanner -Dsonar.host.url=http://localhost:9000 -Dsonar.login=USER_TOKEN -Dsonar.projectKey=PROJECT_NAME`

## docker-compose.yml

Once this is done, in order to orchestrate all these containers, a docker-compose.yml file has been created in which the desired configurations of each container are specified and all of them are launched together. The file has the following content:

```
version: '3'
services:
  flask_app:
    image: server
    ports:
      - "5000:5000"
    volumes:
      - "./logs:/app/borrowbooksapp/logs"
    environment:
      - MONGO_URI=mongodb://localhost:27017/borrowbooksdb
    depends_on:
      - mongo

  sonarqube:
    image: sonarqube
    ports:
      - "9000:9000"

  mongo:
    image: mongo
    ports:
      - "27017:27017"
```

Doing `$docker-compose up` will deploy all the containers on your machine and everything will be fully operational. However, you will need to have all the images downloaded. For this, a [Makefile](https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/Makefile) has been created which will download all the images (mongo and sonar) and mount the API image from the Dockerfile mentioned above.

## Logs

As a detail, because the logs are recorded inside the API container, a line has been added to the docker-compose so that everything that is done in the application logs folder is saved in another folder logs that will be created in the same path as the docker-compose. In this way, all the logs made on the server can be viewed from the host machine. This has been done by adding a volumes tag.

## Testing the service composition

If we execute the make command, the final result is going to be the deployment of the containers:

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone2/docs/resources/containers.JPG" alt="docker-compose execution result"/>