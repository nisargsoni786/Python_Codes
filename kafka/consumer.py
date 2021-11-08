from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    "topic_2_partition",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset="earliest",
    group_id="consumer_group_1"
    )

print("--------------------STARTING CONSUMING-----------------")

for msg in consumer:
    print("msg-->  ",json.loads(msg.value))