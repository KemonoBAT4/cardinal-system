# imports
import os
import configparser
import sys
import typing
import uuid

#################
# CONFIGURATION #
#region #########
config = configparser.ConfigParser()

args: list  = sys.argv.copy()
runner: str = args.pop(0) # run.py
name: str   = args.pop(0) # name

ROOT_PATH: str = os.path.join((os.path.dirname(os.path.abspath(__file__))), "..", "..")

NoneType = type(None)

def generate_uuid() -> str:
    return uuid.uuid4().hex
# #enddef generate_uuid

def build_db_uri(cfg: configparser.ConfigParser) -> str:
    """
    #### DESCRIPTION:
    Returns the database URI based on the configuration (tries to get the env vars first).

    #### PARAMETERS:
    - cfg: configparser.ConfigParser -> the configuration parser

    #### RETURN:
    - str : the database URI
    """

    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT", "3306")
    db_name = os.environ.get("DB_NAME")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASSWORD")

    if all([db_host, db_name, db_user, db_pass]):
        return f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    # #endif

    return cfg.get("Cardinal Database", "SQLALCHEMY_DATABASE_URI")
# #enddef build_db_uri

def get_cardinal_text(cardinal: "Cardinal") -> str: # type: ignore
    return f"""
    #######################
    # WELCOME TO CARDINAL #
    #######################

    # --- SYSTEM INFORMATIONS --- #
    - current system name: {cardinal._config.get('Cardinal', 'name')}
    - current system version: {cardinal.version}
    - author: {cardinal._config.get('Cardinal', 'author')}
    - source code: {cardinal._config.get('Cardinal', 'source')}
    - current database version: {cardinal._config.get('Cardinal', 'version')}

    # --- SYSTEM CONFIGURATIONS --- #
    - host: {cardinal._host}
    - port: {cardinal._port}

    # --- DATABASE INFORMATIONS --- #
    - current database path: {build_db_uri(cardinal._config)}

    # --- SYSTEM DEFAULT PATHS --- #
    - cardinal dashboard base path: '/cardinal'
    - cardinal authentication base path: '/auth'
    """
# #enddef get_cardinal_text
#endregion ######