from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, Optional
from directory.models import User
from flask_wtf.file import FileField, FileAllowed, FileRequired

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_validate):
        duplicate = User.query.filter_by(username=username_to_validate.data).first()
        if duplicate:
            raise ValidationError("Username Exists. Please try a different one")
    
    def validate_email_address(self, email_to_validate):
        duplicate = User.query.filter_by(email_address=email_to_validate.data).first()
        if duplicate:
            raise ValidationError("Email Address Exists. Please try a different one")

        
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()] )
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class ProblemForm(FlaskForm):
    title = StringField(label='Problem Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField(label="Problem Description", validators=[DataRequired()])
    sample_input = TextAreaField(label="Sample Input", validators=[DataRequired()])
    sample_output = TextAreaField(label="Sample Output", validators=[DataRequired()])
    submit = SubmitField(label="Add Problem")

class SolveProblemForm(FlaskForm):
    def validate_user_output(self, user_output):
        if user_output.data:
            user_output.data = user_output.data.strip()
        if not user_output.data and not self.code_file.data:
            return False     
        return True

    user_output = TextAreaField(label="Enter Output", validators=[Optional()])
    code_file = FileField(label="Upload Python File",
                          validators=[
                              Optional(),
                              FileAllowed(['py'], "Only .py files are allowed!")
                          ])
    submit = SubmitField(label="Submit Solution")
   