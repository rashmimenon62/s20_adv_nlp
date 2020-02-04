# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:51:20 2020

@author: Garrett
"""

from nltk.corpus import reuters
reuters.readme()
d = {}
for i in reuters.categories():
    d[i] = len(reuters.fileids(i))

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

cat = reuters.fileids(['acq'])[0]
reuters.raw(cat)
