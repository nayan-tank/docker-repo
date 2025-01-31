import pika

def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")

def consume_messages():
    # Connect to RabbitMQ
    credentials = pika.PlainCredentials('guest', 'guest')  # Replace with your credentials
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))  # Adjust host and port if needed
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/'))  # Adjust host and port if needed
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='demo_queue')

    # Set up the consumer
    channel.basic_consume(queue='demo_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit, press CTRL+C')

    # Start consuming
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
