# coding=utf-8
from flask import Flask
from flask import render_template, request, url_for, flash, redirect
from flask_wtf import Form
from forms import searchForm
from main.actions import query_by_keyword

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/query/', methods=['POST'])
def query():
    keyword = request.form['keyword']
    print keyword
    # url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title="+keyword
    url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title="+keyword
    result = query_by_keyword(url)
    return render_template('result.html', result=result)
    #return "中文".encode('utf-8').decode('gbk')

if __name__ == '__main__':
    app.debug = True
    app.run()

