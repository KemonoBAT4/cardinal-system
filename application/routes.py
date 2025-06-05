
from flask import Blueprint, redirect, url_for
from flask import render_template, send_from_directory

import os
import json

from core.models.base import db
from core.web.pages import *

# config = configparser.ConfigParser()
with open(f'{os.path.dirname(os.path.realpath(__file__))}\config.json', 'r') as f:
    data = json.load(f)
#endwith

routes = Blueprint(data.get("name"), __name__)

@routes.route("/test", methods=['GET', 'POST'])
def index():
    return "test"
#enddef