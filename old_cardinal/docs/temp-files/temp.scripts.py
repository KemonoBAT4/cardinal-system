
import os
import logging
import psutil

from datetime import datetime

# logging possibilities 
logger = logging.getLogger(__name__)
logging.basicConfig(filename='cardinal.log', encoding='utf-8', level=logging.DEBUG)


logger.debug("this message should go to the log file")
logger.info("so should this")
logger.warning("and this, too")
logger.error("and non-ASCII stuff, too, like Øresund and Malmö")
#-------------------------------------

# cpu percentage method 1
cpu = psutil.cpu_percent(4)
now = datetime.now()

string = ("cpu: " + cpu + "; time: " + now)
logger.info(string)
#-------------------------------------


# cpu percentage method 2
load1, load5, load15 = psutil.getloadavg()
now = datetime.now()

cpu = (load15/os.cpu_count()) * 100

string = ("cpu: " + cpu + "; time: " + now)
logger.info(string)
#-------------------------------------


# infos
# https://docs.python.org/3/howto/logging.html
# https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/
#-------------------------------------


# NOTE:
'''
    This cardinal should act like the openbridge application
    but with some upgrades like auto update scripts, chatbots, a login system
    for accessing the data and a rest api 
'''
