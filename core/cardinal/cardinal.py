
import os
import uuid
import socket
import configparser
import threading
import time
import subprocess
import importlib

from core.models.base import db
from core.models.models import *
from core.handlers.handlers import *
from core.web.routes import main_routes

from flask import current_app

class Cardinal:

    _app = None
    _app_context = None
    _db = None

    _config = None

    _applications = []  # a list of all the application data
    _threads = []
    _sockets = []

    _version = None
    _api_version = None

    def __init__(self, app, config: configparser.ConfigParser = None):

        self._app = app
        self._app_context = app.app_context()
        self._app_context.push()

        self._config = config if config else configparser.ConfigParser()

        self._db = db

        # Register routes
        # self._app.register_blueprint(main_routes)

        # Load version from config
        # self._version = self._config.get("Cardinal", "version", fallback="0.1.0")
    #enddef

    def __del__(self):
        self._app_context.pop()
    #enddef

    def setup(self):
        """
        DESCRIPTION:
        sets all the variables needed
        """
        pass
        # self._setupApplications()
    #enddef

    def start(self):
        """
        DESCRIPTION:
        Starts the Cardinal instance by setting up the database, loading registered applications,
        and starting the applications in separate threads or sockets.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """
        cardinal_prefix = f'/cardinal'
        main_prefix = f'/'

        current_app.register_blueprint(main_routes, url_prefix=main_prefix)
        # if not self._running:
        #     self._running = True


            # self._logger.debug(self._showStartData())
            # self._setupApplications()
            # self._startApplications()
#endclass

# class Handlers:
#     def __init__(self):
#         pass

# logger = CardinalLogger()

# def resetDatabase(self):
#     """
#     DESCRIPTION:
#     Resets the database by dropping all tables and creating new ones.

#     PARAMETERS:
#     - no parameters required

#     RETURN:
#     - no return
#     """
#     try:
#         if db is not None:
#             logger.debug("Resetting the database . . .")
#             db.drop_all()
#             db.create_all()
#             logger.debug("Database reset complete")
#         else:
#             logger.error("Database is not set up. Cannot reset.")
#         #endif
#     except Exception as e:
#         logger.error(f"Error resetting the database: {e}")
#         logger.debug("See the log file for the complete error.")
#     #endtry
# #endde

