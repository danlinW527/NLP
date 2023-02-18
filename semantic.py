print('example 1: md example')
import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp('fried rice')
word2 = nlp('fried noodles')
word3 = nlp('udon noodles')

print(f'{word1} and {word2} similarity is {word1.similarity(word2)}')
print(f'{word3} and {word2} similarity is {word3.similarity(word2)}')
print(f'{word3} and {word1} similarity is {word3.similarity(word1)}')

nlp = spacy.load('en_core_web_sm')
word1 = nlp('fried rice')
word2 = nlp('fried noodles')
word3 = nlp('udon noodles')

print(f'{word1} and {word2} similarity is {word1.similarity(word2)}')
print(f'{word3} and {word2} similarity is {word3.similarity(word2)}')
print(f'{word3} and {word1} similarity is {word3.similarity(word1)}')

#when running both mode, the results from sm mode is lower
#also it has the warming sign which says the mode you are using has no word vectors loaded,
# so the result of the doc.similarity method will be based on the tagger, parser and NER,
# which may not give userful simimlarity jundgements. This may happen if you're using one of the small models
# which don't ship with word vectors and only use context-sensitive tensors.
# You can always add your own word vectors, or use one of the larger models instead if available.
