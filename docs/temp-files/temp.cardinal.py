
import os
import uuid
import socket
import configparser
import threading
import time
import subprocess


#TODO: check if this description is correct

# Cardinal is a class that represents a system for managing applications and their configurations.
# It provides methods for setting up the system, starting applications, and managing threads.
# It also includes methods for generating unique identifiers and managing application registrations.
# It is designed to be extensible and can be used as a base class for creating specific application systems.
# Cardinal is a singleton class, meaning that only one instance of it can exist at a time.
# It is initialized with an application instance and provides methods for setting up and starting the system.
# It also includes methods for managing application registrations and generating unique identifiers.

class Cardinal:

    _uid = None
    _app = None

    

    def __init__(self, app):
        self._app = app
    #enddef

    def setup(self):
        self._uid = self._generateUid()
    #enddef

    def start(self):
        pass
    #enddef



    #############
    # UTILITIES #
    #region #####

    def _registeredApplications(self):
        """
        DESCRIPTION:
        loads the registered applications from the database.

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
