#!/usr/bin/python3
"""This is a module that contains views for the State for this API"""
from flask import jsonify
from flask import request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_all_states():
    """This is a function that gets all states when the api/states route is
    reached"""
    result = storage.all(State).values()
    all_states = list(map(lambda x: x.to_dict(), result))
    return jsonify(all_states)
