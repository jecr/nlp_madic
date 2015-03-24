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
					tweet = tweet.replace( urls[x], '[url]')
			urls = []
			if len(twitpics) > 0:
				for x in range( len(twitpics) ):
					tweet = tweet.replace( twitpics[x], '[url]')
			twitpics = []
			if len(hashtags) > 0:
				for x in range( len(hashtags) ):
					tweet = tweet.replace( hashtags[x], '[hashtag]')
			hashtags = []
			if len(users) > 0:
				for x in range( len(users) ):
					tweet = tweet.replace( users[x], '[user]')
			users = []
			of.write(tweet.lower()+'\n')