FROM python

COPY /testingDocker /tests

RUN pip install pytest && pip install requests

WORKDIR /tests

CMD ["make"]