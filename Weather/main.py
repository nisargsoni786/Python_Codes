from flask import Flask,request,jsonify
import requests,json,aiohttp,time,asyncio,async_timeout
import nest_asyncio

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def get_weather():
    try:
        data=request.get_json()
        name=data.get('city')
        if name == None:
            raise Exception("city name is necessary")
        res=requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60')
        data=json.loads(res.text)
        print(type(data))
        print(data)
        return jsonify({"OK":"true","data":data['weather']}),200

    except Exception as e:
        return jsonify({"OK":"false","error":str(e),"data":{}}),401

@app.route('/a')
async def gett():
    tasks=[]
    st=time.time()
    names=['pune','ahmedabad','nashik','mumbai','delhi','banglore','hayderabad','chennai','asaam','manipur','surat','rajkot','kutch','bhuj','varansi']
    async with aiohttp.ClientSession(trust_env=True) as session,async_timeout.timeout(20):
        for name in names:
            url=f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60'
            async with session.get(url) as resp:
                # res=await resp.json()
                # print(name,name,name,name,'\n')
                # print('\n',res,'\n')
                    tasks.append(asyncio.ensure_future(resp.json()))
            pokes=await asyncio.gather(*tasks)
            print(pokes)
    return {'time':time.time()-st}

@app.route('/b')
async def gettb():
    st=time.time()
    
    names=['pune','ahmedabad','nashik','mumbai','delhi','banglore','haidrabad','chennai','aasam','manipur','surat','rajkot','kutch','bhuj','mujffarabad','varansi']
    for name in names:
        url=f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60'
        res=requests.get(url)
        print(name,name,name,name,'\n')
        print('\n',res,'\n')
    return {'time':time.time()-st}

async def fetch(session,url):
    async with session.get(url) as resp:
        return await resp.json()

@app.route('/c')
async def gettc():
    tasks=[]
    st=time.time()
    names=['pune','ahmedabad','nashik','mumbai','delhi','banglore','hayderabad','chennai','asaam','manipur','surat','rajkot','kutch','bhuj','varansi','ahmedabad']
    async with aiohttp.ClientSession() as session:
        for name in names:
            url=f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60'

            tasks.append(asyncio.ensure_future(fetch(session,url)))

        responses=await asyncio.gather(*tasks) 
        for i in responses:
            print(i,'\n\n\n')
    return {'time':time.time()-st}

@app.route('/async')
async def asy():
    tasks=[]
    d={}
    st=time.time()
    names=['pune','ahmedabad','nashik','mumbai','delhi','banglore','hayderabad','chennai','asaam','manipur','surat','rajkot','kutch','bhuj','varansi','ahmedabad']
    async with aiohttp.ClientSession() as session:
        for name in names:
            url=f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60'
            tasks.append(asyncio.ensure_future(fetch(session,url)))

        responses=await asyncio.gather(*tasks)
        for i in range(len(responses)):
            d[i]=responses[i]
        return jsonify(d)

async def infun(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

@app.route('/def')
async def ddd():
    tasks=[]
    d={}
    st=time.time()
    names=['pune','ahmedabad','nashik','mumbai','delhi','banglore','hayderabad','chennai','asaam','manipur','surat','rajkot','kutch','bhuj','varansi','ahmedabad']
    for name in names:
        url=f'http://api.openweathermap.org/data/2.5/weather?q={name}&APPID=e9dc35968dad4441862cc6c824889e60'
        tasks.append(asyncio.ensure_future(infun(url)))

    responses=await asyncio.gather(*tasks)
    for i in range(len(responses)):
        d[i]=responses[i]
    # return jsonify(d)
    return "got"


if __name__ == '__main__':
    # nest_asyncio.apply()
    app.run(debug=True)