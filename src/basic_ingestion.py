import nltk
nltk.download('reuters')
from nltk.corpus import reuters

print(reuters.categories())

import spacy
nlp = spacy.load("en_core_web_lg")

class Entity:
    def __init__(self):
        self.text = None # the actual text that spacy extracts
        self.begin = None # the start offset of the named entity
        self.end = None # the end offset of the named entity
        self.label = None # the label associated with the entity

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def __repr__(self):
        return "<Entity: " + self.text + ">"

class Document:
    def __init__(self):
        self.id = None
        self.text = None
        self.entities = []

    def setId(self, id):
        self.id = id

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def addEntity(self, entity):
        self.entities.append(entity)

    def getEntities(self):
        return self.entities


documentArr = []
for fileid in reuters.fileids():
    #print(fileid)
    document = Document()
    document.setId(fileid)
    docText = reuters.raw(fileid)
    document.setText(docText)
    spacyDoc = nlp(docText)
    for ent in spacyDoc.ents:
        entity = Entity()
        entity.setText(ent)
        document.addEntity(entity)

    print("Added " + str(len(document.getEntities())) + " entities to doc " + fileid )
    documentArr.append(document)

print("Created " + str(len(documentArr)) + " documents")

# Steps
# 1 - load reuters
#       from NLTK
# 1a - load spacy
# 1b - load spacy model
# 2 - Iterate through and turn into doc objects
# 3 - Extract entities
# 3b - Store entities in appropriate objects
# 4 - Insert docs into storage system
# 5 -
