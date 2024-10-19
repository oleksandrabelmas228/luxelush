from wtforms import Form, validators, StringField, FloatField, PasswordField, EmailField, SubmitField
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()], render_kw={"class": "form-control", "placeholder": "Enter username"})
    email = EmailField('Email', [validators.Length(min=6, max=50), validators.Email(check_deliverability=True), validators.DataRequired()], render_kw={"class": "form-control", "placeholder": "Email address"})
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6, max=20)], render_kw={"class": "form-control", "placeholder": "Create password"})
    submit = SubmitField("Sign up", render_kw={"class": "btn btn-primary btn-block"})