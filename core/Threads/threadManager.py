import threading
import time

from ..Logging.cardinalLogger import CardinalLogger
from .thread import CardinalThread

# TODO: fix this class


class ThreadManager():

    def __init__():
        CardinalLogger.debug("Thread Manager initialized")
    #enddef

    def newThread(id, description, function, args):
        CardinalLogger.debug("creating thread: " + id + " & " + description)
        thread_class = CardinalThread()
        
        return thread_class.new(id, description, function, args) # FIXME: probably wrong
    #enddef

    def startThread(self, thread, timout = 10):
        
        if(thread.thread_status == "running"):
            return True
        else:
            thread.start()

            if(thread.thread_status == "running"):
                return True
            else:
                CardinalLogger.warning("Could not start Thread: " + thread.get_thread_data().thread_id)
                CardinalLogger.warning("Retrying in a couple of seconds")
                if timout > 0:
                    timout = timout - 1
                    time.sleep(2)
                    return self.startThread(thread, timout)
                else:
                    CardinalLogger.error("Thread " +  thread.get_thread_data().thread_id + "exceeded") 
                    return False
            #endif
        #endif
    #enddef


    def joinThread(thread):
        thread.join()
    #enddef
#endclass
