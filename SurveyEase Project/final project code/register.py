from sqlalchemy.orm import sessionmaker
from flask import request, url_for, redirect, render_template, Blueprint
from data import engine, User, userScore

Session=sessionmaker(bind=engine)
session=Session()

register=Blueprint("register", __name__)

# displaying registration form
@register.route('/', methods=['GET', 'POST'])
def reg():
    if request.method=='POST':
        user_name=request.form.get("uname")
        password=request.form.get("password")
        exist= session.query(User).filter(User.username==user_name).count() # checking existing users
        if exist>0:
            massage="Username already exists"
            return render_template("register.html", massage=massage)          
        else:
            user_register=User(username=user_name, password=password)
            user_register_score= userScore(username=user_name)
            session.add(user_register)
            session.add(user_register_score)
            session.commit()
            return redirect(url_for('login.login_user'))
    return render_template('register.html')
