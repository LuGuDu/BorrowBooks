FROM python

RUN pip install requests && pip install pytest

COPY borrowbooksapp/testing /tests

WORKDIR /tests

CMD ["make"]