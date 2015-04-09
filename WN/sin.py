# -*- coding: UTF-8 -*-
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

def runner( palabra1 ):

	# sinon =  wn.synsets( palabra1 )[0].lemma_names()

	sinons = []

	for x in wn.synsets( palabra1 ):
		for y in x.lemma_names():
			if y not in sinons:
				sinons.append( y )

	sinons = ' '.join( sinons )

	sinons = ' '.join( sinons.split() )

	return sinons

def splitter( sentence ):
	sentence = sentence.split()

	sentence = [w for w in sentence if not w in stopwords.words('english')]

	newSentence = []

	for word in sentence:
		
		expanded = runner( word )
		
		if expanded == '':
			newSentence.append( word )
		else:
			newSentence.append( expanded )

	newSentence = ' '.join( newSentence )
	newSentence = ' '.join( newSentence.split() )

	return newSentence

thein = raw_input("Give me a word: ")

print splitter( thein )
