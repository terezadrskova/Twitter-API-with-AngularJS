from flask import Flask,jsonify
import json


app = Flask(__name__)

"""
@menus.route('/get', methods=["PUT", "POST"])
def new():
    return jsonify(request.get_json(force=True))
"""

@app.route("/")
def home():
	return app.send_static_file('home.html')

@app.route("/twitter/tweepy")
def twitter():
	from twython import Twython, TwythonError

	consumer_key = "RHuv5VHWqMEtd0vThJAlAwdQU"
	consumer_secret = "cCmcuxFQ0lGENvuOzCTKQa51rpnQdJbI281RwxMoVsj2PSAL9R"

	access_token_key = "2684988325-L9XobRukSFR29mthcZVPEqEw5Bm0YyohMotzedq"
	access_token_secret = "pBxT3rPk1fUqaXDtzZopd3olqqd4NEUF9C4QpCOQs9prW"


	# Requires Authentication as of Twitter API v1.1
	twitter = Twython(consumer_key, consumer_secret,access_token_key, access_token_secret)
	try:
	    user_timeline = twitter.get_user_timeline(screen_name='timberners_lee')
	except TwythonError as e:
	    print e


	#twitterans = twitter.search(q='twitter', result_type='popular')
	#print twitterans

	#print user_timeline

	return jsonify(**twitter.show_user(screen_name='drskovatereza'))
	

if __name__ == "__main__":
	app.run()
