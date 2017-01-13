# coding=utf-8

from flask import Flask

from config import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'

@app.route('/item/<id>/')
def item(id):
    return 'Item--{}'.format( id )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
