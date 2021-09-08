from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fanpeng'}
    posts = [
        {
        'author': {'username': 'Mia'},
        'body': 'Beautiful day in Canberra!'
        },
        {
        'author': {'username': 'Coco'},
        'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
