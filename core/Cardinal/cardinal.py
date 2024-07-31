

import uuid
import socket

from Threads.threadManager import threadManager

class Cardinal:

    # INIT
    def __init__(self):
        self.cardinalStart()
    #enddef

    # CARDINAL LOGIC
    def cardinalRun(self, test):
        pass
    #enddef

    def _cardinalStart(self):

        # creating the socket
        
        # creating the socket thread TODO: fix this thread
        # cst = Cardinal Socket Thread
        cst = threadManager.newThread(id = self.generateUid(), description = "Cardinal Socket", function = 0, args=("./../../core/Cardinal/cardinalSocket.py",))        
        threadManager.startThread(cst)

        # creating the api thread TODO: fix this thread
        # cat = Cardinal Apis Thread                                                                                            TH COR
        cat = threadManager.newThread(id = self.generateUid(), description = "Cardinal Flask Api", function = 0, args=("./../../api/cardinalApi.py",))
        threadManager.startThread(cat)


        #TODO: maybe i can use sockets instead of thread (or even both) to excange data with external programs
        threadManager.joinThread(cst) # close the socket thread
        threadManager.joinThread(cat) # close the api thread


    #enddef

    def _cardinalShutdown(self, test):
        pass
    #enddef

    def cardianlReboot(self):
        pass
    #enddef



    #############
    # UTILITIES #
    #############

    # returns a unique id, no parameters required
    def generateUid():
        return str(uuid.uuid4())
    #enddef
#endclass
    
