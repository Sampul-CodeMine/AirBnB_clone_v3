#!/usr/bin/python3
"""This is a module that contains views for the State for this API"""
from flask import jsonify
from flask import request
from werkzeug.exceptions import NotFound, BadRequest
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_all_states():
    """This is a function that gets all states when the /states route is
    reached"""
    result = storage.all(State).values()
    all_states = list(map(lambda x: x.to_dict(), result))
    return jsonify(all_states)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_one_state(state_id):
    """This is a function that gets a state when the /states/state_id route
    is reached"""
    result = storage.all(State).values()
    if state_id:
        one_state = list(filter(lambda x: x.id == state_id, result))
        if one_state:
            return jsonify(one_state[0].to_dict())
        raise NotFound()


@app_views.route("/states/<state_id>", methods=["DELETE", "GET"],
                 strict_slashes=False)
def delete_one_state(state_id=None):
    """this is a function that deletes a specified state when the
    /states/states_id route is reached"""
    result = storage.all(State).values()
    if state_id:
        one_state = list(filter(lambda x: x.id == state_id, result))
        if one_state:
            storage.delete(one_state[0])
            storage.save()
            return jsonify({}), 200
    raise NotFound()


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state(state_id=None):
    """This is a function that creates a state at the /states route's
    endpoint"""
    user_request = request.get_json()
    if type(user_request) is dict:
        if 'name' in user_request:
            state = State(**user_request)
            state.save
            return jsonify(state.to_dict()), 201
        else:
            raise BadRequest(description='Missing name')
    else:
        raise BadRequest(description='Not a JSON')


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_one_state(state_id=None):
    """This is a function that updates a state at the /states/state_id route's
    endpoint"""
    result = storage.all(State).values()
    state = list(filter(lambda x: x.id == state_id, result))
    if state:
        update_request = request.get_json()
        if type(update_request) is dict:
            update = state[0]
            for item, value in update_request.items():
                if item not in ["id", "created_at", "updated_at"]:
                    setattr(update, item, value)
            update.save()
            return jsonify(update.to_dict()), 200
        else:
            raise BadRequest(description='Not a JSON')
    else:
        raise NotFound()
