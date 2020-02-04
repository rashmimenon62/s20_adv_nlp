import nltk
import spacy
en = spacy.load('en_core_web_lg')
#nltk.download('reuters')
from nltk.corpus import reuters

class PatternExtractor:
    def __init__(self, text):
        self.text = text
        self.analyzed = en(self.text)
        self.base_patterns = {}
        self.examine_sentences()
        self.print_known_patterns()

    def print_known_patterns(self):
        print(self.base_patterns.keys())
        try:
            print(self.base_patterns["inflict"].keys())
        except:
            pass


    def check_and_add_pattern(self, verb, noun, rel):
        if verb not in self.base_patterns.keys():
            self.base_patterns[verb] = {}
        if rel not in self.base_patterns[verb]:
            self.base_patterns[verb][rel] = []
        if noun not in self.base_patterns[verb][rel]:
            self.base_patterns[verb][rel].append(noun)

    def examine_sentences(self):
        with self.analyzed.retokenize() as retokenizer:
            for chunk in self.analyzed.noun_chunks:
                retokenizer.merge(self.analyzed[chunk.start:chunk.end])

        for sentence in self.analyzed.sents:
            print("sentence -> ", sentence.text)
            for token in sentence:
                if token.dep_ in ["nsubj", "dobj"]:
                    #print(token.text, " - ", token.head.text, " - ", token.dep_)
                    self.check_and_add_pattern(token.head.text, token.text, token.dep_)

            print("*&" * 25)




for index, fid in enumerate(reuters.fileids()):
    if index == 5:
        break
    text = reuters.raw(fid)
    new_pe = PatternExtractor(text)
