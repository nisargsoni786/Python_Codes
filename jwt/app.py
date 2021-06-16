from flask import Flask,render_template,jsonify,request,session,url_for,redirect,flash,session,make_response
from auth import auth
from db_connect import sess
from models import Log,Stu
import jwt,datetime
from db_connect import sess
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)
app.config['SECRET_KEY']="1234567890"

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None

        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']

        if not token:
            return jsonify({"message":"Token is missing"}),401
        
        try:
            data=jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user =sess.query(Log).filter_by(username=data['username']).first()
        except:
            return jsonify({"Message":"Token is invalid"}),401
        return f(current_user,*args,**kwargs)
    return decorated


@app.route('/',methods=['GET'])
@token_required
def getalluser(current_user):
    usrs=sess.query(Log).all()
    ans=[(i.id,i.name) for i in usrs]
    return {"Data":ans,"Current":current_user.username+" "+current_user.name}

@app.route('/user',methods=['POST'])
@token_required 
def add_stu(current_user):
    data=request.get_json()

    hashed=generate_password_hash(data['password'],method='sha256')
    usr=Log(name=data['name'],username=data['username'],password=hashed)

    sess.add(usr)
    sess.commit()
    return {"data":data,"OK":"Created"}

@app.route('/user/<int:id>',methods=['PUT'])
@token_required
def update_stu(curent_user,id):
    data=request.get_json()
    sess.query(Stu).filter_by(id=id).update(data)
    sess.commit()
    return {"data":data,"OK":"Updated"}

@app.route('/user/<int:id>',methods=['DELETE'])
@token_required
def delete_stu(current_user,id):
    usr=sess.query(Log).filter_by(id=id).first()
    sess.delete(usr)
    sess.commit()
    return {"OK":"Deleted"}

@app.route('/login')
def login():
    auth=request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Couldn't varify",401,{"WWW-Authenticate":"Basic realm='Login required'"})

    user = sess.query(Log).filter_by(username=auth.username).first()

    if not user:
        return make_response("user not found",401,{"WWW-Authenticate":"Basic realm='user doesnt exist'"})  
    
    if check_password_hash(user.password,auth.password):
        token=jwt.encode({'username':user.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({"token":token})

    return make_response("user not found",401,{"WWW-Authenticate":"Basic realm='user doesnt exist'"}) 

if __name__ == '__main__':
    app.run(debug=True)
