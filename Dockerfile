FROM python

RUN pip install requests && pip install pytest

COPY borrowbooksapp/testingDocker /tests

WORKDIR /tests

CMD ["make"]