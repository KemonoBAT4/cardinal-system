
# Cardinal Routes
from flask import Blueprint, jsonify, request
from flask import redirect, url_for, render_template

import configparser

from core.models.models import *

# TODO: implement login required

cardinal_routes = Blueprint('Cardinal_Routes', __name__)

config = configparser.ConfigParser()
config.read("application.cfg")


@cardinal_routes.route("/", methods=['GET'])
def dashboard_redirect():
    """
    Redirects to the dashboard page
    """
    return redirect(url_for('Cardinal_Routes.dashboard_routes'))
#enddef

@cardinal_routes.route("/dashboard", methods=['GET'])
def dashboard_routes():
    """
    Dashboard page
    """

    current_version = config.get("Cardinal", "version")
    username = "Kemono_BAT_4" # TODO: modify this
    # username = current_user.username
    title = "The Cardinal System"


    return render_template(
        'dashboard.html',
        cardinal_version=current_version,
        logged_user=username,
        main_title=title
    )

    # TODO: implement home dashboard, with login method
    # return result
#enddef


