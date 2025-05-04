
from flask import Blueprint, jsonify, request
from flask import redirect, url_for, render_template

test1_routes = Blueprint('Test1_Routes', __name__)

@test1_routes.route("/banana", methods=['GET'])
def a():
    pass
#enddef 