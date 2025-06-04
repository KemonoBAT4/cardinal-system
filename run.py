
# flask imports:
from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from core.cardinal.cardinal import Cardinal

import configparser

from core.cardinal.cardinal import Cardinal
from core.models.base import db

# Create App
app = Flask(__name__,  template_folder="core/web/templates")
cors = CORS(app)

config = configparser.ConfigParser()
config.read("application.cfg")

# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Cardinal Database', 'SQLALCHEMY_DATABASE_URI')

host = config.get("Cardinal", "host")
port = int(config.get("Cardinal", "port"))

# Init app's database
db.init_app(app)

cardinal = Cardinal(app=app, config=config)
cardinal.setup()

if __name__ == "__main__":
    cardinal.start()
    app.run(debug=True, host=host, port=port)
#endif
