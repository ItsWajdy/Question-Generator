from sentences_selection import SentenceSelection
from gap_selection import GapSelection
import codecs
import csv

port = 9000


sent_selection = SentenceSelection()
gap_selection = GapSelection(port)


important_sents = sent_selection.prepare_sentences('obama_short.txt')
print('important sentences len : ' , len(important_sents))

candidates = gap_selection.get_candidates(important_sents)
print('candidates len : ' , len(candidates))
with open('candidate_gaps.cvs' , mode='w') as file:
    column_names = ['Sentence' , 'Question' , 'Answer']
    dw = csv.DictWriter(file ,  column_names)
    dw.writeheader()
    for cand in candidates:
        dw.writerow(cand)

