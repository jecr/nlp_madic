import re

while True:
	try:
		f = raw_input("File route:")
		myFile = open(f, 'r')
		break
	except IOError:
		print "File not found, try again ;D"

of = open(f+'_output', 'w')


laLinea = 0
x = 0
urls = []
twitpics = []
hashtags = []
users = []
tempCont = []

for line in myFile:
	laLinea = line.split('\t')
	if line.find('tweet_id') < 0:
		
		tweet = laLinea[len(laLinea)-1]
		tweet = tweet.replace( '\n', '')
		tweet = tweet.replace( '\r', '')
		
		if tweet:

			urls = re.findall( 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet )
			twitpics = re.findall( '(?:pic.twitter)[^"\' ]+', tweet )
			hashtags = re.findall( '(?:#)[^"\' ]+', tweet )
			users = re.findall( '(?:@)[^"\' ]+', tweet )
			
			if len(urls) > 0:
				for x in range( len(urls) ):
					tweet = tweet.replace( urls[x], '')
			urls = []
			if len(twitpics) > 0:
				for x in range( len(twitpics) ):
					tweet = tweet.replace( twitpics[x], '')
			twitpics = []
			if len(hashtags) > 0:
				for x in range( len(hashtags) ):
					tweet = tweet.replace( hashtags[x], '')
			hashtags = []
			if len(users) > 0:
				for x in range( len(users) ):
					tweet = tweet.replace( users[x], '')
			users = []

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
				of.write(tweet.lower()+'\n')