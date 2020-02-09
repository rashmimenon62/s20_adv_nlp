from data_sources import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.request
import nltk
import spacy
from nltk.corpus import reuters

if not engine.dialect.has_table(engine, 'reuters_docs'):  # If table don't exist, Create.
    # Create a table with the appropriate Columns
    metadata = db.MetaData(engine)
    db.Table('reuters_docs', metadata,
          db.Column('id', db.Integer, primary_key=True),
          db.Column('doc_id', db.String(length=900)), db.Column('categories', db.Text()),
          db.Column('body', db.Text()))
    # Implement the creation
    metadata.create_all()
for fid in reuters.fileids():
    doc_body = reuters.raw(fid)
    doc_categories = "; ".join(reuters.categories(fid))
    try:
        page_analysis = ReutersDoc(doc_id=fid, body=doc_body, categories=doc_categories)
        session.add(page_analysis)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        print("*" * 25)
