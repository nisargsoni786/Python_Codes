from elasticsearch import Elasticsearch 

es=Elasticsearch(['localhost:9200'])

def create_index():
    res=es.indices.create(index="sents")
    print(res)

def insert():
    doc1={"emo":"love","sent":"love you to the moon and back"}
    doc2={"emo":"anger","sent":"i will beat you bloody badass"}
    doc3={"emo":"surprised","sent":"i cant imagine this from you"}
    doc4={"emo":"surprised","sent":"i cant imagine i am going to moon"}

    es.index(index="sents",id=1, body=doc1)
    es.index(index="sents",id=2, body=doc2)
    es.index(index="sents",id=3, body=doc3)
    es.index(index="sents",id=4, body=doc4)

def query1():
    query={
        "size":2,
        "query":{
            "match":{"emo":"love"}
        }
    }
    res=es.search(index="sents",body=query)
    print('\n',res)

def check_field():
    query={
        "query":{
            "exists":{
                "field":"emo"              ## checks if the field is in the document or not...
            }                               ## if yes than it include that doc in the result !
        }
    }
    print(es.search(index="sents",body=query))

# query={
#   "query": {
#     "ids" : {
#       "values" : ["1", "4", "100"]         #You cn also do this to find values with this ids !!!
#     }
#   }
# }

# {
#   "query": {
#     "prefix": {
#       "user.id": {
#         "value": "ki"                      # to check the prefix of the field
#       }
#     }
#   }
# }

def get_all():
    query={
        "query":
            {"bool":
                {"must":{
                    "match_all":{}
                }
            }
        }
    }
    res=es.search(index="sents",body=query)
    print('\n',res)

def query2():
    query={
        "size":2,
        "query":{
            "bool": 
            {"must":[
                {"match":{"sent":"moon"}},
                {"match":{"emo":"love"}}                
                ]}
        }
    }
    res=es.search(index="sents",body=query)
    print('\n',res)

def check_fuzzy():
    query={
        "query":{
            "fuzzy":{
                "sent":{
                    "value":"moo"
                }
            }
        }
    }
    print(es.search(index="sents",body=query))


# create_index()
# insert()
# get_all()
# check_field()
check_fuzzy()
# query2()


