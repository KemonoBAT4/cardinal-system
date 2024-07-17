import threading
import time

from Logging.cardinalLogger import cardinalLogger
from thread import CardinalThread

class threadManager():

    def __init__():
        cardinalLogger.info("Thread Manager initialized")
    

    def newThread(id, description, function):
        return CardinalThread(id, description, function) # FIXME: probably wrong

    def startThread(thread):
        
        if(thread.thread_status == "running"):
            return False
        else:
            thread.start()

            if(thread.thread_status == "running"):
                return True
            else:
                cardinalLogger.warning("Could not start Thread: " + thread_id)


    def joinThread(thread):
        thread.join()