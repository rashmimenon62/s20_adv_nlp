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

class SeedSentences(db.Model):
    __tablename__ = 'seed_sentences'
    id = db.Column(db.Integer, primary_key=True)
    reuters_doc_id = db.Column(db.Integer)
    begin_offset = db.Column(db.Integer)
    end_offset = db.Column(db.Integer)
    sentence_text = db.Column(db.String())
    seed_word = db.Column(db.String())
