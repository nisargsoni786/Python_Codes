import mongoengine

def connect_db():
    database_name="jsn"
    DB_URI="mongodb+srv://admin:1234567890@cluster0.jnepj.mongodb.net/jsn?retryWrites=true&w=majority"
    mongoengine.connect(host=DB_URI)