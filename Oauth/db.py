from loguru import logger
import pymongo
from pymongo import MongoClient

def init_db():
    try:
        # server info is used to make client connection at initialisation state
        global db
        logger.info(f"Initalising the database")
        # DATABASE_URL = f'mongodb://{db_user}:{db_password}@{db_host}:{db_port}/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000'
        DATABASE_URL = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'
        client = MongoClient(DATABASE_URL, maxPoolSize=10, minPoolSize=10)
        info = client.server_info()
        db = client.oauth
    except Exception as e:
        logger.error(f'Error to connect with DB: {e}')
        db = None
    return db


def get_db():
    global db
    if db is not None:
        return db
    else:
        raise Exception("Not able to connect to database")