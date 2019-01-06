from sentences_selection import SentenceSelection
from gap_selection import GapSelection
from true_flase_questions import TrueFalseQuestions
from question_formation import QuestionFormation
import wrong_answers

port = 1234

#Sentence Selection
sent_selection = SentenceSelection()
important_sents = sent_selection.prepare_sentences('tests/obama_short.txt')
print(len(important_sents))


#True or False Questions
tf = TrueFalseQuestions('tests/obama_short.txt' , port)
# print('_______________________________________________')
# print('True or False')
# true_false_dict = []
# i = 1
# for _ , imps in important_sents.items():
#     dic = {}
#     dic['Sentence'] = imps
#     list_of_false = tf.get_false_sentence(imps)
#     i += len(list_of_false)
#     dic['Questions'] = list_of_false
#     true_false_dict.append(dic)


# with open('true_false_question.txt' , 'w+' , encoding='utf-8') as f:
#     for d in true_false_dict:
#         f.write('Sentence : ' + d['Sentence'] + '\n')
#         f.write('Questions:\n')
#         for sent in d['Questions']:
#             f.write(sent + '\n')
#         f.write('\n__________________\n')
# print('_______________________________________________')


#Gap Selection
gap_selection = GapSelection(port)
candidates = gap_selection.get_candidates(important_sents)
print(len(candidates))


#
# with open('fill_in_gap.txt' , 'w+' , encoding='utf-8') as f:
#
#     for cand in candidates:
#         f.write(cand['Sentence'] + '\n')
#         f.write('Question: ' + cand['Question'] + '\n')
#         wrong = wrong_answers.get_wrong_answers(cand['Answer'])
#         tmp = []
#         if len(wrong) < 4:
#             tmp = tf.get_false_sentence(cand['Answer'])
#         for t in tmp:
#             wrong.append(t)
#         if len(wrong)>1:
#             i = 1
#             for w in wrong:
#                 f.write(str(i) + '. ' + w + '\n')
#                 i +=1
#                 if i>4:
#                     break
#         f.write('_____________________\n\n')



#
qf = QuestionFormation(port)
qf.form_questions(candidates)
