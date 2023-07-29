#!/usr/bin/python3
"""This is a module to render API to our application using Flask web
framework"""
import os
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_flask(exception):
    '''a tear down to close storage'''
    storage.close()


if __name__ == "__main__":
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=app_host, port=app_port, threaded=True)
