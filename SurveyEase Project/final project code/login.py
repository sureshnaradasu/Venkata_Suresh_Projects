from flask import render_template, redirect, url_for, request, Blueprint, current_app, session
from data import engine, User
from sqlalchemy.orm import sessionmaker

login=Blueprint('login', __name__)

Session= sessionmaker(bind=engine)
SESSION=Session()

# displaying login page
@login.route('/login', methods=['GET', 'POST'])
def login_user():
    secret_key=current_app.config['SECRET_KEY']
    if request.method=='POST':
        username=request.form.get('user')
        password=request.form.get('password')
        data=SESSION.query(User)

        # checking data in database
        for i in data:
            if i.username==username and i.password==password:
                session['name']=i.username
                name=session['name']
                session['loggedin']=True
                return redirect(url_for('dashboard.index', name=name))
        else:
            msg="User not found"
            return render_template('login.html', msg=msg)
    return render_template('login.html')

# function for storing name of user
def get_name():
    name=session.get('name')
    return name

# function for logout
def logout():
    return session.pop('loggedin', None), session.pop('name', None)