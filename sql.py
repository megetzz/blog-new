from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import ForeignKey
from blog_sql import *


app=Flask(__name__)
app.secret_key='sdasfasdf'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:258000@localhost/blogregister'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

class BlogReister(db.Model):
    __tablename__='blogregister'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(12),unique=True,nullable=False)
    password=db.Column(db.String(14),unique=True,nullable=False)
    verify_password =db.Column(db.String(14),unique=True,nullable=False)

    def __init__(self,username,password,verify_password):
        self.username=username
        self.password=password
        self.verify_password=verify_password

    def __repr__(self):
        return '%s'%self.username

db.create_all()