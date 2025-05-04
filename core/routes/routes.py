
# Cardinal Routes
from flask import Blueprint, jsonify, request
from flask import redirect, url_for, render_template

from core.Models.models import *
from core.Web.template import *

# from core.Web.

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

    # breakpoint()

    # appa = Application(
    #     name="test1",
    #     description="test1 description",
    #     blueprint_name="test1",
    #     folder_path = "test1",
    #     url_prefix = "test1"
    # )

    result = []

    [result.append(i.to_dict()) for i in Application.query.all()]
    
    # result = appa.save()

    # return render_template("template/dashboard.html")
 
    # TODO: implement home dashboard, with login method
    return result
#enddef


