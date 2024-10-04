FROM python:alpine

WORKDIR /app

COPY client.py /app/client.py

RUN pip install requests

CMD [ "python", "client.py" ]