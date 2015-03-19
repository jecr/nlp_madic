while True:
	try:
		f = raw_input("File route:")
		myFile = open(f, 'r')
		break
	except IOError:
		print "File not found, try again ;D"

of = open(f+'_output', 'w')


cosa = 0
x = 0
for line in myFile:
	cosa = line.split('\t')
	if line.find('tweet_id') < 0:
		if cosa[13] != '\n' or cosa[13] != ' ' or cosa[13] != '\t' or cosa[13] != None:
			if cosa[13].find('http') > 0:
				print(cosa[13].index('http'))
				x = cosa[13].index('http')
				while x < len(cosa[13])-1:
					x += 1
				print cosa[13].index('http') + cosa[13][x]
				x = 0
			of.write(cosa[13].lower())