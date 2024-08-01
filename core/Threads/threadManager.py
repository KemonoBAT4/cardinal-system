import threading
import time

from Logging.cardinalLogger import cardinalLogger
from thread import CardinalThread

class threadManager():

    def __init__():
        cardinalLogger.debug("Thread Manager initialized")
    #enddef

    def newThread(id, description, function):
        cardinalLogger.debug("created thread: " + id + " & " + description)
        return CardinalThread(id, description, function) # FIXME: probably wrong
    #enddef

    def startThread(self, thread, timout = 10):
        
        if(thread.thread_status == "running"):
            return True
        else:
            thread.start()

            if(thread.thread_status == "running"):
                return True
            else:
                cardinalLogger.warning("Could not start Thread: " + thread.get_thread_data().thread_id)
                cardinalLogger.warning("Retrying in a couple of seconds")
                if timout > 0:
                    timout = timout - 1
                    time.sleep(2)
                    return self.startThread(thread, timout)
                else:
                    cardinalLogger.error("Thread " +  thread.get_thread_data().thread_id + "exceeded") 
                    return False
            #endif
        #endif
    #enddef


    def joinThread(thread):
        thread.join()
    #enddef
#endclass
