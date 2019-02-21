from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,ValidationError
from wtforms.validators import Email,DataRequired,EqualTo
from .. models import Employee
#from . import views
class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[Email(),DataRequired()])
    username=StringField('UserName',validators=[DataRequired()])
    first_name=StringField('First_Name',validators=[DataRequired()])
    last_name=StringField('Last_Name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password=PasswordField('Confirm_password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validate_email(self,field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already taken!!')
    def validate_username(self,field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Please Choose Different UserName!!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

