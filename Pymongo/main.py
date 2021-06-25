from flask import Flask,jsonify,request
from pymongo import MongoClient

app = Flask(__name__)

URI='mongodb+srv://admin:1234567890@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI)

db=client.jsn

Book=db.book

@app.route('/',methods=['GET'])
def gett():
    # res=Book.find({"name":"Nisarg"})
    # for book in res:                                        # if want to find many
    #     print(book)

    res=Book.find_one({"name":"Nisarg"})                      # if want to find one
    print(res)
    return "check cmd"
    
@app.route('/',methods=['POST'])
def postt():
    data=request.get_json()
    idd=Book.insert_one(data).inserted_id

    return "Check added or not !............"+str(idd)

@app.route('/',methods=['PUT'])
def putt():
    res=Book.update({'author':'donno'},{'$set':{'author':"Shah"}})
    return "check author donno converted to shah or not !"

@app.route('/',methods=['DELETE'])
def deletee():
    res=Book.delete_one({'name':"songs"})      # delete_many can also use for many
    print(res)
    return "check deleted or not"

@app.route('/all',methods=['GET'])
def gettt():
    res=Book.find()
    ans=[]
    for i in res:
        d={}
        d['name']=i['name']
        d['author']=i['author']
        ans.append(d)
    print(ans)
    return jsonify({"data":ans})

if __name__ == '__main__':
    app.run(debug=True)