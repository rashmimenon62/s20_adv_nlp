import spacy

nlp = spacy.load('en_core_web_lg')


class entity_mentions:

    def __init__(self):

        self.doc_id = ''

        self.ent_id = []

        self.ent_name = ''

        self.text = ''

        self.toks = None

        self.nlp_doc = None

        self.entity = ''

        self.before = None

        self.after = None

        # so, I figure that what'll happen is

        # at times... there won't be available stuff on right and on left.... so i'll store separately

        # at least initially.

        self.right_context = []

        self.left_context = []

    def docInit(self, docId, docText):

        if self.doc_id != '':
            return (print(
                'You have already set a document... and this implementaiton only allows entitty mentions from ONE document')

                    )

        self.doc_id = docId

        self.text = docText

        # self.nlp_doc = nlp(self.text)

    def add_entity(self, entity):

        if self.entity != '':

            return (print(
                'You already set an entity, this implementation only allows one entity mention as it will be eventually appended as a field to an entity class'))

        else:

            self.entity = entity

    def set_mentions(self):

        if self.entity == '' or self.text == '':

            return (print(
                'You either need to add a document and use add_entity method to add an entity, or just the last option '))

        else:

            inpt = int(input('How many tokens do you want from the beginning and end of the word? '))

            preceed = True

            prOceed = True

            # sometimes there is no preceeding text to entity

            # if there isn't..... then we move on past this part....

            # if not, we will grab out the text before it

            if 0 == self.entity.begin:
                print('no preceeding text')

                preceed = False

            if preceed:

                print(self.entity.begin)

                # halfT1 =

                half1 = nlp(self.text[0:self.entity.begin])

                if len(half1) < inpt:

                    ments1 = [i.text for i in half1]



                else:

                    ments1 = [i.text for i in half1[-inpt:]]

                self.before = ments1

            # now we want to get the text after the entity

            if len(self.text) - 1 == self.entity.end:
                print('no prOceeding text')

                prOceed = False

            if prOceed:

                half2 = nlp(self.text[self.entity.end:].strip())

                if len(half2) < inpt:

                    ments2 = [i.text for i in half2]

                else:

                    ments2 = [i.text for i in half2[0:inpt]]

                self.after = ments2