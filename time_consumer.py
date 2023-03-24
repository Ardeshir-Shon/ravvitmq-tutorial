import pika

def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# Configure connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)

# Create a channel
channel = connection.channel()

# Declare the same queue as in the publisher
queue_name = 'time_queue'
channel.queue_declare(queue=queue_name)

# Set up the consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
