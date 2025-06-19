from sqlalchemy import Column, Integer, VARCHAR, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# making connection with database
db_url='sqlite:///quiz.db'
engine= create_engine(db_url)
Base=declarative_base()

# models for different tables
class User(Base):
    __tablename__= "user"

    id= Column(Integer, primary_key=True )
    username=Column(VARCHAR(20), unique=True, nullable=False)
    password=Column(VARCHAR(20), nullable=False)

    def _init_(self, username, password):
        self.username=username
        self.password=password


class userScore(Base):
    __tablename__= "userScore"
    
    id=Column(Integer, primary_key=True)
    username=Column(String(20), ForeignKey('user.username'))
    GK_questions=Column(Integer)
    computer_questions=Column(Integer)
    science_questions=Column(Integer)
    animals_questions=Column(Integer)
    sports_questions=Column(Integer)

class GK_questions(Base):
    __tablename__= "GK_questions"

    id=Column(Integer, nullable=False,primary_key=True)
    question=Column(String(400), nullable=False, )
    correct=Column(VARCHAR(100))
    incorrect1=Column(VARCHAR(100))
    incorrect2=Column(VARCHAR(100))
    incorrect3=Column(VARCHAR(100))
    
class sports_questions(Base):
    __tablename__= "sports_questions"

    id=Column(Integer, nullable=False,primary_key=True)
    question=Column(String(400), nullable=False)
    correct=Column(VARCHAR(100))
    incorrect1=Column(VARCHAR(100))
    incorrect2=Column(VARCHAR(100))
    incorrect3=Column(VARCHAR(100))


class animals_questions(Base):
    __tablename__= "animals_questions"

    id=Column(Integer, nullable=False,primary_key=True)
    question=Column(String(400), nullable=False)
    correct=Column(VARCHAR(100))
    incorrect1=Column(VARCHAR(100))
    incorrect2=Column(VARCHAR(100))
    incorrect3=Column(VARCHAR(100))

    
class science_questions(Base):
    __tablename__= "science_questions"

    id=Column(Integer, nullable=False,primary_key=True)
    question=Column(String(400), nullable=False)
    correct=Column(VARCHAR(100))
    incorrect1=Column(VARCHAR(100))
    incorrect2=Column(VARCHAR(100))
    incorrect3=Column(VARCHAR(100))

class computer_questions(Base):
    __tablename__= "computer_questions"

    id=Column(Integer, nullable=False,primary_key=True)
    question=Column(String(400), nullable=False)
    correct=Column(VARCHAR(100))
    incorrect1=Column(VARCHAR(100))
    incorrect2=Column(VARCHAR(100))
    incorrect3=Column(VARCHAR(100))


Base.metadata.create_all(engine)  # creating database with above tables