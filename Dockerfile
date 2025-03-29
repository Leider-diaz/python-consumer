FROM python:3.10-slim


WORKDIR /app


RUN pip install pika

COPY consumer.py /app/


CMD ["python", "consumer.py"]