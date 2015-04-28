# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
from flask import render_template, request, url_for, flash, redirect, session,g,Response
from app.actions import query_by_keyword
import json


def index():
    return render_template('index.html')


# 查询方法，返回result.html
def query():
    keyword = request.form['keyword']
    print request
    print keyword
    url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title=" + keyword
    # url = "http://127.0.0.1:5000/python.xml"
    result = query_by_keyword(url)
    #if request.form:
    # result = [{'1': 'ee'}, {'1': '中文'.decode('utf-8')}]
    session['result'] = result
    print result
    # g['result'] = result
    # print result[0]
    # return redirect(url_for('result_temp'))
    response = Response(response=result[0], status=200, mimetype="application/json")
    print "response.status=", response.status
    print "response.response=", response.response
    #print str(response.data)
    return redirect(url_for('result'))
    #return render_template('result.html', result=session.get('result'))
    # return render_template('result.html', result=result)
    # return redirect('result.html')
    #return "中文".encode('utf-8').decode('gbk')
    
def q():
    keyword = request.form['keyword']
    print keyword
    url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title=" + keyword
    # url = "http://127.0.0.1:5000/python.xml"
    result = query_by_keyword(url)
    return result
    #return render_template('result.html', result=session.get('result'))
    # return render_template('result.html', result=result)
    # return redirect('result.html')
    #return "中文".encode('utf-8').decode('gbk')


def send_ok_json(data=None):
    if not data:
        data = {}
    ok_json = {'ok':True,'reason':'','data':data}
    return json.dumps(ok_json)


def q():
    keyword = request.form['keyword']
    print keyword
    url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title=" + keyword
    # url = "http://127.0.0.1:5000/python.xml"
    result = query_by_keyword(url)
    ret = '%s**%s' %(keyword+keyword, 'post')
    response = Response(response=result[0], status=200, mimetype="application/json")
    print "response=", response.response
    return response


def result_temp():
    # print g['result']
    return redirect('result')


def result():
        print session['result']
        return render_template('result.html', result=session.get('result'))  #, result=session.get('result'))

