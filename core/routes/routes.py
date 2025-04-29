
# Cardinal Routes
from flask import Blueprint, jsonify, request
from flask import redirect, url_for
# TODO: implement login required

cardinal_routes = Blueprint('Cardinal_Routes', __name__)

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
    # TODO: implement home dashboard, with login method
    return "test"
#enddef
