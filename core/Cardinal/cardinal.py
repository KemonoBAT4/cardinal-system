

import uuid
import socket

from Threads.threadManager import threadManager

class Cardinal:

    # INIT
    def __init__(self):
        self.cardinalStart()

    # CARDINAL LOGIC
    def cardinalRun(self, test):
        pass

    def cardinalStart(self, test):

        # creating the api thread                                                                                                 TH COR
        apis_thread = threadManager.newThread(id = self.generateUid(), description = "Cardinal Flask Api", function = 0, args=("./../../api/cardinalApi.py",))
        
        threadManager.startThread(apis_thread)


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

    
