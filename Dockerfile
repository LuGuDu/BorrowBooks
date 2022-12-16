FROM python

RUN pip install flask && pip install flask_pymongo && pip install pytest

COPY .. /app

WORKDIR /app/borrowbooksapp/testing

CMD ["make"]