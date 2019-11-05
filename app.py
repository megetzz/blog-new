from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)



@app.route('/index')
def hello_world():
    return render_template('blog_index.html')


if __name__ == '__main__':
    app.run(debug=True)
