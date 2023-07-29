#!/usr/bin/python3
"""
This module contains the blueprint for the API.
"""

from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_view', __name__, url_prefix="/api/v1")
