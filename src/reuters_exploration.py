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

len(reuters.categories())
cat = reuters.fileids(['acq'])[0]
reuters.raw(cat)

# 2/4/2020
# Look for seed words and reasonable extraction patterns
# Good seed word: A seed word is some word that is generally related to this type of event.
# HW: Come in with 10 words - pull the entire sentence with seed words and doc ids.
# Think about semantic categories you are identifying.

# Setup SQL alchemy

# Next week: talk through the scoring methods