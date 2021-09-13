from flask import Flask,jsonify,request
import motor,asyncio
from motor.motor_asyncio import AsyncIOMotorClient

app = Flask(__name__)

URI='mongodb+srv://admin:1234567890@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority'
client = AsyncIOMotorClient(URI)

db=client.jsn

@app.route('/')
async def index():
    return "Home"

@app.route('/add',methods=["GET"])
def post():
    asyncio.set_event_loop(asyncio.new_event_loop())
    task=asyncio.ensure_future(add())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(asyncio.gather())
    print(result)
    return "check added or not ..."+str(result)

async def add():
    doc={"name":"aaaaaaa","author":"bbbbbb"}
    res=await db.book.insert_one(doc)
    print('result %s' % repr(res.inserted_id))
    return res.inserted_id



if __name__ == '__main__':
    app.run(debug=True)