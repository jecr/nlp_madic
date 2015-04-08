# -*- coding: UTF-8 -*-
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

def runner( palabra1 ):
	terminos1 = []
	sign = wn.synsets(palabra1)

	firstOne = sign[0].name()

	print firstOne

	print wn.synset( 'cat' ).lemma_names

	#lpal = ' '.join( lpal )
	#lpal = ' '.join( lpal.split() )

	return 'pato'

sentence = raw_input("Give me a sentence (English only): ")

sentence = sentence.split()

sentence = [w for w in sentence if not w in stopwords.words('english')]

newSentence = []

for word in sentence:
	newSentence.append( word )
	expanded = runner( word )
	newSentence.append( expanded )

newSentence = ' '.join( newSentence )
newSentence = ' '.join( newSentence.split() )

print newSentence