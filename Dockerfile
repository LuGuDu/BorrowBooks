FROM python

RUN pip install flask && pip install pytest

COPY .. /app

WORKDIR /borrowbookspp/testing

CMD ["make"]