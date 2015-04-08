# -*- coding: UTF-8 -*-
import nltk
from nltk.corpus import wordnet as wn

def runner( palabra1, palabra2 ):
	terminos1 = []
	terminos2 = []
	
	for algo in wn.synsets( palabra1 ):
		terminos1.append( str(algo.name()) )


	for algo in wn.synsets( palabra2 ):
		terminos2.append( str(algo.name()) )

	score = 0
	ganador = ''
	for sent1 in terminos1:
		sent1 = wn.synset(sent1)
		for sent2 in terminos2:
			sent2 = wn.synset(sent2)
			hyperonimo = sent1.lowest_common_hypernyms( sent2 )
			if hyperonimo != []:
				hyperonimo = str(hyperonimo[0].name())

				points = wn.synset( hyperonimo ).min_depth()
				if points > score:
					score = points
					ganador = hyperonimo
	ganador = ganador.split('.')
	ganador = ganador[0]
	ganador = ganador.replace('_',' ')
	return ganador

sentence = raw_input("Give me a sentence (English only): ")

sentence = sentence.split()

newSentence = []

for word in sentence:
	newSentence.append( word )
	if sentence.index(word) + 1 < len(sentence):
		expanded = runner( word, sentence[ sentence.index(word) + 1 ] )
		newSentence.append( expanded )

newSentence = ' '.join( newSentence )
newSentence = ' '.join( newSentence.split() )

print newSentence