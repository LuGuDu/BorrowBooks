# 🚀 Milestone 0 - Repository creation 🚀

---


First of all, it will be necessary to create a new repository from the github interface or from the git bash. For this repository to have the usual documents, it will be necessary to add a *readme.md* file, in which the most relevant documentation of the whole project will be shown, and another *license* file. This repository will have the MIT license. 

Once we have the repository created we can clone it to our computer using the command `git clone 'repositoryName'` in bash. This way we will be able to work locally in the repository.

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone0/docs/resources/milestone0c1.JPG" alt="Git clone without resources" style="width:400px;"/>

However, there is a problem, as we are notified that we do not have the necessary permissions to clone the repository. This is a security measure, and it is necessary to authenticate via ssh, since this way we can work in a much more secure way and, in this way, to be able to control those devices that are actively collaborating in our repository.

In order to obtain an ssh key we can generate it using the following command:

`ssh-keygen -t ed25519 -C "email@email.com"`

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone0/docs/resources/milestone0c2.JPG" alt="ssh keygen" style="width:400px;"/>

This command will generate a key that we will have to introduce in our github profile, and in this way we will be able to use that computer to work. From the moment that our account has linked that ssh key we can clone the repository successfully.

<img src="https://github.com/LuGuDu/BorrowBooks/blob/LuGuDu-milestone0/docs/resources/milestone0c3.JPG" alt="ssh generated" style="width:500px;"/>

From our local repository we could make any modification, either create, delete or edit directories or files. However, these changes would be in local. In order to update the repository remotely, we will have to create a commit with the command `git commit -m "commitName"`, add the changes to the commit with the command `git add .` and finally upload the changes with the command `git push -u origin 'branchName'`.


