from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app=Flask(__name__)
Bootstrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template('0.html')