from flask import Flask,request,jsonify
from flask_pydantic import validate
from pydantic import BaseModel, StrictStr

app = Flask(__name__)

class base(BaseModel):
    name : StrictStr
    no : int

class base2(BaseModel):
    mul: float

@app.route('/')
@validate()
def index(body: base):
    return jsonify(request.get_json())

@app.route('/mul')
@validate()
def index2(body: base2):
    return jsonify(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)