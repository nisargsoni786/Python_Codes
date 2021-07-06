from elasticsearch import Elasticsearch 
#import json


# Method to store data in elasticsearch
def send_data_to_es(data):
 es=Elasticsearch(['localhost:9200'])
 res = es.index(index='employee',doc_type='devops',body=data)
 print('\n\n\n',res,'\n\n\n')

# Method to get data from elasticsearch
def get_data_from_es():
 es=Elasticsearch(['localhost:9200'])
 r = es.search(index="employee", body={"query": {"match": {'Name':'john'}}})
 print('gettttttt from the db \n\n\n',r,'\n\n\n')
#  print(type(r))
 print(r["hits"]["hits"][0]["_source"])

# Main function from where the execution starts
if __name__== "__main__":
 # Define a dictoinary having required data to be stored in ES
 data = {"Name": "john", "Age":27, "address": "winterfell"}
#  send_data_to_es(data)
 get_data_from_es()