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
twitpics = []
hashtags = []
users = []

for line in myFile:
	cosa = line.split('\t')
	if line.find('tweet_id') < 0:
		if cosa[13]:
			cosa[13] = cosa[13].replace( '\n', '')
			urls = re.findall( 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cosa[13] )
			twitpics = re.findall( '(?:pic.twitter)[^"\' ]+', cosa[13] )
			hashtags = re.findall( '(?:#)[^"\' ]+', cosa[13] )
			users = re.findall( '(?:@)[^"\' ]+', cosa[13] )
			if len(urls) > 0:
				for x in range( len(urls) ):
					cosa[13] = cosa[13].replace( urls[x], '[url]')
			urls = []
			if len(twitpics) > 0:
				for x in range( len(twitpics) ):
					cosa[13] = cosa[13].replace( twitpics[x], '[url]')
			twitpics = []
			if len(hashtags) > 0:
				for x in range( len(hashtags) ):
					cosa[13] = cosa[13].replace( hashtags[x], '[hashtag]')
			hashtags = []
			if len(users) > 0:
				for x in range( len(users) ):
					cosa[13] = cosa[13].replace( users[x], '[user]')
			users = []
			of.write(cosa[13].lower()+'\n')