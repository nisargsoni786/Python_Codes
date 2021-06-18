from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base=declarative_base()

class Stu(Base):
    __tablename__='Student'

    id=Column('id',Integer, primary_key=True)
    name = Column('name',String)