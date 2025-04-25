
# flask imports:
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt

# other imports:
import configparser

# cardinal imports:
from core.Cardinal.cardinal import Cardinal

# FIXME: fix this imports
# from ..models import *
# from ..utils import *
# from ..rotues import *

# Create App
app = Flask(__name__)
cors = CORS(app)

# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #TODO: change this

cardinal = Cardinal(app, config=configparser.ConfigParser())
cardinal.setup()

if __name__ == "__main__":
    cardinal.start()
    app.run(debug=True, host='0.0.0.0')
#endif