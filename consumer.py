import pika

def callback(ch, method, properties, body):
    print(f"Received '{body.decode()}'")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672)
)
channel = connection.channel()

channel.queue_declare(queue='example_queue')

channel.basic_consume(queue='example_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. Press CTRL+C to exit.')
channel.start_consuming()
