# 🗄️ Task manager 🗄️

---

We have opted to use the Make task manager. Make is a dependency management tool, so that it can direct the compilation or interpretation of code automatically. It will do this by executing the necessary commands to be specified in a file called Makefile.

Make is widely used on Unix/Linux operating systems. However, in Windows, which is the system used for the development of this application, it does not come by default. Therefore, to use it, the tool had to be installed following the tutorial below:
 - [How to run make on Windows](https://linuxhint.com/run-makefile-windows/)

The MinGW tool, a package manager that allows the installation of Make on windows, was installed. This enabled the command from the cmd. After that, a simple Makefile was written to automatically deploy the tests.

```
run:
	pytest tests/
```

This solves the problem of automatic test execution by means of a task manager.
