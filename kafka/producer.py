from kafka import KafkaProducer
import json,time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)

if __name__ == '__main__':
    i =1
    while True:
        data = {
            "name" : "Hkqhq------>"+str(i),
            "address" : "parth----->"+str(i),
            "created_at" : "2021------>"+str(i)
        }

        time.sleep(3)
        producer.send("topic1", data)


        print(f"DATA NUMBER {i} SENT SUCCESSFULLY !!!")
        i+=1