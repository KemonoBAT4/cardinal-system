
import logging

from datetime import datetime

class CardinalLogger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)

    def debug(message):
        logger.debug(message)

    def warning(message):
        logger.warning(message)

    def error(message):
        logger.error(message)

