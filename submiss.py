from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
SECRET_KEY = 'my-secrete-key'
class LoginForm(FlaskForm):
    current_password=PasswordField('Current Password',validators=[DataRequired()])
    new_pass=PasswordField('New Password',validators=[DataRequired()])
    retype_pass=PasswordField('Retype Password',validators=[DataRequired()])


