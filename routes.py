from flask import Flask,jsonify
import json
from twython import Twython, TwythonError

consumer_key = "RHuv5VHWqMEtd0vThJAlAwdQU"
consumer_secret = "cCmcuxFQ0lGENvuOzCTKQa51rpnQdJbI281RwxMoVsj2PSAL9R"

access_token_key = "2684988325-L9XobRukSFR29mthcZVPEqEw5Bm0YyohMotzedq"
access_token_secret = "pBxT3rPk1fUqaXDtzZopd3olqqd4NEUF9C4QpCOQs9prW"


# Requires Authentication as of Twitter API v1.1
twitter = Twython(consumer_key, consumer_secret,access_token_key, access_token_secret)
username = 'timberners_lee'

app = Flask(__name__)


@app.route("/")
def home():
	return app.send_static_file('home.html')

@app.route("/timeline")
def timeline():	
	try:
		twitter.show_user(screen_name=username)
		print twitter.show_user(screen_name=username)
	except TwythonError as e:
	    print e

	return jsonify(**twitter.show_user(screen_name=username))



@app.route("/tweets")
def tweets():	
	try:
		twitter.show_user(screen_name=username)
	except TwythonError as e:
	    print e

	user_tweets = twitter.get_user_timeline(screen_name='mikehelmick', include_rts=True)
	tweetsObject = {}
	tweetsArray = []
	i = 0
	for tweet in user_tweets:
		tweet['text'] = Twython.html_for_tweet(tweet)
		tweetsArray.append(tweet['text'])
		tweetsObject[i] = tweet['text']
		i += 1
	tweet_obj = {'tweet_array': tweetsArray}
	tweetsObject = json.dumps(tweetsObject)
	return tweetsObject


if __name__ == "__main__":
	app.run(debug = True)
