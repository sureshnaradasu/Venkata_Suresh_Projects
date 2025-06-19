from flask import render_template, Blueprint, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from data import engine, userScore
from login import get_name

Session=sessionmaker(bind=engine)
SESSION=Session()

score=Blueprint("score", __name__)

score_check=[]  # storing marks
column_name=["General Knowledge", "Sports", "Computer", "Science And Nature", "Animals"] # storing column names

# getting previous marks form database
def storing_score(user):
    marks=SESSION.query(userScore).filter_by(username=user).first()
    gk_score=marks.GK_questions
    sports_score=marks.sports_questions
    comp_score=marks.computer_questions
    science_score=marks.science_questions
    animal_score=marks.animals_questions
    score_check.append(gk_score)
    score_check.append(sports_score)
    score_check.append(comp_score)
    score_check.append(science_score)
    score_check.append(animal_score)
    
    # checking if quiz is submitted or not
    for i in score_check:
        if i==None:
            index=score_check.index(i)
            score_check[index]="Quiz not Submitted"
    return score_check, column_name

# re-rendering previous results
@score.route('/re_render', methods=['GET', 'POST'])
def clearing():
    if request.method=='POST':
        score_check.clear()
    return redirect(url_for('score.previous_result'))

# displaying results of previous quizes
@score.route('/previous_results')
def previous_result():
    user= get_name()
    storing_score(user)
    length=len(score_check)
    return render_template('previous_results.html',user=user, score_check=score_check, column_name=column_name, length=length)
    
