# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:51:20 2020

@author: Garrett
"""

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
        return f'<{self.name}: {self.text}>'