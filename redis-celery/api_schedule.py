from flask import Flask,jsonify,request
import redis,random
from celery import Celery
from celery.schedules import crontab

app = Flask(__name__)
a=0

celery_beat_schedule={
    "time_scheduler":{
        "task":"api_schedule.func", # here api_schedule is file name so
        "schedule":1.0           # after every 1 sec it will call
    }
}

app.config['CELERY_BROKER_URL']='redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND']='redis://localhost:6379/0'

celery=Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(
    result_backend=app.config['CELERY_RESULT_BACKEND'],
    beat_schedule=celery_beat_schedule
    )


@celery.task(name='api_schedule.func')
def func():
    a=random.randint(0,300)
    print("in function !")
    return "jsn"


@app.route('/')
def index():
    func.delay()
    return {'a':a}

if __name__ == '__main__':
    app.run(debug=True)