
import logging

from datetime import datetime

# Log Class, Should be called only by Cardinal itself
class CardinalLogger():
    logger = logging.getLogger(__name__)

    def __init__(self):
        
        logging.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)

    def debug(self, message):
        self.logger.debug(datetime.now() + ": " + message)

    def warning(self, message):
        self.logger.warning(datetime.now() + ": " + message)

    def error(self, message):
        self.logger.error(datetime.now() + ": " + message)

