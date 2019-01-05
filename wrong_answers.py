import nltk
from nltk.corpus import wordnet


class Answer:
	def __init__(self, text, similarity):
		self.text = text
		self.similarity = similarity


def _get_parents(synset):
	"""
	Returns one of the parents of the synset.
	:param synset: The synset to obtain the parent from
	:return: One of the parents of the synset
	"""

	return synset.hypernyms()


def _get_all_siblings(synset):
	"""
	Returns up to five siblings of the synset.
	:param synset: The synset to obtain the siblings from
	:return: The siblings obtained from the synset
	"""

	siblings = []
	sibling_count = 0
	parents = _get_parents(synset)

	for parent in parents:
		for sibling in parent.hyponyms():
			if sibling != synset:
				siblings.insert(sibling_count, sibling)
				sibling_count += 1

	return siblings


def _get_possible_replacements(nouns, i, constructed, rep):
	if i == len(nouns):
		rep.append(constructed.copy())
		return

	for word in nouns[i]:
		constructed.append(word)
		_get_possible_replacements(nouns, i+1, constructed, rep)
		constructed.pop()


def get_wrong_answers(answer_sentence):
	tokens = nltk.word_tokenize(answer_sentence)
	tagged = nltk.pos_tag(tokens)

	wrong_answers = []
	nouns = []

	for word in tagged:
		if word[1] == 'NN':
			tmp = []
			tmp.append(word[0])
			synset = wordnet.synsets(word[0])[0]
			distractors = _get_all_siblings(synset)

			for distractor in distractors:
				tmp.append(distractor.lemma_names()[0].replace('_', ' '))

			nouns.append(tmp)

	rep = []
	constructed = []
	_get_possible_replacements(nouns, 0, constructed, rep)

	for r in rep:
		wrong_answer = answer_sentence
		score = 0
		for i in range(len(nouns)):
			wrong_answer = wrong_answer.replace(nouns[i][0], r[i])
			score += wordnet.wup_similarity(wordnet.synsets(nouns[i][0])[0], wordnet.synsets(r[i].replace(' ', '_'))[0])
		wrong_answers.append(Answer(wrong_answer, score))

	ret = sorted(wrong_answers.copy(), key=lambda x: x.similarity, reverse=True)
	ret = [wrong.text for wrong in wrong_answers]

	wrong_answers = []
	for i in ret:
		if len(wrong_answers) == 0:
			wrong_answers.append(i)
		elif i != wrong_answers[len(wrong_answers) - 1]:
			wrong_answers.append(i)

	return wrong_answers


# print(get_wrong_answers('the big brown fox'))
