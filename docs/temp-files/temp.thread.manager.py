import threading
import time

from ..logging.cardinalLogger import CardinalLogger
from .thread import CardinalThread


class aThreadManager():

    _logger = None
    _classname = "CardinalThreadManager"

    def __init__(self, logger: CardinalLogger):
        self._logger = logger
        # self._logger.debug("Thread Manager initialized")
    #enddef

    def newThread(self, id, description, function, args):
        self._logger.debug("creating thread: " + id + " & " + description)
        thread_class = CardinalThread()

        return thread_class.new(id, description, function, args) # FIXME: probably wrong
    #enddef

    def startThread(self, thread, timout = 10):

        if(thread.get_thread_status() == "running"):
            return True
        else:
            thread.start()

            if(thread.thread_status == "running"):
                return True
            else:
                self._logger.warning("Could not start Thread: " + thread.get_thread_data().thread_id)
                self._logger.warning("Retrying in a couple of seconds")
                if timout > 0:
                    timout = timout - 1
                    time.sleep(2)
                    return self.startThread(thread, timout)
                else:
                    self._logger.error("Thread " +  thread.get_thread_data().thread_id + "exceeded") 
                    return False
            #endif
        #endif
    #enddef


    def joinThread(self, thread):
        thread.join()
    #enddef
#endclass
