

import uuid
import socket

from ..Threads.threadManager import ThreadManager
from ..Logging.cardinalLogger import CardinalLogger

class Cardinal:
    
    # cardinal personal info
    _cardinal_uid = "" # cardinal's unique id
    _cardinal_connection = None # cardinl's connection with childrens
    logger = None

    # cardinal master info
    _master_uid = None # string | none, cardinal master's uid
    _master_connection = None # socket | none, cardinal master connection

    # cardinal children info
    _childrens = []

    # INIT
    def __init__(self, master_uid = None, master_connection = None, children_uid = None):
        self.logger = CardinalLogger()

        if master_uid != None:

            # if there is a master cardinal
            self._master_uid = master_uid
            self._master_connection = master_connection
            self._cardinal_uid = children_uid

            self.logger.debug("started cardinal with")
            
        else:

            # if this cardinal is the master or not related
            self._cardinal_uid = self._generateUid()

        self._cardinalStart()
    #enddef

    # CARDINAL LOGIC
    def cardinalRun(self, process_id, status = 'stop'):
        pass

    #enddef

    def _cardinalStart(self):

        # creating the socket
        
        # creating the socket thread TODO: fix this thread
        # cst = Cardinal Socket Thread FIXME: https://realpython.com/python-sockets/
        cst = ThreadManager.newThread(id = self._generateUid(), description = "Cardinal Socket", function = 0, args=("./../../core/Cardinal/cardinalSocket.py",))        
        ThreadManager.startThread(cst)

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

    def cardinalShutdown(self, test):
        pass
    #enddef

    def cardianlReboot(self):
        pass
    #enddef

    def _startCardinalConsole(self):
        pass



    #############
    # UTILITIES #
    #############

    def _showStartData(self):
        
        print("#######################")
        print("# WELCOME TO CARDINAL #")
        print("#######################")
        print("")
        print("")

    def _new_cardinal_children(self):
        pass

    # returns the cardinal uid, no parameters required
    def get_cardinal_uid(self):
        return self.cardinal_uid
    #enddef

    # returns a unique id, no parameters required
    def _generateUid(self):
        return str(uuid.uuid4())
    #enddef
#endclass
    
