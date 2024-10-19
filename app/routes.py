from app import app
from app.forms import RegistrationForm

from flask import render_template, redirect


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(f"username: {form.username.data}\n"
                f"email: {form.email.data}\n"
                f"password: {form.password.data}")
        return redirect('/')

    return render_template('registration.html', form=form)