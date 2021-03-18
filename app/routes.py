from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Dari"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Restore The Snyder Verse'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Justice League Snyder Cut is awesome!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)