from flask_wtf import Form,FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField,StringField,PasswordField
from flask import Flask,request,render_template,redirect,url_for,flash
from sql import *


app = Flask(__name__)
app.secret_key='sdasfasdf'


# class Blogzhuce(Form):
#     username = StringField('username', validators=[DataRequired()])
#     password = PasswordField('password', validators=[DataRequired()])
#
#     submit = SubmitField('登录')



class Myform(Form):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('登录')
    verify_password = PasswordField('verify_password', validators=[DataRequired()])
    # def __init__(self,username,password):
    #     self.username = username
    #     self.password = password
    #
    # def __repr__(self):
    #     return "{'User':%s,'Pwd':%s}"% self.username,self.password
@app.route('/blogregister' ,methods=['GET','POST'])
def zhuce():
    form=Myform()
    if request.method == "GET" :
        print(request.method)
        return render_template('blogregister.html',form=form)
    else:
        username = request.form['username']
        password = request.form['password']
        verify_password=request.form['verify_password']
        yonghuzhuce = BlogReister(username, password, verify_password)
        if password==verify_password:
            db.session.add(yonghuzhuce)
            db.session.commit()
            flash('注册成功')
            return render_template('bloglogin.html')


@app.route('/bloglogin',methods = ['GET','POST'])
def flask_wtf1():
    form=Myform()
    if request.method == "GET" :
        print(request.method)
        return render_template('bloglogin.html',form=form)
    else:
        username = request.form['username']
        password = request.form['password']
        sqluser = db.session.query(BlogReister).filter_by(username=username).first()
        # print(sqluser)
        sqlpwd =db.session.query(BlogReister).filter_by(password=password).first()
        # print(sqlpwd)
        if username == sqluser and password == sqlpwd:
            return render_template('blog_index.html')
        else:
            return redirect(url_for('flask_wtf1'))







if __name__ == '__main__':
    app.run(debug=True)