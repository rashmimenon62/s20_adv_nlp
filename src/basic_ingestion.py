import nltk
import spacy
en = spacy.load('en_core_web_lg')
#nltk.download('reuters')
from nltk.corpus import reuters
import json


from models import Entity
from models import Document

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