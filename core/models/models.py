
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import backref, relationship

from core.Utils.models import BaseModel, db


class User(BaseModel):

    _classname = "User"
    __tablename__ = "users"

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
#endclass

class Role(BaseModel):

    _classname = "Role"
    __tablename__ = "roles"

    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
#endclass

class UserRole(BaseModel):

    _classname = "UserRole"
    __tablename__ = "user_roles"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = relationship(User, )
    # user = relationship("User", backref=backref("user_roles", cascade="all, delete-orphan"))

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    role = relationship("Role", backref=backref("user_roles", cascade="all, delete-orphan"))
#enclass

class Application(BaseModel):

    _classname = "Application"
    __tablename__ = "applications"

    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)

    path = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(255), nullable=False)
#endclass