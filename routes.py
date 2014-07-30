from flask import Flask,jsonify
import json
from twython import Twython, TwythonError

consumer_key = "RHuv5VHWqMEtd0vThJAlAwdQU"
consumer_secret = "cCmcuxFQ0lGENvuOzCTKQa51rpnQdJbI281RwxMoVsj2PSAL9R"

access_token_key = "2684988325-L9XobRukSFR29mthcZVPEqEw5Bm0YyohMotzedq"
access_token_secret = "pBxT3rPk1fUqaXDtzZopd3olqqd4NEUF9C4QpCOQs9prW"

# Requires Authentication as of Twitter API v1.1
twitter = Twython(consumer_key, consumer_secret,access_token_key, access_token_secret)


app = Flask(__name__)


@app.route("/")
def home():
	return app.send_static_file('home.html')

@app.route("/timeline")
def timeline():	
	try:
	    user_timeline = twitter.get_user_timeline(screen_name='timberners_lee')
	except TwythonError as e:
	    print e

	return jsonify(**twitter.show_user(screen_name='timberners_lee'))


@app.route("/tweets")
def tweets():	
	try:
		tweets = get_home_timeline(screen_name='timberners_lee')
	except TwythonError as e:
   		print e

	return jsonify(**get_home_timeline(screen_name='timberners_lee'))


if __name__ == "__main__":
	app.run()
