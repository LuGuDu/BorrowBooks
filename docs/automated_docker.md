# 🐳 Automated Docker 🐳

---

Next, the aim is to automate the building of the docker image that we have already created so that, every time a push is made to the main branch, it can be built.

This has been done by means of the github actions tool, which provides us with a series of pipes to be able to launch scripts when an action is performed.

But first, we had to create an account in DockerHub with its corresponding repository to be able to save the image that we are going to build. So, in order for Github Actions to be able to collaborate with this dockerhub account, it is necessary to create two corresponding secrets with the user's name and password in Dockerhub.

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/secrets.JPG" alt="Repository secrets with DockerHub credentials" style="width:700px;"/>

Once this step has been done, the following script has been created and saved in a file specifically located for Github Actions. 
You can see the file from the following link: [docker-update.yml](https://github.com/LuGuDu/BorrowBooks/blob/main/.github/workflows/docker-update.yml)


So if we perform the action and put any change that contains a modification in the Dockerfile file to the main branch, this script will be executed and we will be able to see how the dockerhub repository is updated.

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/successAction.JPG" alt="Success Build Action" style="width:600px;"/>

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone1/docs/resources/dockerhub.JPG" alt="DockerHub updated" style="width:600px;"/>
