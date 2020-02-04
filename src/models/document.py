# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:51:20 2020

@author: Garrett
"""

class Document:
    def __init__(self, ID, text, model):
        self._ID = ID
        self._text = text
        self._model = model(text)
        self._entities = []

    #Id Getter
    @property
    def ID(self):
        return self._ID

    #Id Setter
    @ID.setter
    def ID(self, ID):
        self._ID = ID

    #Doc Getter
    @property
    def text(self):
        return self._text

    #Doc Setter
    @text.setter
    def doc(self, text):
        self._text = text

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
        return self.ID