# -*- coding: UTF-8 -*-
import re
import os
import glob

# while True:
# 	try:
# 		f = raw_input("File route:")
# 		myFile = open(f, 'r')
# 		break
# 	except IOError:
# 		print "File not found, try again ;D"
#openedFile = open(f+'_output', 'w')

ruta = raw_input("Give me a path to follow ~(ºoº)~:")

# Aquí van a ir el tweet y su ID (sólo uno)
combined = [0] * 3

# Primer array combinado, todos los tuits con su ID
theFirst = []

# Lista de entidades
entities = []

def cleanse( theFileName ):

	while True:
		try:
			myFile = open(theFileName, 'r')
			break
		except IOError:
			print "File not found, try again ;D"

	laLinea = 0
	x = 0
	removeMe = []
	tempCont = []
	elID = []
	entity = []

	for line in myFile:
		laLinea = line.split('\t')
		if line.find('tweet_id') < 0 and len(laLinea) > 10:
			
			# Asigna el tuit para su purificación			
			tweet = laLinea[len(laLinea)-1]

			# Asigna el ID
			elID = laLinea[0]

			# Asigna la entidad
			entity = laLinea[2]

			if entity not in entities:
				entities.append(entity)

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
					# Almacena el ID en la primer posición de combined
					combined[0] = elID
					# Almacena el tweet en lowercase en la segunda posición de combined
					combined[1] = tweet.lower()

					# Le agrega el número de entidad de acuerdo al arreglo de entidades
					combined[2] = entities.index(entity)

					# Va metiendo en theFirst TODOS los arreglos [ ID ][ Tuit ]
					theFirst.append( combined )
					
					openedFile.write( str(combined[2]) + ' ' + combined[0] + ' ' + combined[1] + '\n' )

		# Vacía el arreglo para volverlo a usar, vivan las 3 Rs
		combined = []
		combined = [0] * 3

	return

openedFile = open('stuff'+'_output', 'w')

for filename in glob.glob(os.path.join(ruta, '*.2')):
	print filename
	cleanse(filename)

print len( entities )