import numpy as np
import codecs
from sentences_selection import SentenceSelection
from gap_selection import GapSelection
import wrong_answers
from question_formation import QuestionFormation
import csv
from nltk.parse.corenlp import CoreNLPParser
from stanfordcorenlp import StanfordCoreNLP
import nltk
from nltk.corpus import brown
from true_flase_questions import TrueFalseQuestions
#English
"""
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 1234 -port 1234 -timeout 30000 & 
"""

#Arabic
"""
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-arabic.properties -preload tokenize,ssplit,pos,lemma,ner,parse -status_port 9005  -port 9005 -timeout 30000
"""
test_sent = 'Barack Hussein Obama II is an American politician serving as the 44th President of the United States'
arabic_test_sent = 'باراك أوباما واسمه الكامل باراك حسين أوباما الابن هو الرئيس الرابع والأربعون للولايات المتحدة الأمريكية'


#parser = CoreNLPParser('http://localhost:' + str(1234) , tagtype='ner')



#Sentence Selection test
sent_selection = SentenceSelection()
important_sents = sent_selection.prepare_sentences('obama_short.txt')
print(len(important_sents))

# tokens = nltk.word_tokenize(test_sent)
# tagged = nltk.pos_tag(tokens)
# ne_chunk = nltk.ne_chunk(tagged)
#
#
# print(ne_chunk)
# print('------------------')

# stanford_tagged = parser.tag(arabic_test_sent.split())
# print(stanford_tagged)

#
# parser = CoreNLPParser('http://localhost:' + str(1234))
# parsed_sentence = list(parser.raw_parse((sents)))
# print(type(parsed_sentence))
# print(parsed_sentence)

#Gap Selection test
#
port = 1234
gap_selection = GapSelection(port)
candidates = gap_selection.get_candidates(important_sents)




# important_sents = sent_selection.prepare_sentences('obama_short.txt')
# print('important sentences len : ' , len(important_sents))
#

tf = TrueFalseQuestions('obama_short.txt' , port)
print('candidates len : ' , len(candidates))

for cand in candidates:
    print(cand['Sentence'])
    print('Question: ' , cand['Question'])
    wrong = wrong_answers.get_wrong_answers(cand['Answer'])
    #if len(wrong)>1:
    #    print('True or False')
    #    print(tf.get_false_sentence(cand['Answer'] , cand['Question'] , wrong))
    #print('Answer : ' , cand['Answer'])
    #print('similar' , tf.get_false_sentence(cand['Answer']))
    print(tf.get_false_sentence(cand['Sentence']))
    print('-------------------------------------')
print('-----------------')



#qf = QuestionFormation()
#qf.form_questions(candidates)



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
