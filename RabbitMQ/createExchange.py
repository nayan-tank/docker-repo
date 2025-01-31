import pika

def create_exchange():
    # Connection parameters
    credentials = pika.PlainCredentials('guest', 'guest')  # Replace with your RabbitMQ credentials
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    # Declare an exchange
    exchange_name = "demo_exchange"
    exchange_type = "fanout"  # Can be 'direct', 'topic', 'fanout', or 'headers'

    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)

    print(f"Exchange '{exchange_name}' of type '{exchange_type}' created successfully!")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    create_exchange()
