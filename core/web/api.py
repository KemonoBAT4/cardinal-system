
import os
from pathlib import *
from core.configs import *

from flask import Blueprint, jsonify
from .handlers import *

api = Blueprint('main_api', __name__)


@api.route("/available/applications", methods=['GET'])
def available_applications():

    app_path: Path = Path(F"{ROOT_PATH}/app")
    result: list[dict] = []

    for folder in app_path.iterdir():

        if folder.is_dir():
            
            if folder.name != "cardinal":
                cfg_files = list(folder.glob("*.cfg"))

                for cfg_file in cfg_files:

                    _config = configparser.ConfigParser()
                    _config.read(cfg_file)

                    result.append(
                        {
                            "folder": folder.name,
                            "config": {
                                section: dict(_config[section])
                                for section in _config.sections()
                            }
                        }
                    )
                # #endfor
            # #endif
        # #endif    
    # #endfor

    print(result)

    computed_response_json = []

    for r in result:
        computed_response_json.append(
            {
                "name"        : r.get("config", {}).get("Cardinal", {}).get("name"),
                "version"     : f'{r.get("config", {}).get("Cardinal", {}).get("version_type")} {r.get("config", {}).get("Cardinal", {}).get("version")}',
                "author"      : r.get("config", {}).get("Cardinal", {}).get("author"),
                "api_version" : f'v{r.get("config", {}).get("Cardinal", {}).get("api")}',
                "host"        : r.get("config", {}).get("Cardinal", {}).get("host"),
                "port"        : r.get("config", {}).get("Cardinal", {}).get("port"),
            }
        )
    # #endfor

    return jsonify({"data": computed_response_json})
# #enddef available_applications
