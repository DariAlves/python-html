from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dari'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Snyder Cut movie was so cool!'
        },
        {
            'author': {'username': 'DC'},
            'body': 'UFC sets Chandler vs. Oliveira fight for lightweight title'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)