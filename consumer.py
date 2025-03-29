import pika
import logging

# Conexión a RabbitMQ usando la IP del servidor RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.6.101.93'))
channel = connection.channel()

# Declarar cola
#channel.queue_declare(queue='cola5')

def callback(ch, method, properties, body):
    logging.info("Mensaje recibido:", body.decode())

# Suscribirse a la cola
channel.basic_consume(queue='cola5',
                      on_message_callback=callback,
                      auto_ack=True)

logging.info('Esperando mensajes. Presiona CTRL+C para salir')
channel.start_consuming()