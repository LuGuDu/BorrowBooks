FROM python

RUN pip install pytest && pip install requests

COPY /testingDocker /tests

WORKDIR /tests

CMD ["make"]