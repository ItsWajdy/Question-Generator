from sentences_selection import SentenceSelection
from gap_selection import GapSelection
from nltk.parse import CoreNLPParser
from stanfordcorenlp import StanfordCoreNLP


#Arabic
"""
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-arabic.properties -preload tokenize,ssplit,pos,parse -status_port 1234  -port 1234 -timeout 25000

"""



sent_selection = SentenceSelection()
important_sents = sent_selection.prepare_sentences('arabic.txt')
print('important sentences len : ' , len(important_sents))

# parser = StanfordCoreNLP(r'C:\Program Files\Stanford CoreNLP\stanford-corenlp-full-2018-10-05', lang='ar')
#
#

#
port = 1234
gap_selection = GapSelection(port)
candidates = gap_selection.get_candidates(important_sents)
print('candidates len : ' , len(candidates))
for cand in candidates:
    print(cand['Question'])
    print(cand['Answer'])
    print('---------------------')


# parser = CoreNLPParser('http://localhost:' + str(1234))
#
# for id , sent in important_sents.items():
#     print(sent)
#     tree = parser.parse(sent)
#     for t in tree:
#         print(t)
#     print(tree)
#     print('----------------')
#


"""
(ROOT
  (S
    (VP
      (VBD حاز)
      (PP (IN على) (NP (CD ثلاث) (NP (NNS فترات))))
      (PP (IN في) (NP (NN مجلس) (NP (DTNN الشيوخ))))
      (PP (IN ب) (NP (DTNN الينوي)))
      (NAC
        (CC و)
        (PP
          (NP (DT ذلك))
          (IN في)
          (NP (NP (DTNN الفترة)) (PP (IN من) (NP (CD 1997))))))
      (PP (IN الى) (NP (CD 2004))))))
"""


"""
(ROOT
  (S
    (S
      (CC و)
      (NP
        (NP
          (NN عقب)
          (NP
            (NN محاولة)
            (NP
              (NN غير)
              (NP
                (NP (NN ناجحة))
                (PP
                  (IN ل)
                  (NP
                    (NP (DTNN الحصول))
                    (PP
                      (IN على)
                      (NP
                        (NP (NN مقعد))
                        (PP
                          (IN في)
                          (NP (NN مجلس) (NP (DTNN النواب))))))))))))
        (NP (NN عام) (NP (CD 20))))
      (VP
        (VBD رشح)
        (NP (NN نفس) (NP (PRP$ ه)))
        (PP (IN ل) (NP (NN مجلس) (NP (DTNN الشيوخ))))
        (NP (NN عام) (NP (CD 2004,)))))
    (CC و)
    (S
      (S
        (VP
          (VBD استطاع)
          (SBAR
            (IN ان)
            (S
              (VP
                (VBP يحوز)
                (PP
                  (IN على)
                  (NP (NP (NN مقعد)) (PP (IN ب) (NP (DTNN المجلس)))))
                (PP (IN في) (NP (NN مارس) (NP (CD 2004,)))))))))
      (CC و)
      (S
        (VP
          (VBD استطاع)
          (PP (IN ب) (NP (NP (DT هذا)) (NP (DTNN الفور))))
          (NP
            (NN جذب)
            (NP (NN انتباه) (NP (DTNN الحزب) (DTJJ الديمقراطي))))))
      (PUNC ,)
      (CC و)
      (S
        (VP
          (VBD كان)
          (NP
            (NP
              (NP (NN خطاب) (NP (PRP$ ه)))
              (ADJP (DTJJ التلفزيوني)))
            (SBAR
              (WHNP (WP الذي))
              (S
                (VP
                  (VBD تم)
                  (NP (NN بث) (NP (PRP$ ه)))
                  (NP (JJ محليا))
                  (NP
                    (NN خلال)
                    (NP
                      (DTNN المؤتمر)
                      (DTJJ الوطني)
                      (DTJJ الديمقراطي)))
                  (PP
                    (IN في)
                    (NP
                      (NP (NN يوليو))
                      (PP (IN من) (NP (NN عام) (NP (CD 2004))))))))))
          (VP
            (VBD جعل)
            (NP (PRP ه))
            (NP
              (NP (NN نجما) (JJ صاعدا))
              (PP (IN على) (NP (DTNN الصعيد) (DTJJ الوطني))))
            (PP (IN في) (NP (DTNN الحزب)))))))))
"""


"""
(ROOT
  (S
    (S
      (CC و)
      (NP (NN بعد) (NP (PRP ها)))
      (VP
        (VBD تم)
        (NP
          (NP (NN انتخاب) (NP (PRP$ ه)))
          (PP
            (IN ل)
            (NP (NN عضوية) (NP (NN مجلس) (NP (DTNN الشيوخ))))))
        (PP (IN في) (NP (NN نوفمبر) (NP (CD 2004))))))
    (CC و)
    (S
      (VP
        (VBD حاز)
        (PP
          (IN على)
          (NP
            (NP (ADJP (JJR اكبر) (NP (NN نسبة))))
            (PP (IN في) (NP (NN تاريخ) (NP (DTNN الينوي))))))))))
"""
