
import logging

from datetime import datetime

# Log Class, Should be called only by Cardinal itself
class CardinalLogger():
    logger = logging.getLogger(__name__)

    # FIXME: fix this class
    def __init__(self):
        pass
        # self.logger.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)

    def debug(self, message = ""):
        pass
        # self.logger.debug(datetime.now() + ": " + message)

    def warning(self, message = ""):
        pass
        # self.logger.warning(datetime.now() + ": " + message)

    def error(self, message = ""):
        pass
        # self.logger.error(datetime.now() + ": " + message)

