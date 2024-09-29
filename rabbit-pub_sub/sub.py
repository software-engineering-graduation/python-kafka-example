import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='new_flavors', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='flavors', queue=queue_name, routing_key='new')

def callback(ch, method, properties, body):
    print(f"Received new flavor: {body.decode()} at {time.strftime('%H:%M:%S')}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

rand_sub_name = 'subscriber_' + str(time.time())
print(f'[{rand_sub_name}] Waiting for new flavors...')
channel.start_consuming()