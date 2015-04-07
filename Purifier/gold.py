# -*- coding: UTF-8 -*-
import re
import os
import glob

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