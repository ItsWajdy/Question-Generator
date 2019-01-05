import numpy as np
import codecs
from sentences_selection import SentenceSelection
from gap_selection import GapSelection
from question_formation import QuestionFormation
import csv
from nltk.parse import CoreNLPParser
from stanfordcorenlp import StanfordCoreNLP
import nltk
#English
"""
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 9000 -port 9000 -timeout 15000 & 
"""

#Arabic
"""
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-arabic.properties -preload tokenize,ssplit,pos,parse -status_port 9005  -port 9005 -timeout 15000
"""


#Sentence Selection test
# sent_selection = SentenceSelection()
# important_sents = sent_selection.prepare_sentences('arabic.txt')
# print(len(important_sents))
# print(dict(important_sents))

#
# parser = CoreNLPParser('http://localhost:' + str(1234))
# parsed_sentence = list(parser.raw_parse((sents)))
# print(type(parsed_sentence))
# print(parsed_sentence)

#Gap Selection test

port = 9005
sent_selection = SentenceSelection()
gap_selection = GapSelection(port)


important_sents = sent_selection.prepare_sentences('obama_short.txt')
print('important sentences len : ' , len(important_sents))

candidates = gap_selection.get_candidates(important_sents)
print('candidates len : ' , len(candidates))
print(candidates)
print('-----------------')
qf = QuestionFormation()
qf.form_questions(candidates)



"""
(ROOT
  (S
    (NP (NNP Barack) (NNP Hussein) (NNP Obama) (NNP II))
    (VP
      (VBZ is)
      (NP
        (NP (DT an) (JJ American) (NN politician))
        (VP
          (VBG serving)
          (PP
            (IN as)
            (NP
              (NP (DT the) (JJ 44th) (NN President))
              (PP (IN of) (NP (DT the) (NNP United) (NNPS States))))))))))
------------

"""
