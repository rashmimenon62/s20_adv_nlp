from data_sources import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.request
import nltk
import spacy
from nltk.corpus import reuters


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
