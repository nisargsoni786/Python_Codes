from sqlalchemy import Column,Integer,String,BigInteger,ForeignKey
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Log(UserMixin ,Base):
    __tablename__='Logs'

    id=Column('id',Integer, primary_key=True)
    name = Column('name',String(50))
    username = Column('username',String(100))
    password=Column('password',String(100))

class Stu(Base):
    __tablename__='Student'

    id=Column('id',Integer,primary_key=True)
    name = Column('name',String(100))
    