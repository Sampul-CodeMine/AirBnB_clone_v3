#!/usr/bin/python3
'''Module that contains the index view for the API.'''
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status')
def status_getter():
    """route /status gets the status of the API"""
    return jsonify(status='OK')
