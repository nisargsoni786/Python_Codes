from kafka import KafkaProducer
import json,time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# --------------- IF WE WANT MESSAGE ALWAYS SENT TO P0----------------.
def get_partition(key,all,available):
    return 1


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
             value_serializer=json_serializer,
             partitioner=get_partition
             )

if __name__ == '__main__':
    i =1
    while True:
        data = {
            "name" : "Hkqhq------>"+str(i),
            "address" : "parth----->"+str(i),
            "created_at" : "2021------>"+str(i)
        }

        time.sleep(3)
        producer.send("topic_2_partition", data)


        print(f"DATA NUMBER {i} SENT SUCCESSFULLY !!!")
        # i+=1