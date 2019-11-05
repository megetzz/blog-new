from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp


class RegisterForm(FlaskForm):
    name = StringField(
        label='用户名',
        # 验证用户名：用户名不能为空
        validators=[DataRequired()]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(),
            # 验证密码长度是否为6～8之间，如果不是，报错
            Length(8, 16, message='密码格式错误!')
        ]
    )

    repassword = PasswordField(
        label='确认密码',
        validators=[
            DataRequired(),
            # 验证当前表单输入的内容和password这个表单输入的内容是否一致，如果不一致，报错
            EqualTo('password', message='密码不一致!')
        ]
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(),
            # 验证当前表单输入的内容是否为一个邮箱地址，如果不是，报错
            Email(message='邮箱格式错误!')
        ]
    )

    phone = StringField(
        label='手机号码',
        validators=[
            DataRequired(),
            # 验证当前表单输入的电话号码是否符合首位为1，由11位数字组成的正则表达式，如果不是，报错
            Regexp(r'1\d{10}', message='手机号码格式错误!')
        ]

    )

    # RadioField也可以实现单选按钮，但是不美观，推荐用 SelectField
    gender = SelectField(
        label='性别',
        coerce=int,
        choices=[(1, '男'), (2, '女')]
    )

    # 多选按钮
    tech = SelectMultipleField(
        label='擅长领域',
        coerce=int,
        choices=[(1, 'python'), (2, 'linux'), (3, 'java'), (4, 'php'), (5, 'ruby'), (6, 'c++')]
    )

    submit = SubmitField(label='注册')