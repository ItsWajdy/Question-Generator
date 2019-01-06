from nltk.parse.corenlp import CoreNLPParser
from nltk.corpus import brown
from nltk import WhitespaceTokenizer
from random import randint


class TrueFalseQuestions:

    def __init__(self, filename, port):
        self.filename = filename
        self.port = port
        self.prepare_similars()
        pass

    def prepare_similars(self):
        with open(self.filename, 'r') as f:
            text = f.read()

        self.parser = CoreNLPParser('http://localhost:' + str(self.port), tagtype='ner')
        tokens = text.split(' ')
        ner_tagged = self.parser.tag(tokens)

        self.all_ner_tags = {}
        last = 'O'
        sent = ''
        for w, tag in ner_tagged:
            if tag == 'O':
                if last != 'O' and len(sent) > 0:
                    if last in self.all_ner_tags.keys():
                        self.all_ner_tags[last].append(sent)
                    else:
                        self.all_ner_tags[last] = [sent]
                sent = ''
                continue
            if tag == last:
                if len(sent) > 0:
                    sent += ' ' + w
                else:
                    sent += w
            else:
                if last != 'O' and len(sent) > 0:
                    if last in self.all_ner_tags.keys():
                        self.all_ner_tags[last].append(sent)
                    else:
                        self.all_ner_tags[last] = [sent]
                sent = w
            last = tag

        for key, li in self.all_ner_tags.items():
            stt = set(li)
            li = []
            for word in stt:
                li.append(word)
            self.all_ner_tags[key] = li

    def get_false_sentence(self, sentence):
        ner_tag = self.parser.tag(sentence.split(' '))
        last = 'O'
        tagged_sentence = []
        sent = ''
        index = 0
        for w, tag in ner_tag:
            index +=1
            if tag == last:
                if sent:
                    sent += ' ' + w
                else:
                    sent += w
            else:
                if last != 'O':
                    tagged_sentence.append((sent, last))
                sent = w
            if index == len(ner_tag) and tag!='O':
                tagged_sentence.append((sent,tag))

            last = tag

        candidate_wrong = []
        for gap , tag in tagged_sentence:
            if tag not in self.all_ner_tags.keys():
                continue
            length = len(self.all_ner_tags[tag])
            if length < 2:
                continue
            while True:
                rep = self.all_ner_tags[tag][randint(0,length-1)]
                if rep != gap:
                    break
            candidate_wrong.append(sentence.replace(gap , rep))

        return candidate_wrong
