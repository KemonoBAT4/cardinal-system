
# Main Routes
from flask import Blueprint, jsonify, request, send_from_directory
from flask import redirect, url_for, render_template

import os

# TODO: implement login required
from flask_login import login_required
from core.Models.models import *
# from core.Web.template import *

main_routes = Blueprint('Main_Routes', __name__)

@main_routes.route("/", methods=['GET', 'POST'])
def index():
    return redirect("/home")
#enddef

@main_routes.route("/home", methods=['GET'])
def home():
    # return "home page test"

    return render_template('homepage.html')

    # home page
#enddef

@main_routes.route("/login", methods=['GET'])
def dashboard_routes():
    """
    Dashboard page
    """
    return "Login page test"
#enddef


#################
# GET THE FILES #
#################

@main_routes.route("/styles/<string:app>/<path:filename>", methods=['GET'])
def styles(app, filename):
    if "cardinal" in app.lower():
        return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'web', 'styles'), filename)
    #endif
#enddef

@main_routes.route("/scripts/<string:app>/<path:filename>", methods=['GET'])
def scripts(app, filename):
    if "cardinal" in app.lower():
        return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'web', 'scripts'), filename)
    #enddef
#enddef
