import threading
import time

from Logging.cardinalLogger import cardinalLogger
from thread import CardinalThread

class threadManager():

    def __init__():
        cardinalLogger.info("Thread Manager initialized")
    #enddef

    def newThread(id, description, function):
        return CardinalThread(id, description, function) # FIXME: probably wrong
    #enddef

    def startThread(thread):
        
        if(thread.thread_status == "running"):
            return False
        else:
            thread.start()

            if(thread.thread_status == "running"):
                return True
            else:
                cardinalLogger.warning("Could not start Thread: " + thread.thread_id)
                return False
            #endif
        #endif
    #enddef


    def joinThread(thread):
        thread.join()
    #enddef
#endclass
