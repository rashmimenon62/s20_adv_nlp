from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import db


db.metadata.clear()

class ReutersDoc(db.Model):
    __tablename__ = 'reuters_docs'
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.String(length=900))
    categories = db.Column(db.String())
    body = db.Column(db.String())

