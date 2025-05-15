

# flask imports:
from flask import Flask, request, jsonify, redirect, url_for
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
from core.Models.models import db

# Create App
app = Flask(__name__, template_folder="core/web/templates")
cors = CORS(app)

config = configparser.ConfigParser()
config.read("application.cfg")

# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Cardinal Database', 'SQLALCHEMY_DATABASE_URI')

# Init app's database
db.init_app(app)

# TODO: find a way to not comment / uncomment every time we need a database reset / migration
# from core.Models.models import *
# with app.app_context():
#     db.create_all()

cardinal = Cardinal(app=app, config=config)
cardinal.setup()

if __name__ == "__main__":
    cardinal.start()
    app.run(debug=True, host='0.0.0.0')
#endif
