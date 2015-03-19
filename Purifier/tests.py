import re

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
urls = []
for line in myFile:
	cosa = line.split('\t')
	if line.find('tweet_id') < 0:
		if cosa[13] != '\n' or cosa[13] != ' ' or cosa[13] != '\t' or cosa[13] != None:
			if cosa[13].find('http') > 0:
				urls.append( re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cosa[13]) )
				if len(urls) > 0:
					for x in range( len(urls) ):
						cosa[13] = cosa[13].replace( urls[x][0] ,'[url]')
				urls = []
			of.write(cosa[13].lower())