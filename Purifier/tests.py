# -*- coding: UTF-8 -*-
import re
import os

# while True:
# 	try:
# 		f = raw_input("File route:")
# 		myFile = open(f, 'r')
# 		break
# 	except IOError:
# 		print "File not found, try again ;D"
#openedFile = open(f+'_output', 'w')

ruta = raw_input("Give me a path to follow ~(ºoº)~:")

def cleanse():
	laLinea = 0
	x = 0
	removeMe = []
	tempCont = []

	for line in myFile:
		laLinea = line.split('\t')
		if line.find('tweet_id') < 0:
			
			tweet = laLinea[len(laLinea)-1]
			tweet = tweet.replace( '\n', '')
			tweet = tweet.replace( '\r', '')
			
			if tweet:
				
				removeMe = re.findall( 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet )
				if len(removeMe) > 0:
					for x in range( len(removeMe) ):
						tweet = tweet.replace( removeMe[x], '')
				removeMe = []

				removeMe = re.findall( '(?:pic.twitter)[^"\' ]+', tweet )
				if len(removeMe) > 0:
					for x in range( len(removeMe) ):
						tweet = tweet.replace( removeMe[x], '')
				removeMe = []

				removeMe = re.findall( '(?:#)[^"\' ]+', tweet )
				if len(removeMe) > 0:
					for x in range( len(removeMe) ):
						tweet = tweet.replace( removeMe[x], '')
				removeMe = []

				removeMe = re.findall( '(?:@)[^"\' ]+', tweet )
				if len(removeMe) > 0:
					for x in range( len(removeMe) ):
						tweet = tweet.replace( removeMe[x], '')
				removeMe = []

				tweet = ''.join(c for c in tweet if c.isalnum() or c == ' ')

				laLinea = tweet.split(' ')
				for palabra in laLinea:
					if  palabra.isalpha() != True:
						palabra = ''
					if palabra != ' ':
						tempCont.append(palabra)

				tweet = ' '.join( tempCont )
				tweet = ' '.join( tweet.split() )
				tempCont = []

				if tweet != '':
					openedFile.write(tweet.lower()+'\n')
	return