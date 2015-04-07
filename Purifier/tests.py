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
						# Almacena el tweet en lowercase en la segunda posición de combined
						combined[1] = tweet.lower()

						# Le agrega el número de entidad de acuerdo al arreglo de entidades
						combined[2] = entity

						# Va metiendo en theFirst TODOS los arreglos [ ID ][ Tuit ]
						theFirst.append( combined )
						
						openedFile.write( combined[2] + ' ' + combined[0] + ' ' + combined[1] + '\n' )

		# Vacía el arreglo para volverlo a usar, vivan las 3 Rs
		combined = []
		combined = [0] * 4

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
golden3 = [0] * 61

for linea in goldStand:
	if linea.find('tweet_id') < 0:
		linea = linea.replace( '\n', '')
		linea = linea.replace( '"', '')
		goldie = linea.split('\t')
		
		if goldie[0] not in golden1:
			golden1.append( goldie[0] )

		if goldie[0] in golden1:
			golden2[ golden1.index( goldie[0] ) ] += '\t' + goldie[2]


temas = open('lista_temas', 'w')
for item in golden2:
	linesplit = item.split('\t')
	tempo = []	
	for algo in linesplit:
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
		perc = round( 100 * ( float(theFirst.index(oneTweet)) / float(len(theFirst)) ) )
		if perc != whereAmI:
			whereAmI = perc
			print str( whereAmI ) + '%'
		
		# Para cada entidad dentro de entities, crea una carpeta con su index
		for someEntity in entities:
			newpath = r'Output/ENT' + str( entities.index( someEntity ) )
			if not os.path.exists(newpath): os.makedirs(newpath)
			if someEntity == oneTweet[2]:

				tweetFile = open( 'Output/ENT' + str( entities.index( someEntity ) ) + '/' + str( oneTweet[0] ) + '.txt', 'w' )
				tweetFile.write( oneTweet[1] )