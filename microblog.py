from flask import Flask

app = Flask("microblog")

@app.route("/")
def index():
    return "Olá Mundo"

app.run()