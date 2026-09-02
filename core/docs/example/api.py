
# local imports
from ._common import *
from .models import *

api = Blueprint(f'{project_name}_api', __name__)

@api.route("/example", methods=['GET', 'POST'])
def example_api():
    result: dict = {
        "status": True,
        "message": "example api endpoint"
    }

    return jsonify(result), 200
# #enddef example_api

