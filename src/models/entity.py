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