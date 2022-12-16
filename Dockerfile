FROM python

RUN pip install flask && pip install pytest

COPY .. /app

WORKDIR /app/borrowbookspp/testing

CMD ["make"]