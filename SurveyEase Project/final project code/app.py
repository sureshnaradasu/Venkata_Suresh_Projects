from flask import Flask
from data import engine
from sqlalchemy.orm import sessionmaker
from register import register
from login import login
from dashboard import dashboard
from quiz import quiz
from score import score


app = Flask(__name__)
app.config['SECRET_KEY']='super_secret_key'
Session= sessionmaker(bind=engine)
session=Session()

# page for registration
app.register_blueprint(register)

# page for login
app.register_blueprint(login)

# page for dashboard
app.register_blueprint(dashboard)

# page for quiz index
app.register_blueprint(quiz)

# page for previous results of user
app.register_blueprint(score)
    
if __name__=='__main__':
    app.run(debug=True)