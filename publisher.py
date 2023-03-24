import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672)
)
channel = connection.channel()

channel.queue_declare(queue='example_queue')

for i in range(10):
    message = f"Hello world! {i}"
    channel.basic_publish(exchange='', routing_key='example_queue', body=message)
    print(f"Sent '{message}'")

connection.close()
