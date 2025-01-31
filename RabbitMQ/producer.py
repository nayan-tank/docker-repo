import pika

def produce_messages():
    # Connection parameters with authentication
    credentials = pika.PlainCredentials('guest', 'guest')  # Replace with your credentials
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))  # Adjust host and port if needed
    channel = connection.channel()


    # Declare a queue
    channel.queue_declare(queue='demo_queue')
    # channel.queue_declare(queue='demo_queue', durable=True)

    # Produce messages
    messages = ["Hello World!", "RabbitMQ with authentication!", "Message 3", "Message 4", "Message 5"]
    for message in messages:
        channel.basic_publish(exchange='', routing_key='demo_queue', body=message)
        print(f"Sent: {message}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    produce_messages()
