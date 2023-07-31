#!/usr/bin/python3
"""
This module contains the blueprint for the API.
"""
from flask import Blueprint
app_views = Blueprint('app_view', __name__, url_prefix="/api/v1")
from api.v1.views.index import *
from api.v1.views.states import *
