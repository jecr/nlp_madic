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
combined = [0] * 4

# Primer array combinado, todos los tuits con su ID
theFirst = []

# Lista de entidades
entities = []

# =========================================================================================================

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
						combined[2] = str( entities.index(entity) )

						# Va metiendo en theFirst TODOS los arreglos [ ID ][ Tuit ]
						theFirst.append( combined )
						
						openedFile.write( combined[2] + ' ' + combined[0] + ' ' + combined[1] + '\n' )

		# Vacía el arreglo para volverlo a usar, vivan las 3 Rs
		combined = []
		combined = [0] * 4

	return

# =========================================================================================================

# Declaración del archivo donde van TODOS los tuits
openedFile = open('all_tuits', 'w')

for filename in glob.glob(os.path.join(ruta, '*.2')):
	# Ejecuta la limpieza
	cleanse(filename)

print '\nLimpieza terminada \n\nTuits guardados en "all_tuits"'

# Guarda las entidades en un archivo aparte, para referencia
entitiesList = open('lista_entidades', 'w')

for laentidad in entities:
	entitiesList.write( str( entities.index( laentidad ) ) + ' ' + laentidad + '\n' )
print '\nEntidades guardadas en "lista_entidades"'

# Guarda los tuits en archivos individuales
seGuardan = raw_input('\nQuieres que se guarden los tuits en archivos individuales? [Y/N]: ').lower()
if seGuardan == 'y':
	newpath = r'Output' 
	if not os.path.exists(newpath): os.makedirs(newpath)

	whereAmI = 0;

	for oneTweet in theFirst:
		perc = round( 100 * ( float(theFirst.index(oneTweet)) / float(len(theFirst)) ) )
		if perc != whereAmI:
			whereAmI = perc
			print str( whereAmI ) + '%'
		
		for someEntity in entities:
			newpath = r'Output/ENT' + str( entities.index( someEntity ) )
			if not os.path.exists(newpath): os.makedirs(newpath)
			if entities.index(someEntity) == int( oneTweet[2] ):

				tweetFile = open( 'Output/ENT' + str( entities.index( someEntity ) ) + '/' + str( oneTweet[0] ) + '.txt', 'w' )
				tweetFile.write( oneTweet[1] )