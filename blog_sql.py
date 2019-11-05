from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import not_



app=Flask(__name__)
app.secret_key='sdasfasdf'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:258000@localhost/blogproject'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)


class Blog(db.Model):
    __tablename__ = 'blogboke'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(20), unique=True, nullable=False)
    # text=db.Column(db.String(200),unique=True,nullable=False)
    content=db.Column(db.String(500),unique=True,nullable=False)

    def __init__(self,title, author,content):
        self.title = title
        self.author = author
        self.content=content

    def __repr__(self):
        return  '%r'%self.title

db.create_all()


# bk1=blog('静夜思','李白','床前明月光,疑是地上霜.举头望明月,低头思故乡')
# db.session.add(bk1)
# db.session.commit()

# bk2=blog('大战拖延症','Priest','逆来顺受、随波逐流、浑浑噩噩地也是一辈子，一直卡着自己的脖子往上爬，摔下来痛苦一场，再咬牙继续往上爬，也算一辈子。结果怎么样，谁也不能未卜先知。前者觉得后者累、自讨苦吃，后者觉得前者糊里糊涂、可怜。各有各的活法，谁也不能说谁错，可是人得挑一种对得起自己的活法——所谓对得起自己，就是甘当废柴也好，逆水行舟也好，都得坦坦荡荡。愿意活得轻松自在的，看见别人香车宝马、功成名就，得能没有一点艳羡之心，知道自己是怎么回事，所以无论遇到什么事，也绝不会不甘心。至于那些知道自己一定会不甘心的，最好就马上洗干净脸，该干什么干什么去。任何时候，都不会后悔，不会焦虑，不会讨厌自己，不会觉得自己浪费了生命，那就是对得起自己的活法')
# db.session.add(bk2)
# db.session.commit()

# bk3=blog('小雅·采薇', '佚名' , """采薇采薇，薇亦作止。曰归曰归，岁亦莫止。靡室靡家，玁狁之故。不遑启居，玁狁之故。
#
# 采薇采薇，薇亦柔止。曰归曰归，心亦忧止。忧心烈烈，载饥载渴。我戍未定，靡使归聘。
#
# 采薇采薇，薇亦刚止。曰归曰归，岁亦阳止。王事靡盬，不遑启处。忧心孔疚，我行不来。
#
# 彼尔维何？维常之华。彼路斯何？君子之车。戎车既驾，四牡业业。岂敢定居？一月三捷。
#
# 驾彼四牡，四牡骙骙。君子所依，小人所腓。四牡翼翼，象弭鱼服。岂不日戒，玁狁孔棘。
#
# 昔我往矣，杨柳依依。今我来思，雨雪霏霏。行道迟迟，载渴载饥。我心伤悲，莫知我哀""")
# db.session.add(bk3)
# db.session.commit()
# xiaoxi=[]

# blog_showall=db.session.query(Blog).all()
# print(blog_showall)
# xiaoxi.append(blog_showall)
#
# bk4=Blog('雨巷','戴望舒',"""撑着油纸伞，独自
# 彷徨在悠长、悠长
# 又寂寥的雨巷
# 我希望逢着
# 一个丁香一样地
# 结着愁怨的姑娘
# 她是有
# 丁香一样的颜色
# 丁香一样的芬芳
# 丁香一样的忧愁
# 在雨中哀怨
# 哀怨又彷徨
# 她彷徨在这寂寥的雨巷
# 撑着油纸伞
# 像我一样
# 像我一样地
# 默默彳亍着
# 冷漠、凄清，又惆怅
# 她默默地走近
# 走近，又投出
# 太息一般的眼光
# 她飘过
# 像梦一般地
# 像梦一般地凄婉迷茫
# 像梦中飘过
# 一枝丁香地
# 我身旁飘过这女郎
# 她静默地远了、远了
# 到了颓圮的篱墙
# 走尽这雨巷
# 在雨的哀曲里
# 消了她的颜色
# 散了她的芬芳
# 消散了，甚至她的
# 太息般的眼光
# 丁香般的惆怅
# 撑着油纸伞，独自
# 彷徨在悠长、悠长
# 又寂寥的雨巷
# 我希望飘过
# 一个丁香一样地
# 结着愁怨的姑娘""")
# db.session.add(bk4)
# db.session.commit()


