
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship

db = SQLAlchemy()

class BaseModel(db.Model):
    """
    DESCRIPTION:
    Base model class for all database models in the application.
    """
    __abstract__ = True

    # update this when adding a new method that has to be avoided
    _methods_to_avoid = [ "to_dict", "save", "delete" ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        """
        DESCRIPTION:
        Saves the model instance to the database.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """
        db.session.add(self)
        db.session.commit()
    #enddef

    def delete(self):
        """
        DESCRIPTION:
        Deletes the model instance from the database.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """
        db.session.delete(self)
        db.session.commit()
    #enddef

    def to_dict(self):
        """
        DESCRIPTION:
        Converts the model instance to a dictionary representation.

        PARAMETERS:
        - no parameters required

        RETURN:
        - dict: A dictionary representation of the model instance.
        """
        result = { }

        # TODO: try it
        # for column in self.__table__.columns:
        #     if column.name not in self._methods_to_avoid:
        #         result[column.name] = getattr(self, column.name)
        for key, value in vars(self).items():
            if not key.startswith('_') and key not in self._methods_to_avoid:
                result[key] = value
        return result
    #enddef

    def __repr__(self):
        return f"<{self._class__.__name__} {self.id}>"
    #enddef
#endclass
