import nltk
import math
import string
import operator
import codecs
from collections import defaultdict, OrderedDict


class SentenceSelection:
    """Select topically import sentences from given document"""
    def __init__(self):
        self.ratio = 1
        # self.ratio = 0.05

    def _load_sentences(self, file_name):
        """Load sentences from given document
        Args:
                file_name: document name to read
        Return:
                sentences: sentences read from given document
        """
        with codecs.open(file_name , 'r' , encoding='utf-8') as file:
            text = file.read()
        return text

    def _load_sentences_text(self, input_text):
        """same function as above
           just instead of document it will consider text string as input
        """
        return input_text


    def _clean_sentences(self, sentences):
        """Clean sentences, remove digit, punctuation, upper case to lower
        Args:
                sentences: sentences to be cleaned
        Return:
                sentences_processed: dict of cleaned sentences
        """
        flag = 0
        sentence_processed = {}

        #sentences = sentences.decode('utf-8')

        punc = set(string.punctuation)
        punc.remove('.')
        sentences = ''.join([x for x in sentences if not x.isdigit()])
        sentences = ''.join([x for x in sentences if x not in punc])
        sentences = ''.join([x.lower() for x in sentences])
        sentences = ' '.join(sentences.split())

        stop_words = nltk.corpus.stopwords.words('english')
        stemmer = nltk.stem.PorterStemmer()
        tokenize = nltk.word_tokenize

        for sentence in sentences.split('.'):
            sentence = sentence.strip()
            sentence = [stemmer.stem(word) for word in tokenize(
                sentence) if not word in stop_words]
            if sentence:
                sentence_processed[flag] = sentence
                flag += 1

        return sentence_processed

    def _word_distribution(self, sentence_processed):
        """Compute word probabilistic distribution
        """
        word_distr = defaultdict(int)
        word_count = 0.0
        for k in sentence_processed:
            for word in sentence_processed[k]:
                word_distr[word] += 1
                word_count += 1

        for word in word_distr:
            word_distr[word] = word_distr[word] / word_count

        return word_distr

    def _sentence_weight(self, word_distribution, sentence_processed):
        """Compute weight with respect to sentences
        Args:
                word_distribution: probabilistic distribution of terms in document
                sentence_processed: dict of processed sentences generated by clean_sentences
        Return:
                sentence_weight: dict of weight of each sentence
        """
        sentence_weight = {}

        for sentence_id in sentence_processed:
            for word in sentence_processed[sentence_id]:

                if word_distribution[word] and sentence_id in sentence_weight:
                    sentence_weight[sentence_id] += word_distribution[word]
                else:
                    sentence_weight[sentence_id] = word_distribution[word]

            sentence_weight[sentence_id] = sentence_weight[
                sentence_id] / float(len(sentence_processed[sentence_id]))

        sentence_weight = sorted(sentence_weight.items(
        ), key=operator.itemgetter(1), reverse=True)
        return sentence_weight

    def _topically_important_sentence(self, sentence_weight, sentences):
        """Select topically import sentences
        Args:
                sentence_weight: dict, weight of sentences computed in sentence_weight
                sentences: set of sentences
        Return:
                sentences_selected: dict, topically important sentences selected
        """
        sentence_length = len(sentence_weight)
        # how many sentences to retain
        num_sentences_selected = math.ceil(float(self.ratio) * sentence_length)
        num_sentences_selected = int(num_sentences_selected)
        # key of selected sentences
        sentences_selected_key = []
        # dictionary of all sentences
        sentences_dict = {}
        flag = 0
        for k, v in sentence_weight[0:num_sentences_selected]:
            sentences_selected_key.append(k)

        for sentence in sentences.split('.'):
            if sentence:
                sentences_dict[flag] = sentence
                flag += 1
        sentences_selected = OrderedDict()

        for key in sentences_selected_key:
            sentences_selected[key] = sentences_dict[key]

        return sentences_selected

    def prepare_sentences(self, file_name):
        """Prepare sentences to be parsed
        Args:
            file_names(str): string of file names
        Returns:
            important_sentences(OrderedDict): OrderedDict of important sentences
            position:sentence, ordered by importance
        """
        print('Preparing Sentences ')
        sentences = self._load_sentences(file_name)

        sentences_cleaned = self._clean_sentences(sentences)

        distribution = self._word_distribution(sentences_cleaned)

        sentence_weight = self._sentence_weight(
            distribution, sentences_cleaned)

        important_sentences = self._topically_important_sentence(
            sentence_weight, sentences)
        return important_sentences


    def prepare_sentences_from_rawtext(self,input_text):
        """
        Same function as above just with the input format changed
        Args:
            input_text(str): raw text
        Returns:
            important_sentences(OrderedDict): OrderedDict of important sentences
            position:sentence, ordered by importance
        """
        sentences = self._load_sentences_text(input_text)

        sentences_cleaned = self._clean_sentences(sentences)

        distribution = self._word_distribution(sentences_cleaned)

        sentence_weight = self._sentence_weight(
            distribution, sentences_cleaned)

        important_sentences = self._topically_important_sentence(
            sentence_weight, sentences)
        return important_sentences
