
import threading
import subprocess
import time

class CardinalThread():

    _thread = None
    _id = None
    _description = None
    _function = None
    _running = False
    _args = None
    

    _logger = None
    _classname = "CardinalThread"

    def __init__(self, id, description = "No description provided", function, *args, **kwargs):
        self._thread = threading.Thread()
        self._id = id
        self._description = description
        self._args = *args
    #enddef

    def new(self, id, description, function, args):
        pass
                    
        
#endclass
