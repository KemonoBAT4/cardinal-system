

import uuid

from .Threads.threadManager import threadManager

class Cardinal:

    # INIT
    def __init__(self):
        self.cardinalStart()

    # CARDINAL LOGIC
    def cardinalRun(self, test):
        pass

    def cardinalStart(self, test):

        apis_thread = threadManager.newThread(generateUid(), "Cardinal Flask Api", ) # FIXME: here goes the api script for the thread, search if its possible


        #TODO: maybe i can use sockets instead of thread (or even both) to excange data with external programs

        # pass

    def cardinalShutdown(self, test):
        pass

    def cardinalLogin(self, test):
        pass
    
    def cardinalLogout(self, test):
        pass

    def cardianlReboot(self, test):
        pass




    #############
    # UTILITIES #
    #############

    # returns a unique id, no parameters required
    def generateUid():
        return str(uuid.uuid4())

    
