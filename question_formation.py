# -*- coding: utf-8 -*-
import re, nltk
import pandas as pd
from DeepQF import Actual_Question_Formation
from nltk.parse.corenlp import CoreNLPParser
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

class QuestionFormation:

    def __init__(self , port):
        self.port = port


    def tree_to_dict(self, tree):
        """
        Aditya : Convert Tree to a usefull dict[] = <list> format
        input : tree
        output : dictionary

        """
        tree_dict = dict()
        for st in tree:
            # not everything gets a NE tag,
            # so we can ignore untagged tokens
            # which are stored in tuples
            if isinstance(st, nltk.Tree):

                input_chunked = " "
                for d in range(len(st)):
                    input_chunked = input_chunked + st[d][0] + " "

                if st.label() in tree_dict:
                    #print(" before : ",tree_dict[st.label()])
                    tree_dict[st.label()] = tree_dict[st.label()] + " " +input_chunked
                    #print(" after : ",tree_dict[st.label()])

                else:
                    tree_dict[st.label()] = input_chunked
        return tree_dict





    def form_questions(self,candidates):
        """Ques formation
        - Args:
            df(pandas.dataframe): dataframe of df[['Question', 'Answer', 'Sentence','Prediction']]
        - Returns:
            question_answers(pandas.dataframe): Full_qus, Question, Answer, Prediction, Sentence
            """

        candidates = pd.DataFrame(candidates)
        deepqf = Actual_Question_Formation()

        #print("From Ques formatrion")

        candidates1 = []
        df = {}
        for index, candidate in candidates.iterrows():
            # print "candidate : "
            # print candidate
            # print candidate['Answer']
            # sentence_copy = candidate['Question']

            tokens = nltk.word_tokenize(str(candidate['Sentence']))
            tagged = nltk.pos_tag(tokens)
            ne_chunk = nltk.ne_chunk(tagged)
            #print('ne chunk: \n')
            #print(ne_chunk)

            chunk_dict = self.tree_to_dict(ne_chunk)
            #print(chunk_dict)

            full_ques, ans, flag = deepqf.form_full_questions(candidate,chunk_dict,tagged)
            print ("full_ques is " )
            print (full_ques)


            if flag == 1:
                df['Full_qus'] = full_ques[0]
                if ans == 0:
                    df['Answer'] = candidate['Answer']
                else:
                    df['Answer'] = ans

            # if str(outputformat) == "blanks":
            #     # if flag == 0:
            #     df['Full_qus'] = candidate['Question']
            #     if ans == 0:
            #         df['Answer'] = candidate['Answer']
            #     else:
            #         df['Answer'] = ans
            #
            # if str(outputformat) == "both":
            #     df['Full_qus'] = full_ques[0]
            #     if ans == 0:
            #         df['Answer'] = candidate['Answer']
            #     else:
            #         df['Answer'] = ans

            # df['Question'] = candidate['Question']

            # df['Prediction'] = candidate['Prediction']
            # df['Sentence'] = candidate['Sentence']
            # df['flag'] = flag
            if len(df.items()) != 0:
                candidates1.append(df)
            df = {}
            #print (" ")
        #print ("new final output :")
        #for df in candidates1:
            #print(df)
            #print('-----------------')
        return candidates1


