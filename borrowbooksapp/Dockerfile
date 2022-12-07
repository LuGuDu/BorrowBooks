FROM python

RUN pip install requests && pip install pytest

COPY /testingDocker /tests

WORKDIR /tests

CMD ["make"]