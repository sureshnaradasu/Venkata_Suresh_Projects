from flask import render_template, Blueprint, request, session, redirect, url_for
from sqlalchemy.orm import sessionmaker
from data import engine, userScore
from dashboard import Questions, options, correct_answer, score_table
from login import get_name
import random

Session=sessionmaker(bind=engine)
SESSION=Session()

quiz=Blueprint("quiz", __name__)

paired_options=[]
Questions_correct=[]

# function for shuffling options
def shuffle():
    # making pair of all options according to the nummber of options i.e 4          
        for i in range(0,len(options),4):
            paired_options.append(options[i:i+4])

        # shuffling options  
        for mcq in paired_options:
            random.shuffle(mcq)

# display questions and options
@quiz.route('/quiz', methods=['GET', 'POST'])
def quiz_index():
    length=len(Questions)
    shuffle()
    return render_template("index.html", Questions=Questions, paired_options=paired_options, length=length)

# submitting and showing results
@quiz.route('/result', methods=['GET', 'POST'])
def result():
    session['correct']=0
    correct=session['correct']
    selected_answers=[]
    length=len(Questions)

    # counting correct answers
    for i in range(0,length):
        select=("option"+str(i)) 
        selected_answers.append(select)
        selection=request.form.get(selected_answers[i])

        if selection==correct_answer[i]:
            correct=correct+1

    count(correct)
    for i in Questions:
        Questions_correct.append(i)

    options.clear()
    paired_options.clear()
    Questions.clear()
    return render_template('result.html', length=length, correct=correct)

# function for saving number of previous correct answers in database
def count(correct):  
    column=score_table()
    user=get_name()
    existing_user=SESSION.query(userScore).filter_by(username=user).first()
    if existing_user is not None:
        setattr(existing_user, column, correct)
        SESSION.commit()
    else:
         return "no data found"

# link for displaying correct answers
@quiz.route('/correct', methods=['GET', 'POST'])
def correct():
    length=len(Questions_correct)
    return render_template("correct.html", Questions_correct=Questions_correct, correct_answer=correct_answer, length=length)

# for clearing lists
@quiz.route('/clear', methods=['GET', 'POST'])
def clear_lists():
    if request.method=='POST':
        Questions_correct.clear()
        correct_answer.clear()
        return redirect(url_for('dashboard.index'))