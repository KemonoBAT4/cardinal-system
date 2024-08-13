

import uuid
import socket

from Threads.threadManager import ThreadManager
from Logging.cardinalLogger import CardinalLogger

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

        self.cardinalStart()
    #enddef

    # CARDINAL LOGIC
    def cardinalRun(self, function):
        pass
    #enddef

    def _cardinalStart(self):

        # creating the socket
        
        # creating the socket thread TODO: fix this thread
        # cst = Cardinal Socket Thread
        cst = ThreadManager.newThread(id = self.generateUid(), description = "Cardinal Socket", function = 0, args=("./../../core/Cardinal/cardinalSocket.py",))        
        ThreadManager.startThread(cst)

        # creating the api thread TODO: fix this thread
        # cat = Cardinal Apis Thread                                                                                            TH COR
        cat = ThreadManager.newThread(id = self.generateUid(), description = "Cardinal Flask Api", function = 0, args=("./../../api/cardinalApi.py",))
        ThreadManager.startThread(cat)


        #TODO: maybe i can use sockets instead of thread (or even both) to excange data with external programs
        ThreadManager.joinThread(cst) # close the socket thread
        ThreadManager.joinThread(cat) # close the api thread


    #enddef

    def cardinalShutdown(self, test):
        pass
    #enddef

    def cardianlReboot(self):
        pass
    #enddef



    #############
    # UTILITIES #
    #############

    def _new_cardinal_children():
        

    # returns the cardinal uid, no parameters required
    def get_cardinal_uid(self):
        return self.cardinal_uid
    #enddef

    # returns a unique id, no parameters required
    def _generateUid():
        return str(uuid.uuid4())
    #enddef
#endclass
    
