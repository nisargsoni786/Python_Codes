import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost')
)

channel1 = connection.channel()

channel1.queue_declare(queue = "hello")
channel1.queue_declare(queue = "hello2")

while(1):
    x = input()
    channel1.basic_publish(exchange="", routing_key="hello",body = x)
    channel1.basic_publish(exchange="", routing_key="hello2",body = x+" 222")

channel1.close()