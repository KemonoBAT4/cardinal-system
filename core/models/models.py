
from .base import *

class User(UserMixin, BaseModel):

    __tablename__ = "users"

    name            = db.Column(db.String(80) , nullable=True )
    surname         = db.Column(db.String(80) , nullable=True )
    username        = db.Column(db.String(80) , nullable=False, unique=True )
    email           = db.Column(db.String(120), nullable=False, unique=True )
    hashed_password = db.Column(db.LargeBinary, nullable=False )

    @property
    def title(self) -> str:
        """
        #### DESCRIPTION:
        Returns the title of the user.

        #### PARAMETERS:
        - no parameters required

        #### RETURN:
        - str: The title of the user.
        """

        result: str = ""
        result = self.username

        # if (self.name is not None) and (self.surname is not None):
        #     result = " - ".join([self.surname, self.name])
        # else:
        #     result = self.username
        # # #endif

        return result
    # #enddef title

    @classmethod
    def register(cls, username: str, email: str, name: str, surname: str, password: str) -> "User | tuple":
        """
        #### DESCRIPTION:
        Adds a new user with the provided password.

        #### PARAMETERS:
        - username (str): The username of the user.
        - email (str): The email address of the user.
        - name (str): The name of the user.
        - surname (str): The surname of the user.
        - password (str): The password to set for the user.

        #### RETURN:
        - tuple: A tuple containing the status and message of the operation.
        """

        found_user: "User | None" = User.query.filter(
            or_(
                User.email    == email,
                User.username == username
            )
        ).first()


        if (found_user is not None):
            return User.Result(False, "User already exists").result()
        # #endif

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        user: "User" = User(
            name            = name,
            surname         = surname,
            username        = username,
            email           = email,
            hashed_password = hashed_password
        )
        user.save()

        return user
    #enddef register

    @classmethod
    def login(cls, username: str, password: str) -> "User | tuple":

        user: "User | None" = User.query.filter(
            User.username == username
        ).first()


        if user is None:
            return cls.Result(False, "User not found").result()
        # #endif

        if not bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
            return cls.Result(False, "Invalid password").result()
        # #endif
        return user
    #enddef login

    # NOTE: [IMPORTANT] method required for flask-login to work properly
    # binded with load_user method in core/system/startup.py
    def get_id(self) -> int:
        return self.id
    # #enddef get_id

    def save(self) -> tuple:

        if (self.hashed_password is None):
            return self.Result(False, "Password is required").result()
        #endif

        return super().save()
    # #enddef save

    def to_dict(self) -> dict:
        """
        #### DESCRIPTION:
        Converts the model instance to a dictionary representation.

        #### PARAMETERS:
        - no parameters required

        #### RETURN:
        - dict: A dictionary representation of the model instance.
        """
        result: dict = { }

        for key, value in vars(self).items():
            if ((not callable(getattr(self, key))) and (not key.startswith('_')) and (key != "hashed_password")):
                result[key] = value
            # #endif
        # #endfor

        return result
    # #enddef to_dict
#endclass

class Role(BaseModel):

    __tablename__ = "roles"

    code = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
#endclass

class Application(BaseModel):

    __tablename__ = "applications"

    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)
#endclass

class CardinalSystem(BaseModel):
    pass