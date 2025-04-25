
import os
import uuid
import socket
import configparser
import threading
import time
import subprocess

from core.Logging.cardinalLogger import CardinalLogger
from core.Models.models import *


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

    _db = None

    _running = False
    _config = None
    _logger = None

    _applications = []
    _threads = []
    _sockets = []
    #endregion - cardinal's variables ---------- #

    # init
    def __init__(self, app, config: configparser.ConfigParser = None, logger: CardinalLogger = None):
        self._app = app
        self.config = config if config else configparser.ConfigParser()
        self.config.read("application.cfg")
        self._logger = logger if logger else CardinalLogger()
        # self._logger.setLogger(self._config.get('Cardinal', 'logFilePath'))
    #enddef

    # this function will setup cardinal meaning that:
    # - it will setup the database (if not set)
    # - it will load the registered applications
    #- it will setup applications' databases (if not set)
    def setup(self):



        self._uid = self._generateUid()
        self._registeredApplications()
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
        self._logger.debug(self._logger.self._showStartData())

        self._setApplicationRoutes()
        # self.

    #enddef

    


    #############
    # UTILITIES #
    #region #####

    def _showStartData(self):
        """
        DESCRIPTION:
        Displays the start data of the Cardinal instance.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
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

        for application in self._applications:
            self._app.register_blueprint(application.) # TODO: fix this line
            # self._app.register_blueprint(application.getBlueprint())
            # self._app.register_blueprint(application)
    #enddef

    def _registeredApplications(self):
        """
        DESCRIPTION:
        loads the registered applications from the database.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """
        apps = Application.query.all()
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
        pass
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
