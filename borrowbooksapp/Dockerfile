FROM python

COPY /testingDocker /test

RUN pip install pytest && pip install requests

WORKDIR /test

CMD ["make"]