import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost')
)

channel1 = connection.channel()

channel1.queue_declare(queue = "hello")

while(1):
    x = input()
    channel1.basic_publish(exchange="", routing_key="hello",body = x)

channel1.close()