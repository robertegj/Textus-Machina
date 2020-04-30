# primary infrastructure, web worker
from flask import Flask, request, jsonify, send_from_directory, render_template
# flask extenders
import logging
from flask_cors import CORS
import json
# text analytics
import logic as l

app = Flask(__name__,static_url_path='/static/')
logging.basicConfig(filename="server.log", 
level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
CORS(app)

@app.route('/', methods = ['GET','POST'])
def home():
	try:
		return render_template('home.htm')
	except Exception as err:
		log(err)
		return err

@app.route('/widget', methods = ['GET','POST'])
def widget():
	try:
		return render_template('widget.html')
	except Exception as err:
		app.logger.info(err)
		return err

@app.route('/api', methods = ['GET','POST'])
def apiRoute():
	try:
		if request:
			app.logger.info(request)
		command = request.args.get('command')
		text = request.args.get('text')
		if (command =="getCommands"):
			commands = {}
			for each in dir(l):
				if (each.startswith("get")):
					commands.update({each:"generic description"})
			return '''{}'''.format(commands)
		if (command=="getSentiment"):
			app.logger.info(text)
			return '''{}'''.format(l.getSentiment(text))
		if (command=="getSentimentScore"):
			app.logger.info(text)
			return '''{}'''.format(l.getSentimentScore(text))
		if (command=="getEntities"):
			app.logger.info(text)
			return '''{}'''.format(l.getEntities(text))
		if (command=="getNouns"):
			app.logger.info(text)
			return '''{}'''.format(l.getNouns(text))
		if (command=="getCompound"):
			app.logger.info(text)
			return '''{}'''.format(l.getCompound(text))
		else:
			return "No known command sent!"
	except Exception as err:
		app.logger.error(err)
		return err

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

app.logger.info('EOF REACHED')