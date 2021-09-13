from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

URI='mongodb+srv://admin:1234567890@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority'
client = AsyncIOMotorClient(URI)

db=client.jsn

async def add():
    doc={"name":"songs","author":"KK"}
    res=await db.book.insert_one(doc)
    print('result %s' % repr(res.inserted_id))
    return res.inserted_id

async def findone():
    res=db.book.find_one({"author":"KK"})
    print(res)
    print(type(res))
    return res.get('name')

async def findall():
    res=db.book.find({"author":"KK"})
    async for doc in res:
        print(doc,'..........................',doc.get('name'))
    return res

async def update():
    doc=await db.book.find_one({"author":"Soni"})
    print(doc)
    new=await db.book.update_one({"author":"Soni"},{'$set':{"name":"Nisarg"}})
    print(new)

async def delete():
    # res=await db.book.delete_many({"name":"songs"})
    res=await db.book.delete_one({"name":"songs"})
    print(res)


loop = asyncio.get_event_loop()
# loop.run_until_complete(add())
# loop.run_until_complete(findone())
# loop.run_until_complete(findall())
# loop.run_until_complete(update())
loop.run_until_complete(delete())