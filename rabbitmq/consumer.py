import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost')
)

channel1 = connection.channel()

def callback(ch,method,properties,body):
    print("Body>>",body)

channel1.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True)

print("******WAITING****")
channel1.start_consuming()