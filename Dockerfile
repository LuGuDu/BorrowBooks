FROM python

RUN pip install flask && pip install pytest

COPY .. /borrowbooksapp

WORKDIR /testing

CMD ["make"]