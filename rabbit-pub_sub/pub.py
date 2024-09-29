import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='flavors', exchange_type='topic')

new_flavors = ['Nutella', 'Coconut', 'Berry Mix', 'Peanut Butter', 'Mint']

for flavor in new_flavors:
    channel.basic_publish(exchange='flavors', routing_key='new', body=flavor)
    print(f"Announced new flavor: {flavor} at {time.strftime('%H:%M:%S')}")

connection.close()