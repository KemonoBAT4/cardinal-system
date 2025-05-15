
# Main Routes
from flask import Blueprint, jsonify, request, send_from_directory
from flask import redirect, url_for, render_template

import os
import configparser

# TODO: implement login required
from flask_login import login_required
from core.models.models import *
# from core.Web.template import *

main_routes = Blueprint('Main_Routes', __name__)

config = configparser.ConfigParser()
config.read("application.cfg")

@main_routes.route("/", methods=['GET', 'POST'])
def index():
    return redirect("/home")
#enddef

@main_routes.route("/home", methods=['GET'])
def home():
    # return "home page test"

    current_version = config.get("Cardinal", "version")
    username = "Kemono_BAT_4"
    # username = current_user.username
    title = "The Cardinal System"


    return render_template(
        'homepage.html',
        cardinal_version=current_version,
        logged_user=username,
        main_title=title
    )

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
