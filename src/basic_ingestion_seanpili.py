import nltk
import spacy
en = spacy.load('en_core_web_lg')
#nltk.download('reuters')
from nltk.corpus import reuters
import json


class Entity:
    def __init__(self):
        self.text = '' # the actual text that spacy extracts
        self.begin = None # the start offset of the named entity
        self.end = None # the end offset of the named entity
        self.label = None # the label associated with the entity

    def setText(self, text):
        self.text = text

    def setOffsets(self,fIrst,laSt):
        self.begin = fIrst
        self.end = laSt
    def setLabel(self,label):
        self.label = label

    def getText(self):

        return self.text

    def getOffsets(self):
        return([self.begin,self.end])

    def getLabel(self):
        return(self.label)

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
# so we will store our documents in a nested dictionary because that can easily be converted to a .json file :)

docDict = {}
from tqdm import tqdm
for fid in tqdm(reuters.fileids()):
    # set each key in the dictionary to be the fileid...
    # then the value will be an empty instance of the Document class
    docDict[fid] = {'Doc':Document(),'ents':[]}
    docDict[fid]['Doc'].text = reuters.raw(fid)
    nlpTemp = en(docDict[fid]['Doc'].text)
    raw_ents = [[m.start_char,m.end_char,m.label_,m.text] for m in nlpTemp.ents]
    if len(nlpTemp.ents)>0:
        [docDict[fid]['ents'].append(Entity()) for x in range(len(nlpTemp.ents))]
        for x in range(len(nlpTemp.ents)):
            docDict[fid]['ents'][x].setOffsets(raw_ents[x][0], raw_ents[x][1])
            docDict[fid]['ents'][x].setLabel(raw_ents[x][2])
            docDict[fid]['ents'][x].setText(raw_ents[x][3])
            docDict[fid]['Doc'].addEntity(docDict[fid]['ents'][x])

# now that we have the data structure we want (although it is a bit redundant because we have
# a dictionary containing documents that have entities added as well as a separate value containing the entities themselves
# we will put all of this in a format that everyone will be able to load from a json

import json


json_container = {}
for fid in tqdm(reuters.fileids()):
    json_container[fid] = {'Text':docDict[fid]['Doc'].text,'entities':[[{'Entity_Text':docDict[fid]['ents'][x].text,'Entity_Begin':docDict[fid]['ents'][x].begin,'Entity_End':docDict[fid]['ents'][x].end,'Entity_Label':docDict[fid]['ents'][x].label}]for x in range(len(docDict[fid]['ents']))]}



with open('adv_NLP_reuters.txt', 'w') as outfile:
    json.dump(json_container, outfile)






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

#key_list = list(docDict.keys())
# for x in range(len(en('My name is Samuel Edward Jackson and my Sister is Frank Castle').ents)):
#     dd['a']['ents'].append(Entity())
#     nlpTemp = en('My name is Samuel Edward Jackson')
#     raw_ents = [[m.start_char,m.end_char,m.label_,m.text] for m in nlpTemp.ents]
#     dd['a']['ents'][-1] .setOffsets(raw_ents[0][0],raw_ents[0][1])
#     dd['a']['ents'][-1].setLabel(raw_ents[0][2])
#     dd['a']['ents'][-1].setText(raw_ents[0][3])



