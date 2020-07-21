from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateTimeField
from wtforms.validators import InputRequired


class ProxyForm(FlaskForm):
    user = StringField(validators=[InputRequired('Missing user')])
    date = DateTimeField(format='%Y%m%d%H%M%S', validators=[InputRequired('Missing date')])

