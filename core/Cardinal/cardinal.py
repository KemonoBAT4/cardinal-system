
import os
import uuid
import socket
import configparser

from ..Threads.threadManager import ThreadManager
from ..Logging.cardinalLogger import CardinalLogger

class Cardinal:
    # region ---- cardinal variables ---------- #
    # cardinal personal info
    _cardinal_uid = "" # cardinal's unique id
    _cardinal_connection = None # cardinl's connection with childrens
    _is_running = False
    _config = None
    _logger = None

    # cardinal master info
    _master_uid = None # string | none, cardinal master's uid
    _master_connection = None # socket | none, cardinal master connection

    # threads & thread manager

    _thread_manager = None

    _threads = []
    _active_threads = []
    _closed_threads = []


    # cardinal children info
    _childrens = []

    # endregion-- cardinal variables ---------- #
    # INIT
    def __init__(self, master_uid = None, master_connection = None, children_uid = None):

        self._config = configparser.ConfigParser()
        self._config.read("application.cfg")

        # setting the logger
        self.logger = CardinalLogger()  
        self._thread_manager = ThreadManager(self.logger)

        #region setting the master infos
        if master_uid != None:
            # if there is a master cardinal
            self._master_uid = master_uid
            self._master_connection = master_connection
            self._cardinal_uid = children_uid

            self.logger.debug("started cardinal with")
        else:

            # if this cardinal is the master or not related
            self._cardinal_uid = self._generateUid()
        #endregion master infos

        self._cardinalStart()
    #enddef

    # CARDINAL LOGIC
    def cardinalRun(self, process_id, status = 'stop'):
        pass
    #enddef

    def _cardinalStart(self):

        self._is_running = True

        _start_text = self._showStartData()
        self.logger.debug(_start_text)

        # start cardinal listener thread
        self._start_cardinal_listener_thread()

        
        
        # creating the socket

        # creating the socket thread TODO: fix this thread
        # cst = Cardinal Socket Thread FIXME: https://realpython.com/python-sockets/

        # all the threads are not real threads, are class instances of CardinalThread

        # FIXME: all thread gives errors
        # cst = self._thread_manager.newThread(id = self._generateUid(), description = "Cardinal Socket", function = 0, args=("./core/Socket/cardinalSocket.py",))

        # self._thread_manager.startThread(cst)

        return True
        # creating the api thread TODO: fix this thread
        # cat = Cardinal Apis Thread                                                                                            TH COR
        cat = ThreadManager.newThread(id = self._generateUid(), description = "Cardinal Flask Api", function = 0, args=("./../../api/cardinalApi.py",))
        ThreadManager.startThread(cat)

        #TODO: maybe i can use sockets instead of thread (or even both) to excange data with external programs
        ThreadManager.joinThread(cst) # close the socket thread
        ThreadManager.joinThread(cat) # close the api thread

        self._showStartData()
        self._startCardinalConsole()
    #enddef

    def shutdown(self, test):
        self._force_join_all()
        
        self._is_running = False
    #enddef


    # FIXME: do an actual reboot of the system
    def cardianlReboot(self):
        self._is_running = False
        self._cardinalStart()
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

    def _kill_childrens():
        for children in _childrens:
            children.shutdown()

    def _showStartData(self):
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

    def _new_cardinal_children(self):
        pass
    #enddef

    # returns the cardinal uid, no parameters required
    def get_cardinal_uid(self):
        return self._cardinal_uid
    #enddef

    # returns a unique id, no parameters required
    def _generateUid(self):
        return str(uuid.uuid4())
    #enddef

    # returns a boolean if the action is completed or not
    def _force_join_all():

        self._kill_childrens()
        
        
        # TODO: implement this function in the ThreadManager script
        ThreadManager.force_join_all()
        return False
        
#endclass
