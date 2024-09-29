from queue import Queue
import random
import threading
import time
import pika

ORDER_ARRIVED_COLOR = '\033[92m'
ORDER_PROCESSED_COLOR = '\033[94m'

order_queue = Queue()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sorvete_queue')

def callback(_ch, _method, _properties, body):
    print(f"{ORDER_ARRIVED_COLOR}Order received: {body.decode()} : {time.strftime('%H:%M:%S')}")
    order_queue.put(body.decode())
    
def process_order():
    while True:
        order = order_queue.get()
        if order is None:
            break 

        time.sleep(random.randint(1, 5))
        print(f"{ORDER_PROCESSED_COLOR}Order processed: {order} : {time.strftime('%H:%M:%S')}")

        order_queue.task_done()
        
# Start the worker thread for processing orders
worker_thread = threading.Thread(target=process_order, daemon=True)
worker_thread.start()

channel.basic_consume(queue='sorvete_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for orders...')
channel.start_consuming()