import threading
import time

from ..Logging.cardinalLogger import CardinalLogger
from .thread import CardinalThread

# TODO: fix this class

class ThreadManager:
    _logger = None
    _classname = "CardinalThreadManager"

    def __init__(self, logger: CardinalLogger):
        self._logger = logger
    #enddef

    def newThread(self, id, description, function, *args, **kwargs):
        pass
    #enddef

    def startThread(self, thread, timout = 10):
        pass
    #enddef

