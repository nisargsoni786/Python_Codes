from flask import Flask,jsonify,request
import redis
from celery import Celery

app = Flask(__name__)

app.config['CELERY_BROKER_URL']='redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND']='redis://localhost:6379/0'

celery=Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task()
def func():
    print("in function !")

@app.route('/')
def index():
    func.delay()
    return "Helo world !!!"

if __name__ == '__main__':
    app.run(debug=True)