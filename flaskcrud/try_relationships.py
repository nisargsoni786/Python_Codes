from flask import Flask,jsonify,request
import sqlalchemy
from sqlalchemy import Column,Integer,String,BigInteger,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session,relationship
from werkzeug.utils import redirect


app=Flask(__name__) 
Base=declarative_base()


class Stu(Base):
    __tablename__='Student'

    id=Column('id',Integer, primary_key=True)
    name = Column('name',String)
    mark=relationship("Mark")

class Mark(Base):
    __tablename__="Marks"

    id=Column(Integer, primary_key=True)
    math=Column(Integer)
    sci=Column(Integer)
    stuid=Column(Integer,ForeignKey('Student.id'))
    student=relationship("Stu")

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/new'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
#conn=engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
sess=Session()

@app.route('/add')
def a():
    try:
        # id=request.args['id']
        if not request.args.get('name'):
            print('\n\n\n\n\n\n',"its not there",'\n\n\n\n\n')
        name=request.args.get('name',default="hey")
        st=Stu(name=name)
        sess.add(st)
        sess.commit()
        return {'success':"True","data":{'name':name}}
    except Exception as e:
        return {"error":e}

@app.route('/all')
def all():
    try:
        st=sess.query(Stu).all()
        print([i.name for i in st])
        return ({'data':[i.name for i in st]})
    except Exception as e:
        return {"error":e}

@app.route('/fetch')
def ge():
    st=sess.query(Stu).filter_by(name='Nisarg',id=1).first()
    print(st)
    # print('\n\n\n\n\n\n\n',st[0].id,st[0].name,'\n\n\n\n\n\n\n')
    return {"data":"check"}

@app.route('/del')
def de():
    st=sess.query(Stu).filter_by(name='A').first()
    sess.delete(st)
    sess.commit()
    return "Deleted!!!"

@app.route('/update')
def update():
    id=request.args['id']
    newname=request.args['newname']
    st=sess.query(Stu).filter_by(id=id).first()
    st.name=newname
    sess.commit()
    return "Update complete"

@app.route('/addm')
def b():
    try:
        mm=Mark(id=1,math=100,sci=200,stuid=2)
        sess.add(mm)
        sess.commit()
        return "Data Added!"
    except Exception as e:
        return {"error":e}

@app.route('/fetchm')
def bb():
    mm=sess.query(Mark).filter_by(id=1).first()
    print('its mm............',mm)
    print(mm.id,mm.math,mm.sci,mm.stuid)
    print('\n\ncheck relationship\n\n',mm.student,mm.student.name,mm.student.id)
    return 'mmmmmmmmm'

@app.route('/fetchm2')
def bbb():
    mm=sess.query(Stu).filter_by(id=2).first()
    print('its mm............',mm)
    print(mm.name)
    print('\n\ncheck relationship\n\n',mm.mark[0].math)
    return 'm2m2m2m2m2m2'

if __name__== '__main__':
    app.run(debug=True)
