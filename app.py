from flask import Flask, render_template, url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@127.0.0.1/test_24'

db.init_app(app)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(155), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)


@app.route('/')
def index():
    questions = Question.query.all()
    random.shuffle(questions)

    for q in questions:
        random.shuffle(q.answers)
    
    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    questions = Question.query.all()
    total = len(questions)

    for q in questions:
        answer_id = request.form.get(f'q{q.id}')
        if answer_id:
            correct = Answer.query.filter_by(question_id=q.id, is_correct=True).first()
            if correct and answer_id == str(correct.id):
                score += 1

    incorrect = total - score
    score_percentage = (score / total) * 100
    return render_template('result.html', correct=score, incorrect=incorrect, score=round(score_percentage, 2))



if __name__ == '__main__':
    app.run(debug=True)