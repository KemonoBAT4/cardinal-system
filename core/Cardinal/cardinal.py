
import os
import uuid
import socket
import configparser

from ..Threads.threadManager import ThreadManager
from ..Logging.cardinalLogger import CardinalLogger

class Cardinal:
    # region ---- cardinal variables ---------- #

    # cardinal personal info
    _uid = "" # cardinal's unique id
    _is_running = False # cardinal status
    _host = None # cardinal host
    _port = None # cardinal port
    _config = None # cardinal config file
    _logger = None # cardinal logger script

    # cardinal master info
    _master = None # Cardinal | none, cardinal master's

    # threads & thread manager
    _thread_manager = None
    _threads = []
    _queued_threads = []
    _active_threads = []
    _closed_threads = []

    # cardinal children info
    _childrens = [] # should be a list of cardinals
    _cardinal_childrens_connection = None # cardinl's connection with childrens

    # cardinal applications
    _applications = dict()

    # endregion-- cardinal variables ---------- #
    # INIT
    def __init__(self, master = None,  *args, **kwargs):

        self._config = configparser.ConfigParser()
        self._config.read("application.cfg")

        # setting the logger
        self.logger = CardinalLogger()
        self._thread_manager = ThreadManager(self.logger)

        self._uid = self._generateUid()
        #region setting the master infos
        if isinstance(master, Cardinal) and master != None:

            self._master = master
            self.logger.debug(f"Starting Cardianl With Master {self._master.getCardinalUid()}")
        #endregion master infos

        self._cardinalStart()
    #enddef

    def _cardinalStart(self):

        try:
            # creates the server
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # retrieves the application's host and port
            host = self._config.get('Cardinal', 'host')
            port = self._config.get('Cardinal', 'port')

                            # TODO: change into: int(port)
            server.bind((host, port))
            server.listen(5)


            self._is_running = True # switch status

            self.logger.debug(self._showStartData())
            # cardinal's core handler
            while self._is_running != False:
                client_socket, address = server.accept()
                print(f"Connection from {address} has been established.")

        except Exception as ex:
            pass


        # ------------------------------------------------------------------ #

        # creating the socket

        # creating the socket thread TODO: fix this thread
        # cst = Cardinal Socket Thread FIXME: https://realpython.com/python-sockets/

    #enddef

    def shutdown(self):
        self._force_join_all()

        self._is_running = False
        return True # retuns true if action shutdown successfully
    #enddef

    # TODO: finish this function
    def _startCardinalConsole(self):
        pass

    def _start_cardinal_listener_thread(self):
        clt = ThreadManager.newThread(id = self._generateUid(), description = "Cardinal Listener", function = 0, args="TODO: set function")
        ThreadManager.startThread(clt)
    #enddef

    #############
    # UTILITIES #
    #############

    def _killAllChildrens(self):
        for children in self._childrens:
            self._shutdownChildren(children)
    #enddef

    def _shutdownChildren(self, children):
        return children.shutdown()
    #enddef

    def _showStartData(self) -> str:
        # FIXME: fix this, implement the config reader, and finish the page inizializer
        return f"""

        #######################
        # WELCOME TO CARDINAL #
        #######################

        booting now . . .

        # --- CARDINAL INFORMATIONS --- #
        - current Cardinal version: {self._config.get('Cardinal', 'version')}
        - author: {self._config.get('Cardinal', 'author')}
        - source code: {self._config.get('Cardinal', 'source')}

        """

    #enddef

    def _newChildren(self):
        new = Cardinal(master=self)
    #enddef

    # returns the cardinal uid, no parameters required
    def getCardinalUid(self):
        return self._uid
    #enddef

    # returns a unique id, no parameters required
    def _generateUid(self):
        return str(uuid.uuid4())
    #enddef

    # returns a boolean if the action is completed or not
    def _force_join_all(self):
        self._kill_childrens()
        
        
        # TODO: implement this function in the ThreadManager script
        ThreadManager.force_join_all()
        return False
    #enddef

    def getCardinalData(self) -> dict:
        data = dict()

        data['id'] = self._uid # cardinals uid
        data['running'] = self._is_running # if the cardinal is running
        data['master_uid'] = self._master_uid # cardinal master's uid
        data['master_connection'] = self._master_connection # cardinal master's connection
        data['threads'] = self._threads # cardinal's threads
        data['childrens'] = self._childrens # cardinal's possible subordinates
        data['applications'] = self._applications # cardinal's applications

        return data
    #enddef

    def cardianlReboot(self):
        self.shutdown()
        self._cardinalStart()
    #enddef
#endclass
