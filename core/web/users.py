# other imports
import os
import configparser

# flask imports
from flask import Blueprint, redirect, url_for, request, jsonify
from flask import render_template, send_from_directory
from flask_login import login_required, login_user, logout_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# local imports
from .pages import *
from .handlers import *

from core.configs import config

from core.models.base import db
from core.models.models import User

auth = Blueprint('auth', __name__)

@auth.route("/", methods=['GET'])
def index():
    return redirect(url_for('auth   .me'))
# #enddef index

@auth.route("/login", methods=['GET', 'POST'])
def login():
    """
    #### DESCRIPTION:
    Page to log in the user
    """

    if (request.method == 'POST'):

        data: dict = request.get_json()

        username: str = data.get("username", "")
        password: str = data.get("password", "")

        user: User | tuple = User.login(
            username = username,
            password = password
        )

        status  : bool = True
        message : str  = "Successfully logged in"

        if isinstance(user, User):
            login_user(user)
        else:
            status  = False

            if (user[1] == "Invalid password"):
                message = "Password incorretta"
            elif (user[1] == "User not found"):
                message = "Utente non trovato"
            else:
                message = "Unknown error"
            # #endif
        # #endif

        return jsonify({"status": status, "message": message}), 200
    else:
        page: AuthPage = AuthPage(
            page_title = "",
            template   = "login.html",
        )

        return page.render()
    # #endif
# #enddef login

@auth.route("/register", methods=['GET', 'POST'])
def register():
    """
    #### DESCRIPTION:
    Page to registers a new user
    """

    if (request.method == 'POST'):
        data: dict = request.get_json()

        first_name : str = data.get("first_name", "")
        last_name  : str = data.get("last_name" , "")
        username   : str = data.get("username"  , "")
        email      : str = data.get("email"     , "")
        password   : str = data.get("password"  , "")

        user: User | tuple = User.register(
            username = username,
            email    = email,
            name     = first_name,
            surname  = last_name,
            password = password
        )

        status  : bool = True
        message : str  = "Account successfully registered"

        if isinstance(user, User):
            login_user(user)
        else:
            status  = False
            if (user[1] == "User already exists"):
                message = "Utente già esistente"
            else:
                message = "Unknown error"
            # #endif
        # #endif

        return jsonify({"status": status, "message": message}), 200
    else:
        page: AuthPage = AuthPage(
            page_title = "",
            template   = "register.html",
        )

        return page.render()
    # #endif
# #enddef register

@auth.route("/me", methods=['GET'])
@login_required
def me():
    page = Page(page_title="The Cardinal System", title="Cardinal: Me")
    return page.render()
# #enddef me

@auth.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
#enddef logout
