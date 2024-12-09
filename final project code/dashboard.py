from flask import render_template, Blueprint, request, url_for, redirect, session, current_app
from sqlalchemy.orm import sessionmaker
from data import engine, GK_questions, computer_questions, animals_questions, science_questions,sports_questions
from login import get_name, logout

Session=sessionmaker(bind=engine)
SESSION=Session()

dashboard=Blueprint('dashboard', __name__)

tables=["GK_questions", "computer_questions", "animals_questions", "science_questions", "sports_questions"] # storing table names
Questions=[] # storing questions of given table
options=[] # storing options of given table
correct_answer=[] # storing correct answers

# displaying dashboard for quizes
@dashboard.route('/link', methods=['GET', 'POST'])
def index():
    secret_key=current_app.config['SECRET_KEY']
    name=get_name()

    # getting questions from desired table
    if name!=None:
        if request.method=='POST':
            session['question_table']=request.form['value']
            match session['question_table']:
                case "GK_questions":
                    get_GK_questions()
                    return redirect(url_for('quiz.quiz_index'))
                case "computer_questions":
                    get_comp_questions()
                    return redirect(url_for('quiz.quiz_index' ))
                case "science_questions":
                    get_science_questions()
                    return redirect(url_for('quiz.quiz_index' ))
                case "animals_questions":
                    get_animals_questions()
                    return redirect(url_for('quiz.quiz_index' ))
                case "sports_questions":
                    get_sports_questions()
                    return redirect(url_for('quiz.quiz_index' ))
                case _:
                    print("no data found")
        return render_template("dashboard.html",name=name)
    else:
        return redirect(url_for('login.login_user'))


# functions for getting questions from different tables
def get_GK_questions():
    question_table=session['question_table']
    if question_table=="GK_questions":
        questions=SESSION.query(GK_questions)
        if len(Questions)<20:
            for q in questions:
                Questions.append(q.question)
                correct_answer.append(q.correct)
                options.append(q.correct)
                options.append(q.incorrect1)
                options.append(q.incorrect2)
                options.append(q.incorrect3)
        else:
            Questions.clear()
            options.clear()
            correct_answer.clear()
            get_GK_questions()
    return question_table

def get_comp_questions():
    question_table=session['question_table']
    if question_table=="computer_questions":
        questions=SESSION.query(computer_questions)
        if len(Questions)<20:
            for q in questions:
                Questions.append(q.question)
                correct_answer.append(q.correct)
                options.append(q.correct)
                options.append(q.incorrect1)
                options.append(q.incorrect2)
                options.append(q.incorrect3)
        else:
            Questions.clear()
            options.clear()
            correct_answer.clear()
            get_comp_questions()
    return question_table


def get_science_questions():
    question_table=session['question_table']
    if question_table=="science_questions":
        questions=SESSION.query(science_questions)
        if len(Questions)<20:
            for q in questions:
                Questions.append(q.question)
                correct_answer.append(q.correct)
                options.append(q.correct)
                options.append(q.incorrect1)
                options.append(q.incorrect2)
                options.append(q.incorrect3)
        else:
            Questions.clear()
            options.clear()
            correct_answer.clear()
            get_science_questions()
    return question_table


def get_animals_questions():
    question_table=session['question_table']
    if question_table=="animals_questions":
        questions=SESSION.query(animals_questions)
        if len(Questions)<20:
            for q in questions:
                Questions.append(q.question)
                correct_answer.append(q.correct)
                options.append(q.correct)
                options.append(q.incorrect1)
                options.append(q.incorrect2)
                options.append(q.incorrect3)
        else:
            Questions.clear()
            options.clear()
            correct_answer.clear()
            get_animals_questions()
    return question_table


def get_sports_questions():
    question_table=session['question_table']
    if question_table=="sports_questions":
        questions=SESSION.query(sports_questions)
        if len(Questions)<20:
            for q in questions:
                Questions.append(q.question)
                correct_answer.append(q.correct)
                options.append(q.correct)
                options.append(q.incorrect1)
                options.append(q.incorrect2)
                options.append(q.incorrect3)
        else:
            Questions.clear()
            options.clear()
            correct_answer.clear()
            get_sports_questions()
    return question_table
        
# link for logout
@dashboard.route('/logout')
def log():
    logout()
    return redirect(url_for("login.login_user"))

# function for returning selected table
def score_table():
    table_name=session.get('question_table')
    return table_name