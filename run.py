import flask
from flask import Flask, url_for, request, render_template, redirect
import serial
import time
from flask_socketio import SocketIO
import json
from directkeys import PressKey, ReleaseKey


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event')
def handle_message(message):
	if type(message) is dict:
		for k, v in message.items():
			if k == 'PRESSKEY':
				#print(v)
				PressKey(int(v))

			if k == 'RELEASEKEY': 
				#print(v)
				ReleaseKey(int(v))

	# message = json.dumps(message)
	# print('received message: ' + message)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
	flask_port = 65432
	host = '0.0.0.0'	
	#socketio.run(app)
	socketio.run(app, host=host, port=flask_port)

