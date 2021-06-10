from flask import Flask,request,jsonify
import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker, Session
from models import Employee,Base

app=Flask(__name__)

user=os.environ.get('user')
password=os.environ.get('password')
host=os.environ.get('host')
DB=os.environ.get('DB')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{DB}'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
conn=engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
sess=Session()

@app.route("/",methods=['GET'])
def index():
    return "Home Page"


@app.route('/add',methods=['POST'])
def create():
    try:
        data=request.get_json()

        if data.get('title')==None:
            raise Exception('ERROR title is empty')
        if data.get('experience')==None:
            raise Exception('ERROR experience is empty')

        emp=Employee(**data)
        sess.add(emp)
        sess.commit()
        return jsonify({"data":data})
    except Exception as e:
        return {"error":str(e)}


@app.route('/<int:id>/delete',methods=['DELETE'])
def delete_Employee(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!"
        sess.delete(emp)
        sess.commit()
        return "Deleted!!!"
    except Exception as e:
        return {"error":str(e)}


@app.route('/<int:id>/update',methods=['PUT'])
def updatedata(id):
    try:
        data=request.get_json()
        sess.query(Employee).filter_by(id=id).update(data)

        sess.commit()
        return "Updatedddd!"
    except Exception as e:
        return {"error":str(e)}

@app.route('/<int:id>/fetch',methods=['GET'])
def fet(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!"
        return {"id":id,"data":{"title":emp.title,"dept":emp.department,"country":emp.country,"state":emp.state,"city":emp.city,"remote":emp.remote,"description":emp.description,"requirements":emp.requirements,"benifit":emp.benifits,"comind":emp.company_industry,"job_fun":emp.job_function,"employment_type":emp.employment_type,"experience":emp.experience,"education":emp.education,"keywords":emp.keywords,"salaryFrom":emp.salary_from,"salaryTo":emp.salary_to,"currency":emp.currency}}
    except Exception as e:
        return {"Error":str(e)}

@app.route('/fetchall',methods=['GET'])
def fetch():
    try:
        emp=sess.query(Employee).all()
        if len(emp)==0:
            return "Empty DataBase"
        return {"data":[i.title for i in emp]}
    except Exception as e:
        return {"Error":str(e)}


if __name__=="__main__":
    app.run(debug=True)