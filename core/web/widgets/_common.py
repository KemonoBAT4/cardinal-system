
# other imports
import pandas as pd
import typing
import uuid
import json
# import requests

# core imports
from core import configs

class CardinalBaseWidget:
    def render(self) -> str:
        raise NotImplementedError
    # #enddef render
# #endclass
