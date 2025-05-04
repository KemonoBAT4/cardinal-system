
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    """
    DESCRIPTION:
    Base model class for all database models in the application.
    """
    __abstract__ = True

    # update this when adding a new method that has to be avoided
    _methods_to_avoid = [ "to_dict", "save", "delete", "update", "patch" ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # created_at = db.Column(db.DateTime, nullable=False)
    # updated_at = db.Column(db.DateTime, nullable=False)

    def save(self):
        """
        DESCRIPTION:
        Saves the model instance to the database.

        PARAMETERS:
        - no parameters required

        RETURN:
        - no return
        """

        response = {
            "status": True,
            "message": "Object saved successfully"
        }
        try:
            # if self.id is None:
            #     self.created_at = db.func.current_timestamp()
            #     self.updated_at = db.func.current_timestamp()
            # else:
            #     self.updated_at = db.func.current_timestamp()
            # #endif

            db.session.add(self)
            db.session.commit()

            return response
        except Exception as e:
            db.session.rollback()

            response["status"] = False
            response["message"] = f"Error while saving object: {str(e)}"
            return response
        #endtry
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

    def update(self, object: any) -> dict:
        """
        DESCRIPTION:
        Updates the model instance with the provided object.

        PARAMETERS:
        - object (any): The object to update the model instance with (must be of the same type).

        RETURN:
        - dict: A dictionary containing the status and message.
        """
        response = {
            "status": True,
            "message": "Object updated successfully"
        }

        if not isinstance(object, self.__class__):
            response["status"] = False
            response["message"] = "Object type mismatch"
            return response
        #endif

        try:
            for attr in dir(object):
                if not attr.startswith('_') and attr not in ['id', 'creation_date']:
                    setattr(self, attr, getattr(object, attr))
                #endif
            #endfor

            self.save()
            return response
        except Exception as e:
            response["status"] = False
            response["message"] = f'Error: {str(e)}'
            return response
        #endtry
    #enddef

    def patch(self, patch_dict) -> bool:
        """
        DESCRIPTION:
        Updates the model instance with the provided patch dictionary.

        PARAMETERS:
        - patch_dict (dict): The patch dictionary to update the model instance with.

        RETURN:
        - dict: A dictionary containing the status and message.
        """
        response = {
            "status": True,
            "message": "Object updated successfully"
        }

        try:
            for key, value in patch_dict.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                #endif
            #endfor

            self.save()
            return True
        except Exception as e:
            response["status"] = False
            response["message"] = f'Error: {str(e)}'
            return False
        #endtry
    #enddef

    def to_dict(self) -> dict:
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
