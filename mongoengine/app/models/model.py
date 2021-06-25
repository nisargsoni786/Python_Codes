import mongoengine
import bson

class Book(mongoengine.Document):
    book_id=mongoengine.ObjectIdField(default=bson.ObjectId,primary_key=True)
    name=mongoengine.StringField(max_length=100,required=True)
    author=mongoengine.StringField(max_length=100)

    def to_json(self):
        return{
            "book_id":self.book_id,
            "name":self.name,
            "author":self.author,
        }
