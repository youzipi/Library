# coding=utf-8
from flask import Flask
from app import views

app = Flask(__name__)

# 将函数映射到 URLs
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/index/', view_func=views.index)
#app.add_url_rule('/query/', view_func=views.query)
app.add_url_rule('/query/', methods=['POST'], view_func=views.query)
app.add_url_rule('/q/', methods=['POST'], view_func=views.q)
# app.add_url_rule('/result_temp/', view_func=views.result_temp)
app.add_url_rule('/result/', view_func=views.result)
app.secret_key = 'some_secret'


if __name__ == '__main__':
    app.debug = True
    app.run()

