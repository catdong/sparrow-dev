import auth

from flask import Flask, request
from flask.ext.mongoengine import MongoEngine
from flask_socketio import SocketIO

from camera import camera_api
from pose import pose_api
from control import control_api
from monitor import monitor_api
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)
app.config["MONGODB_SETTINGS"] = {'DB': "sparrow_server_event_log"}

db = MongoEngine(app)

app.register_blueprint(pose_api)
app.register_blueprint(monitor_api)
app.register_blueprint(control_api)

<<<<<<< HEAD
#HOST = "10.34.162.81" # This needs to be modified for server's IP    
HOST = "localhost"
=======
HOST = "10.34.164.142" # This needs to be modified for server's IP    
>>>>>>> aa3bd83a9233836e7846cde8bc5208554684664e

socketio = SocketIO(app)

default_host= "127.0.0.1"

default_port= "5000"
