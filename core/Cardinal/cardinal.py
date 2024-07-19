

import uuid

from Threads.threadManager import threadManager

class Cardinal:

    # CARDINAL LOGIC
    def cardinalRun(self, test):
        pass

    def cardinalStart(self, test):

        # creating the api thread
        apis_thread = threadManager.newThread(self.generateUid(), "Cardinal Flask Api", ) # FIXME: here goes the api script for the thread, search if its possible

        threadManager.startThread(apis_thread)



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

    
