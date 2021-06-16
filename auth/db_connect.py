import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


engine = create_engine("mysql+pymysql://root:password@localhost/new")
Base.metadata.create_all(bind=engine)
conn=engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
sess=Session()