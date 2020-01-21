#Author: Charles Garrett Eason
#Class: Advanced NLP
#Version: 1.0
#encoding: utf-8

#%% Packages
import spacy
from nltk.corpus import reuters
import pickle
import time

model = spacy.load("en_core_web_lg")
start = time.time()


#%% Classes and Functions
class Entity:
    def __init__(self, entity):
        self._text = entity.text # the actual text that spacy extracts
        self._begin = entity.start_char # the start offset of the named entity
        self._end = entity.end_char # the end offset of the named entity
        self._name = entity.label_ # the name associated with the entity

    #Name Getter
    @property
    def name(self):
        return self._name

    #Name Setter
    @name.setter
    def name(self, name):
        self._name = name

    #Text Getter
    @property
    def text(self):
        return self._text

    #Text Setter
    @text.setter
    def text(self, text):
        self._text = text

    #Begin Getter
    @property
    def begin(self):
        return self._begin

    #Begin Setter
    @begin.setter
    def begin(self, begin):
        self._begin = begin

    #End Getter
    @property
    def end(self):
        return self._end

    #End Setter
    @end.setter
    def end(self, end):
        self._end = end

    def __repr__(self):
        return "<"+ self.name + ": " + self.text + ">"


class Document:
    def __init__(self, id, doc, model=model):
        self._id = id
        self._doc = doc
        self._model = model(doc)
        self._entities = []

    #Id Getter
    @property
    def id(self):
        return self._id

    #Id Setter
    @id.setter
    def id(self, id):
        self._id = id

    #Doc Getter
    @property
    def doc(self):
        return self._doc

    #Doc Setter
    @doc.setter
    def doc(self, doc):
        self._doc = doc

    #Model Getter
    @property
    def model(self):
        return self._model

    #Model Setter
    @model.setter
    def model(self, model):
        self._model = model

    #Entities Getter
    @property
    def entities(self):
        return self._entities

    #Entities Adder
    def addEntity(self, entity):
        self.entities.append(entity)

    def __repr__(self):
        return self.id


#%% Execution
doc_list = []
for doc in reuters.fileids():
    doc_ob = Document(doc, reuters.open(doc).read())
    for ent in doc_ob.model.ents:
        doc_ob.addEntity(Entity(ent))
    doc_list.append(doc_ob)

#Writing
f = open('doc_list', 'wb')
pickle.dump(doc_list, f)
f.close()

#Reading
# f = open('doc_list', 'rb')
# doc_list = pickle.load(f)
# f.close()

#Runtime
end = time.time()
print('Program Complete!')
print('Runtime in seconds: ' + str(round(end - start)))
