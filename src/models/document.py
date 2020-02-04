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