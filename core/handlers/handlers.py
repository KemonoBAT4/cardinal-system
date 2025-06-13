
from core.models.base import db
from core.models.models import *

from core.web.routes import main_routes

# from core.logging.cardinalLogger import CardinalLogger
from flask import current_app

def resetDatabase() -> bool:
    """
    DESCRIPTION:
    Resets the database by dropping all tables and creating new ones.

    PARAMETERS:
    - no parameters required

    RETURN:
    - True if the database was reset successfully, False otherwise.
    """
    try:
        if db is not None:
            db.drop_all()
            db.create_all()
            return True
        else:
            raise Exception("Database is not set up. Cannot reset.")
        #endif
    except Exception as e:
        print(f"Error resetting the database: {e}")
        # logger.error(f"Error resetting the database: {e}")
        # logger.debug("See the log file for the complete error.")
    #endtry
    return False
#enddef

# logger = CardinalLogger()

# def resetDatabase(self):
#     """
#     DESCRIPTION:
#     Resets the database by dropping all tables and creating new ones.

#     PARAMETERS:
#     - no parameters required

#     RETURN:
#     - no return
#     """
#     try:
#         if db is not None:
#             logger.debug("Resetting the database . . .")
#             db.drop_all()
#             db.create_all()
#             logger.debug("Database reset complete")
#         else:
#             logger.error("Database is not set up. Cannot reset.")
#         #endif
#     except Exception as e:
#         logger.error(f"Error resetting the database: {e}")
#         logger.debug("See the log file for the complete error.")
#     #endtry
# #enddef
