from flask_bootstrap import Bootstrap
from flask import Flask,render_template,escape,flash,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
from blog_sql import *
from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField,TextAreaField
from wtforms.validators import Required
from login_blog import *

app=Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key='sdasfasdf'

@app.route('/')
def login():
    return 'hello world'


app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:258000@localhost/blogproject"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

@app.route('/blog_index')
def show_all():
    blog_showall=Blog.query.all()
    print(blog_showall)
    return render_template('blog_index.html',blog_showall=blog_showall)#wenzi=wenzi





@app.route('/blogadd',methods=['GET','POST'])
def blogadd():
    if request.method=='GET':
        return render_template('blog_add.html')
    elif request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        bk=Blog(title,author,content)
        db.session.add(bk)
        db.session.commit()
        flash('提交成功')
        # fanhui = request.form['fanhui']
        return render_template('blog_add.html')
        # return redirect(url_for('show_all'))



@app.route('/blogdel/<id>')
def blogdel(id):
   bianhao=db.session.query(Blog).filter_by(id=id).first()
   print(bianhao)
   if bianhao:
       try:
           # Blog.query.filter_by(id=id).delete()
           db.session.delete(bianhao)
           db.session.commit()
           return redirect(url_for('show_all'))
       except:
           '错误'
   else:
       return '没有此id'

@app.route('/query_blog' ,methods=['GET','POST'])
def QueryBlog():
    if request.method=='GET':
        return render_template('query_blog.html')
    else:
        title=request.form['title']
        print(title)
        if title:
            res=db.session.query(Blog).filter_by(title=title).first()
            db.session.commit()
            flash('查找成功')
            return  render_template('query_blog.html',res=res)
        else:
            return '没有此标题'


if __name__ == '__main__':
    app.run(debug=True)


