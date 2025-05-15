import socket
import time
import json


from ..logging.cardinalLogger import CardinalLogger

# TODO: finish creating this class

class CardinalSocket:
    
    logger = CardinalLogger()
    socket = None
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug("Socket initialized")
    #enddef

    def handle_message(self, message):
        self.logger.debug()
#endclass
