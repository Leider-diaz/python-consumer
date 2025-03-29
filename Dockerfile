FROM python:3.10-slim


WORKDIR /app


RUN pip install pika logging

COPY consumer.py /app/


CMD ["python", "-u", "consumer.py"]