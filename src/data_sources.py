import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = db.create_engine(
    'mysql+mysqlconnector://nlpuser:nlpuserpassword@localhost:3306/gw_nlp?charset=utf8',
    #     echo=True
)
connection = engine.connect()
metadata = db.MetaData()

Base = declarative_base()

class ReutersDoc(Base):
    __tablename__ = 'reuters_docs'
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.String(length=900))
    categories = db.Column(db.String())
    body = db.Column(db.String())

Session = sessionmaker(bind=engine)
session = Session()