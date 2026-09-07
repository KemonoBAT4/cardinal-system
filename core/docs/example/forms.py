

from wtforms import Form, StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm                                                             # type: ignore

# local imports
from ._common import *
from .handlers import *
from .models import *

from core.form import *

class MovieForm(BaseForm):
    field1 = StringField('Field1', [validators.DataRequired()], render_kw={"size": 6})
    field2 = StringField('Field2', [validators.DataRequired()], render_kw={"size": 6})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #enddef

    def saveForm(self, obj, *args, **kwargs):
        self.populate_obj(obj)
        obj.save()
    # #enddef
#endclass

