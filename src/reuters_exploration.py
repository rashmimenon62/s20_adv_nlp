# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:51:20 2020

@author: Garrett
"""
#%% Packages
import spacy
from nltk.corpus import reuters
en = spacy.load("en_core_web_lg")

#%% Reuters exploration
reuters.readme()
d = {}
for i in reuters.categories():
    d[i] = len(reuters.fileids(i))

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

len(reuters.categories())
txt = reuters.fileids(['acq'])[0]
print(reuters.raw(txt))

# 2/4/2020
# Look for seed words and reasonable extraction patterns
# Good seed word: A seed word is some word that is generally related to this type of event.
# HW: Come in with 10 words - pull the entire sentence with seed words and doc ids.
# Think about semantic categories you are identifying.

# Setup SQL alchemy

# Next week: talk through the scoring methods

#%% Using Model
txt = reuters.raw(reuters.fileids(['acq'])[0])
print(txt)


processed = en(txt)

for token in processed:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
    
for np in processed.noun_chunks:
    print(np, np.root.dep_)























