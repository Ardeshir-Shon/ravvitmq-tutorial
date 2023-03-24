import pika
import time

# Configure connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)

# Create a channel
channel = connection.channel()

# Declare a queue
queue_name = 'time_queue'
channel.queue_declare(queue=queue_name)

# Publish the current time
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
channel.basic_publish(exchange='', routing_key=queue_name, body=current_time)
print(f" [x] Sent '{current_time}'")

# Close the connection
connection.close()
