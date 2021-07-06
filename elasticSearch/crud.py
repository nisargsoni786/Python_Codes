from elasticsearch import Elasticsearch 

es=Elasticsearch(['localhost:9200'])

# To create Index
def create_index():
    res=es.indices.create(index="first_index")
    print(res)

# To check if index exists or not
def if_exists():
    res=es.indices.exists(index='first_index')
    print(res)

# To delete index
def to_delete():
    res=es.indices.delete(index="first_index")
    print(res)

# To insert Data
def insert():
    doc1={"city":"abad","country":"India"}
    doc2={"city":"LA","country":"USA"}
    doc3={"city":"tel aviv","country":"israel"}
    es.index(index="cities",doc_type="Places",id=1, body=doc1)
    es.index(index="cities",doc_type="Places",id=2, body=doc2)
    es.index(index="cities",doc_type="Places",id=3, body=doc3)

# Get data by id
def get_by_id():
    res=es.get(index="cities",doc_type="Places",id=1)
    print(f"\n{res}\n")
    print(f"\n{res['_source']}\n")

def get_by_query():
    query={
        "size":2,
        "query":{
            "match":{"city":"abad"}
        }
    }
    res=es.search(index="cities",doc_type="Places",body=query)
    print('\n',res)


# create_index()
# if_exists()
# to_delete()
# insert()
# get_by_id()
get_by_query()
