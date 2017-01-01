# coding=utf-8
# 初始化
from flask import Flask, render_template, redirect
from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap( app )

# 路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user( name ):
    # 字典
    users = {
        "gavin": 'YYC'
    }
    # 列表
    ls = ['gavin']
    return render_template('user.html', name=name, users=users, ls=ls)

# 处理 404 和 500 错误页面
@app.errorhandler( 404 )
def page_not_found( e ):
    # 重定向
    return redirect('http://baidu.com')

@app.errorhandler( 500 )
def internal_server_error( e ):
    return '500'

print app.url_map

manager = Manager( app )

if __name__ == '__main__':
    manager.run()
