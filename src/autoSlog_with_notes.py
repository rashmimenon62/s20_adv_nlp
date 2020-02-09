import nltk
import spacy
en = spacy.load('en_core_web_lg')
#nltk.download('reuters')
from nltk.corpus import reuters

# spacy has concepts of a span
# a sentence is a span.
# you can do merges of spans...
# it used to be that you could take them individually but then it would pass to document
# ash but what you msut do 1st nos is retokenize.
# with doc.retokenize() as retoknizer:
    # retokenizer.merge(doc[0:2])
# so now you have sentence level indeces and then you can say it's word 2 of sentence 10..
# but actually word no. 105 o the documen ...


# say we want to pull 10 documents from routers
# "with doc
class PatternExtractor:
    def __init__(self,text):
        self.text = text
        # run spacy
        self.analyzed = en(self.text)
        # so now we can fire that at top:
        self.examine_sentences()
        self.base_patterns = {}

        # we want it to always have text of file
        # at this point
        def examine_sentences(self):
            for sentence in self.analyzed.sents:
                print(sentence)
                print('---')
                with sentence.retokenize() as retokenize()
                    # chunk instelf is a span
                # we need start and end...
                # once we merge we have new version of sentence
                # so apparenlty lookin@ sentence level isn't good. have to go up to doc level
                # so retokenize entire doc...
                for token in sentence.noun_chunks:
                    print("\t",token.text)
                    #print("\t",token.text)
                    # the cunks look WHOOO kay.
                    # to make life even easier... we can RE-TOKENIZE the text
                    # if we recall "This is a Test"
                    # tokens are    ____ __ _ ____
                    # in a sentence like this: 'The exports grew after the new sanctions expired
                    # you can retokenize s.t.   ___________ ____ _____ ___ ___ _________ _______
                    # we re-tokenized it so in effect it keeps the relationships.
                    # there are two libraries to re-tokenize things based on a chunks
                    # can also do it based on the named entities...
# oh, fuck, so yeah he identified noun chunks at DOCUMENT level
# so then when he retokneized all noun chunks (are still chunks, btw) but they are all one token
# he just did print to look for reallllly long-bois as tokens...
# so PROBLEM YOUC AN HAVE is when you call method of your analyze text, or the nlp text...
# are the offsets the OLD offsets or NEW ones...
# SO STEPHE TRIES TO RESET IT SOMEHOW....
        for sentence in self.analyzed.sents:
            for token in sentence:
                print(token.text, "-",token.head.text,'-',token.dep_)

    def check_and_add_pattern(self,verb,noun,rel):
        if verb not in self.base_patterns.keys():
            self.base_patterns[verb] = {}
            # so this si where we will store the rule?!
            # by this line we know verb has to exist
        # we will say that next key is relationship type..
        # then value is appropriate noun-phrase
        if rel not in self.base_patterns[verb] :
            self.base_patterns[verb][rel]= {}
            # now we can see if noun phrase occurs in list
        if noun not in self.base_patterns[verb][rel]:
            self.base_patterns[verb][rel].append(noun)

        #token.head.text, token.
# so stephe goes into displacy and shows root of sentence as well as a bunch of other stuff that show us relationships
# between every part of the sentence.
# comp is ccomp is complement analyzer? it projets another miniature sentnece?
# so you can see one nsubject and then another nsubject...
# stephen tries to descend tree from verb (at top??) back..
# but each token shoud hav ea relationships with something else
# give me the thing give me the word it is related to.
# he also wants tolook @
# when you look @ tokens you can see head....and get it out of the SENTENCE?!

# so is head like.... the parent as opposed to child?
# he also wants to pul relationship... is it with head....
# how does he reset it
# how to get noun chunks...
# do doc.noun_chunkns
for index, fid in reuters.fileids():
    if index ==10:
        break
    text = reuters.raw(fid)
    PatternExtractor(text)
# for autoslog we have to use spacy to process the document. it will give us access to each sentences

# we need to merge noun phrases....
# one thing we COULD DO... is write code up at top of loop
# write class

# anyway so he prints sentence....
# key idea is you are gettng closer to what you want....

# you can extract some of the patterns...

# so what exactly is head?!
# tephe is trying to show us each toekn, it's head and the relationship....

# so stephen will skip verb infinitive and something identity
# so stephe is going to start adding in rules...
# then bomb against target
# stuff where there are prepositions
# you can get prepositional objects but can't get larger things...

# so if we just want to get noun-subject and objects

# so stephen is showing us

# we are beginning to ee different phraseologies...
# but the idea is he is looking for interesting relatinships...

# so now stephen says we can create a limited list of patterns...
# SO NOW WE NEED TO FORM DEM BOIS...
# and try to pull stuff out...

# so stephe says that you will always see noun phrase out...

# so you pull out word and get list of possible words...
# 1st option is when in dobut start with dictionary or a list

# what do we use as key, nou phrase or verb
# key is the verb..... and then value (or 1st entry is reltationship between object and subject.... or something0

# but that first entry in value will be a key to anew ditionary

# one key for the verb, then another key for relationship.... and then you add the noun phrase

#stephe asks how we sort these
# stephe also says can we further narrow the types of verbs....
# he wants to see stuff that is more relevant...

# oh shit so he's talking about doing mutual stuff...

# to complete auto-slog ts bit

# OK so what we need people to do in next week.....
# go over 10k documents....

# stephe would say maybe look for viruses, look for terrorist stuff
# identify a genre and focus on that

# so we will talk about semantic lexicon more...

# so we can pull patterns out...

# so we are "kinda" developing autoslog...

# the other thing is we "HAVE these patterns"

# an then we want to compute relevance statistics

# the thought will be to find targets inside of reuters corpus worth investigating
# so that will be a task

# what would be useful is as part of a grade
# so two of our friends will talk about the papers...

# so we should say waht we DIDN'T get and waht we got...

if not engine.dialect.has_table(engine, 'reuters_docs'):  # If table don't exist, Create.
    # Create a table with the appropriate Columns
    metadata = db.MetaData(engine)
    Table('reuters_docs', metadata,
          db.Column('id', db.Integer, primary_key=True),
          db.Column('doc_id', db.String(length=900)), db.Column('categories', db.String()),
          db.Column('body', db.String()))
    # Implement the creation
    metadata.create_all()

    __tablename__ = 'reuters_docs'
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.String(length=900))
    categories = db.Column(db.String())
    body = db.Column(db.String())