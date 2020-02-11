import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = db.create_engine(
    'mysql+mysqlconnector://nlpuser:nlpuserpassword@localhost:3306/gw_nlp?charset=utf8',
)
connection = engine.connect()
metadata = db.MetaData()

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

sqlDF = pd.read_sql_table("reuters_docs", con=engine)

print("Num docs: {}".format(len(sqlDF)))

def sort_w_col_idx(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

# get the feature names and tf-idf score of top n items
def extract_topn_words(feature_names, sorted_items, topn=10):

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


docs=sqlDF['body'].tolist()

cv=CountVectorizer(max_df=0.85,stop_words="english")
# cv.fit would only create the vocabulary,
# # cv.fit_transform creates the vocabulary and returns a term-document matrix
word_count_vector=cv.fit_transform(docs)

# let’s look at 10 words from our vocabulary
print(list(cv.vocabulary_.keys())[:10])

# compute the IDF values. Take the sparse matrix from CountVectorizer
# (word_count_vector) to generate the IDF
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

feature_names=cv.get_feature_names()

top_words = []
for idx, doc in enumerate(docs):
    # generate tf-idf for the given document
    tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))

    # sort the tf-idf vectors by descending order of scores
    sorted_items = sort_w_col_idx(tf_idf_vector.tocoo())

    # extract only the top n
    keywords = extract_topn_words(feature_names, sorted_items, 5)

    # print the results
    if idx % 2000 == 0:
        print("\n=====Doc=====")
        print(doc)

        print("\n===Keywords===")
        for k in keywords:
            print(k, keywords[k])

    top_words.append(keywords)

sqlDF['top_words'] = top_words
print(sqlDF.iloc[:3]['top_words'])

# get unique categories
array_cats = sqlDF['categories'].str.split(pat="; ").to_list()
cats = list(set(np.concatenate(array_cats)))

print("Num cats: {}".format(len(cats)))
print(cats)

# get the top n special words for each cat
for cat in cats:
    catDF = sqlDF[sqlDF['categories'].str.contains(cat)]
    print("{} docs are tagged {}".format(len(catDF), cat))

    # Combine all of the top_words fields for the catDF
    master_wordlist = {}
    for row in catDF['top_words'].values:
        curr_dict = row

        for key in curr_dict:

            if key not in master_wordlist or curr_dict[key] > master_wordlist[key]:
                master_wordlist[key] = curr_dict[key]


    sorted_wordlist =  sorted(master_wordlist.items(), key=lambda x: x[1], reverse=True)[:20]
    print("Top 20 Sorted word list for {}: {}".format(cat, sorted_wordlist))
