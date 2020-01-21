# from nltk.corpus import reuters
#
#
# import spacy
# nlp = spacy.load("en")

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

    def printName(self):
        print(self.name)

    def __repr__(self):
        return "<Entity: " + self.text + ">"

class Document:
    def __init__(self):
        self.text = None
        self.entities = []

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def addEntity(self, entity):
        self.entities.append(entity)

    def getEntities(self):
        return self.entities

document = Document()
document.setText("This is a text of any text to see")
print(document.getText())


entity = Entity()
entity.setText("any text")
print(entity.getText())

document.addEntity(entity)
print(document.getEntities())




# for fileid in reuters.fileids():
#     print(fileid)


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
