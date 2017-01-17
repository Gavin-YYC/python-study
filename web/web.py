# coding=utf-8
from flask import Flask, request, session
from flask import make_response, redirect, render_template
from flask import url_for, flash

# 通过脚本进行管理
from flask_script import Manager

# 使用bootstrap
from flask_bootstrap import Bootstrap

# 使用表单
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager( app )
bootstrap = Bootstrap( app )

# 创建一个表单
class NameForm( FlaskForm ):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

# 多种请求方式
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # 获取请求头
    user_agent = request.headers.get('User-Agent')
    # 设置响应体
    response = make_response( user_agent )
    # 设置cookie
    response.set_cookie('hahaha', '111')
    return response

# 参数路由
@app.route('/item/<id>/')
def item(id):
    return 'Item--{}'.format( id )

# 模板渲染
# flask会自动寻找templates文件夹
@app.route('/user', methods=['GET', 'POST'])
def user():
    form = NameForm()
    # 用户是否提交表单
    if form.validate_on_submit():
        old_name = session.get('name')
        # 异常提醒：flash
        if old_name is not None and old_name != form.name.data:
            print 'haha'
            flash('您输入的名字不相等')
        # 提交表单后，name重新赋值
        # 先保存到session中一份
        name = form.name.data
        session['name'] = name
        session['users'].append( name )
        # 重定向，防止第二次提交表单
        return redirect(url_for('user'))
    return render_template(
        'user.html',
        name=session.get('name'),
        users=session.get('users'),
        form=NameForm()
    )

# 重定向
@app.route('/redirect')
def redi():
    return redirect('/')

if __name__ == '__main__':
    manager.run()
