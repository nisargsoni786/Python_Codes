from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse as jsonify
from app.controller.trial import router as trial_router
from app.database.connect import sess
from app.models.models import Stu

app=FastAPI()

app.include_router(trial_router)

@app.get('/')
async def index():
    return jsonify({"Message":"Hello There"})

@app.post('/')
async def pp(request:Request=None,response:Response=None):
    data=await request.json()
    print(data)
    print(type(data))
    response.status_code=210
    return ({"Message":data,"OK":"True"})

@app.get('/stu')
async def gett():
    stus=sess.query(Stu).all()
    data=[i.name for i in stus]
    return {"data":data}

@app.post('/stu')
async def postt(request:Request=None):
    data=await request.json()
    print(data)
    stu=Stu(name=data.get('name'))
    sess.add(stu)
    sess.commit()
    return {"MESSAGE":"DATA ADDED!"}

@app.delete('/stu/{id}')
async def dele(id):
    stu=sess.query(Stu).filter_by(id=id).first()
    if stu==None:
        return {"Messsage":"user doesn't exist!"}
    sess.delete(stu)
    sess.commit()
    return {"Message":"Data deleted successfully"}


@app.get('/{id:int}',status_code=204)
async def pp(id,request:Request=None,response:Response=None):
    return {"ID":id}
