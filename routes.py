from flask import Flask,jsonify,render_template,Markup
import json
from twython import Twython, TwythonError

consumer_key = "RHuv5VHWqMEtd0vThJAlAwdQU"
consumer_secret = "cCmcuxFQ0lGENvuOzCTKQa51rpnQdJbI281RwxMoVsj2PSAL9R"

access_token_key = "2684988325-L9XobRukSFR29mthcZVPEqEw5Bm0YyohMotzedq"
access_token_secret = "pBxT3rPk1fUqaXDtzZopd3olqqd4NEUF9C4QpCOQs9prW"


# Requires Authentication as of Twitter API v1.1
twitter = Twython(consumer_key, consumer_secret,access_token_key, access_token_secret)
username = 'timberners_lee'
#username = 'BBCBreaking'
#username = 'drskovatereza'

app = Flask(__name__)


@app.route("/")
def home():
	this_body = render_template('partial1.html')
	return render_template('index.html', title = 'Tereza Drskova', body =  Markup(this_body))

@app.route("/view2")
def otherView():
	this_body = render_template('partial2.html')
	return render_template('index.html', title = 'This Author', body = Markup(this_body))

@app.route("/timeline")
def timeline():	
	try:
		twitter.show_user(screen_name=username)
	except TwythonError as e:
	    print e

	return jsonify(**twitter.show_user(screen_name=username))



@app.route("/tweets")
def tweets():	
	try:
		userTweets = twitter.get_user_timeline(screen_name=username, include_rts=False)
		tweetsArray = []

		for tweet in userTweets:
			tweet['text'] = Twython.html_for_tweet(tweet)
			tweetsArray.append(tweet['text'])
		tweetObj = {'tweet_array': tweetsArray}
	except TwythonError as e:
	    print e
	
	return jsonify(**tweetObj)


if __name__ == "__main__":
	app.run(debug = True)
