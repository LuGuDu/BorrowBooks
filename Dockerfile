FROM python

RUN pip install flask && pip install pytest

COPY .. /borrowbooksapp

WORKDIR /testing/tests

CMD ["make"]