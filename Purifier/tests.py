# -*- coding: UTF-8 -*-
import re
import os
import glob
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

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
combined = [''] * 4

# Primer array combinado, todos los tuits con su ID
theFirst = []

# Lista de entidades
entities = []

# =========================================================================================================
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
		# Si encuentra el texto tweet_id, ignora el renglón
		if line.find('tweet_id') < 0 and len(laLinea) > 10:
			# Si el tweet está en inglés
			if laLinea[4] == 'EN':
				# Asigna el tuit para su purificación			
				tweet = laLinea[len(laLinea)-1]

				# Asigna el ID
				elID = laLinea[0]

				# Asigna la entidad
				entity = laLinea[2]

				#if entity not in entities:
				#	entities.append(entity)

				#entities.sort()

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
						
						# Extiende el tuit, lo asigna inmediatamente :3 like a bauss
						combined[1] = splitter( thein )

						# Le agrega el número de entidad de acuerdo al arreglo de entidades
						combined[2] = entity

						while True:
							try:
								goldStand = open('goldstandard.dat', 'r')
								break
							except IOError:
								print "goldstandard.dat not found"

						for asd in goldStand:
							if elID in asd:
								asd = asd.replace('"','')
								asd = asd.replace('\n','')
								asd = asd.split('\t')
								asd[2] = ''.join(c for c in asd[2] if c.isalnum() or c == ' ')
								asd[2] = ' '.join( asd[2].split() )
								asd[2] = asd[2].lower()
								combined[3] = asd[2]

						# Va metiendo en theFirst TODOS los arreglos [ ID ][ Tuit ]
						theFirst.append( combined )
						
						openedFile.write( combined[2] + ' ' + combined[3] + ' ' + combined[0] + ' ' + combined[1] + '\n' )

		# Vacía el arreglo para volverlo a usar, vivan las 3 Rs
		combined = []
		combined = [''] * 4

	return

# =========================================================================================================

while True:
	try:
		goldStand = open('goldstandard.dat', 'r')
		break
	except IOError:
		print "goldstandard.dat not found"

golden1 = []
golden2 = [''] * 61

for linea in goldStand:
	if linea.find('tweet_id') < 0:
		linea = linea.replace( '\n', '')
		linea = linea.replace( '"', '')
		goldie = linea.split('\t')
		
		if goldie[0] not in golden1:
			golden1.append( goldie[0] )

		if goldie[0] in golden1:
			golden2[ golden1.index( goldie[0] ) ] += '\t' + goldie[2]
# La lista golden1 contiene las entidades en orden?

# temas = open('lista_temas', 'w')
for item in golden2:
	linesplit = item.split('\t')
	tempo = []
	for algo in linesplit:
		algo = ''.join(c for c in algo if c.isalnum() or c == ' ')
		algo = ' '.join( algo.split() )
		algo = algo.lower()
		if  algo not in tempo and algo != '':
			tempo.append(algo)

	golden2[ golden2.index(item) ] = sorted(tempo)
# La lista golden2 contiene en orden de entidades los temas

# Declaración del archivo donde van TODOS los tuits
openedFile = open('all_tuits', 'w')

for filename in glob.glob(os.path.join(ruta, '*.2')):
	# Ejecuta la limpieza
	cleanse(filename)

print '\nLimpieza terminada \n\nTuits guardados en "all_tuits"'

#Abre el archivo lista de entidades y lo convierte en un arreglo
while True:
	try:
		enti = open('lista_entidades', 'r')
		break
	except IOError:
		print "lista_entidades is missing\n"

for e in enti:
	e = e.replace('\n','')
	entities.append(e)

# Guarda los tuits en archivos individuales
seGuardan = raw_input('\nQuieres que se guarden los tuits en archivos individuales? [Y/N]: ').lower()
if seGuardan == 'y':
	newpath = r'Output' 
	if not os.path.exists(newpath): os.makedirs(newpath)

	whereAmI = 0;

	for oneTweet in theFirst:
		# Esto es sólo para mostrar el porcentaje de avance
		perc = round( 100 * ( float(theFirst.index(oneTweet)) / float(len(theFirst)) ) )
		if perc != whereAmI:
			whereAmI = perc
			print str( whereAmI ) + '%'
		
		# Para cada entidad dentro de entities, crea una carpeta con su index
		for someEntity in entities:
			newpath = r'Output/ENT' + str( entities.index( someEntity ) )
			if not os.path.exists(newpath): os.makedirs(newpath)

			# Si la entidad del tuit  coincide con la entidad actual
			if someEntity == oneTweet[2]:

				#el indice de la identidad del tuit en entities es la posición en la que hay que buscar dentro de golden2 la similitud de termino
				#crear carpeta con ese termino y meter dentro el tuit

				for tema in golden2[ entities.index( oneTweet[2] ) ]:
					
					if tema == oneTweet[3]:
						newpath = r'Output/ENT' + str( entities.index( someEntity ) ) + '/' + 'TEM'+ str(golden2[ entities.index( oneTweet[2] ) ].index( tema ))
						if not os.path.exists(newpath): os.makedirs(newpath)
						
						tweetFile = open( 'Output/ENT' + str( entities.index( someEntity ) ) + '/' + 'TEM'+ str(golden2[ entities.index( oneTweet[2] ) ].index( tema )) + '/' + str( oneTweet[0] ) + '.txt', 'w' )
						tweetFile.write( oneTweet[1] )