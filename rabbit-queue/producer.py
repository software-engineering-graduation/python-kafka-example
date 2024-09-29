import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sorvete_queue')

orders = ['Chocolate', 'Vanilla', 'Strawberry', 'Pistachio']

for order in orders:
    channel.basic_publish(exchange='',
                          routing_key='sorvete_queue',
                          body=order)
    print(f"Sent order: {order} : {time.strftime('%H:%M:%S')}")

connection.close()