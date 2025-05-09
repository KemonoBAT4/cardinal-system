
import os
import uuid
import socket
import configparser
import threading
import time
import subprocess
import importlib

from core.Logging.cardinalLogger import CardinalLogger
from core.Models.models import *

# Import Routes
from core.routes.cardinal_routes import cardinal_routes
from core.routes.main_routes import main_routes

from flask import current_app


#TODO: check if this description is correct

# Cardinal is a class that represents a system for managing applications and their configurations.
# It provides methods for setting up the system, starting applications, and managing threads.
# It also includes methods for generating unique identifiers and managing application registrations.
# It is designed to be extensible and can be used as a base class for creating specific application systems.
# Cardinal is a singleton class, meaning that only one instance of it can exist at a time.
# It is initialized with an application instance and provides methods for setting up and starting the system.
# It also includes methods for managing application registrations and generating unique identifiers.

class Cardinal:

    #region ---- cardinal's variables ---------- #
    _uid = None
    _app = None
    _app_context = None

    _db = None

    _running = False
    _config = None
    _logger = None

    _applications = [] # a dict of all the application datas
    _threads = []
    _sockets = []

    _version = None
    _api_version = None

    #endregion - cardinal's variables ---------- #

    # init
    def __init__(self, app, config: configparser.ConfigParser = None, logger: CardinalLogger = None):

        self._app = app
        self._app_context = app.app_context()
        self._app_context.push()

        self._config = config if config else configparser.ConfigParser()
        self._logger = logger if logger else CardinalLogger()
    #enddef

    def __del__(self):
        self._app_context.pop()
    #enddef

    # this function will setup cardinal meaning that:
    # - it will setup the database (if not set)
    # - it will load the registered applications
    #- it will setup applications' databases (if not set)
    def setup(self):
        """
        DESCRIPTION:
        sets all the variables
        """

        self._uid = self._generateUid()
        self._setupApplications()
    #enddef

    # this function will start cardinal meaning that:
    # - it will run all the things that got set up in the setup function
    # - it will run the loaded applications in a separate thread / sockets
    # - it will run a dashboard management page
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

        if not self._running:
            self._running = True

            self._logger.debug(self._showStartData())
            current_app.register_blueprint(cardinal_routes, url_prefix=cardinal_prefix)
            current_app.register_blueprint(main_routes, url_prefix=main_prefix)
        #endif
    #enddef

    #############
    # UTILITIES #
    #region #####

    def _showStartData(self) -> str:
        """
        DESCRIPTION:
        Displays the start data of the Cardinal instance.

        PARAMETERS:
        - no parameters required

        RETURN:
        - str: The start data of the Cardinal instance.
        """

        return f"""

        #######################
        # WELCOME TO CARDINAL #
        #######################

        booting now . . .

        # --- CARDINAL INFORMATIONS --- #
        - current Cardinal version: {self._config.get('Cardinal', 'version')}
        - author: {self._config.get('Cardinal', 'author')}
        - source code: {self._config.get('Cardinal', 'source')}
        # ----------------------------- #

        """
    #enddef

    def _setApplicationRoutes(self):
        """
        DESCRIPTION:
        Sets up the application routes.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """

        pass

        # for dict in self._applications:
        #     blueprint_folder = os.path.join(os.path.dirname(__file__), 'apps', dict['blueprint_name'])
        #     routes_module = importlib.import_module(f'{dict["blueprint_name"]}.routes')
        #     current_app.register_blueprint(getattr(routes_module, f'{dict["blueprint_name"]}_routes'), url_prefix=dict['url_prefix'])
        # #endfor
    #enddef

    def _setupApplications(self):
        """
        DESCRIPTION:
        Sets up the applications by creating their databases and initializing them

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """

        applications = Application.query.all()

        for application in applications:
            # application.delete()
            self._applications.append(application.to_dict())
        #endfor

        self._setApplicationRoutes()
    #enddef

    def _setupThreads(self):
        pass
    #enddef

    def _generateUid(self) -> str:
        """
        DESCRIPTION:
        Generates a unique identifier (UID) for the Cardinal instance.

        PARAMETERS:
        - no parameters required

        RETURN:
        - str: A unique identifier (UID).
        """
        return str(uuid.uuid4())
    #enddef

    #endregion ##
#endclass
