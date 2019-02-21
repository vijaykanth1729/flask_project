#auth/views.py
from flask import flash,redirect,render_template,url_for,request
from flask_login import login_required,login_user,logout_user
from . import auth
from . forms import RegistrationForm,LoginForm
from .. import db
from ..models import Employee


@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        employee=Employee(email=form.email.data,
                          username=form.username.data,
                          first_name=form.first_name.data,
                          last_name=form.last_name.data,
                          password=form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash("You are successfully registered to our site!!, Now You can login")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form,title='Register')

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        employee=Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            login_user(employee)
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))

        else:

            return f"<h2>Invalid login details,Please try Again later!!</h2>"

    else:


        return render_template('auth/login.html',form=form,title='login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You Logged out Successfully!")
    return redirect(url_for('auth.login'))
