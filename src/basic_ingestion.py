#Author: Charles Garrett Eason
#Class: Advanced NLP
#Version: .01
#encoding: utf-8

#%% Packages
import spacy
from nltk.corpus import reuters
import pickle
from tqdm import tqdm
from models import Entity
from models import Document
model = spacy.load("en_core_web_lg")

#%% Execution
docDict = {}
for ID in tqdm(reuters.fileids()):
    doc_ob = Document(ID, reuters.raw(ID), model=model)
    for ent in doc_ob.model.ents:
        doc_ob.addEntity(Entity(ent))
    docDict[ID] = {
        'Doc' : doc_ob, 
        'ents' : doc_ob.entities
    }

#Writing
f = open('docDict', 'wb')
pickle.dump(docDict, f)
f.close()

#Reading
# f = open('doc_list', 'rb')
# doc_list = pickle.load(f)
# f.close()

