# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
import re
from flask import render_template, request, url_for, flash, redirect, session, g, Response
import requests
from app.actions import query_by_keyword, get_book_info
import json
from flask.ext.restful import Resource, reqparse

# request.json
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
    # if request.form:
    # result = [{'1': 'ee'}, {'1': '中文'.decode('utf-8')}]
    session['result'] = result
    print result
    # g['result'] = result
    # print result[0]
    # return redirect(url_for('result_temp'))
    response = Response(response=str(result[0]), status=200, mimetype="application/json")
    print "response.status=", response.status
    print "response.response=", response.response
    # print str(response.data)
    return redirect(url_for('result'))
    #return render_template('result.html', result=session.get('result'))
    # return render_template('result.html', result=result)
    # return redirect('result.html')
    #return "中文".encode('utf-8').decode('gbk')

# Request Parsing
parser = reqparse.RequestParser()
parser_book = reqparse.RequestParser()
parser.add_argument('keyword', type=str, required=True, help="keyword cannot be null")
parser_book.add_argument('marc_no', type=str, required=True, help="marc_no cannot be null")


class q(Resource):
    def get(self):
        args = parser.parse_args()
        keyword = args['keyword']
        url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title=" + keyword

        book_list = query_by_keyword(url)
        response = Response(response=json.dumps(book_list), status=200, mimetype="application/json")
        # return json.dumps(book_list),
        return response
        # return result  #不以index排序


def send_ok_json(data=None):
    if not data:
        data = {}
    ok_json = {'ok': True, 'reason': '', 'data': data}
    return json.dumps(ok_json)


def result_temp():
    # print g['result']
    return redirect('result')


def result():
    print session['result']
    return render_template('result.html', result=session.get('result'))  # , result=session.get('result'))


class d(Resource):
    def get(self,id):
        # args = parser_book.parse_args()
        # url = args['marc_no']
        # book = get_book_info(url)
        book = get_book_info(id)
        session['book'] = book
        print book
        response = Response(response=str(book), status=200)
        return response

class api_detail(Resource):
    def get(self,id):
        data = {}
        r = requests.get('http://lib2.nuist.edu.cn/opac/item.php?marc_no=%s' % id)
        match0 = re.compile(r'<dt>(.*)</dt>')
        match1 = re.compile(r'<dd>(.*)</dd>')
        match2 = re.compile(r'<td  width="25%" title="(.*)"><img src="../tpl/images/place_marker.gif" />(.*)</td>')
        match3 = re.compile(r'<td  width="20%" >(.*)</td>')

        dt = re.findall(match0, r.content)
        dd = re.findall(match1, r.content)
        address = re.findall(match2, r.content)
        flag = re.findall(match3, r.content)
        data['status'] = True
        data['dt'] = dt
        data['dd'] = dd
        data['address'] = address
        data['flag'] = flag
        print data
        response = Response(response=json.dumps(data), status=200, mimetype="application/json")
        return response


def detail(id):
    print id
    data = {}
    r = requests.get('http://lib2.nuist.edu.cn/opac/item.php?marc_no=%s' % id)
    match0 = re.compile(r'<dt>(.*)</dt>')
    match1 = re.compile(r'<dd>(.*)</dd>')
    match2 = re.compile(r'<td  width="25%" title="(.*)"><img src="../tpl/images/place_marker.gif" />(.*)</td>')
    match3 = re.compile(r'<td  width="20%" >(.*)</td>')

    dt = re.findall(match0, r.content)
    dd = re.findall(match1, r.content)
    address = re.findall(match2, r.content)
    flag = re.findall(match3, r.content)
    data['status'] = True
    data['dt'] = dt
    data['dd'] = dd
    data['address'] = address
    data['flag'] = flag
    print data
    # response = Response(content=json.dumps(data), mimetype='application/json')
    response = Response(response=json.dumps(data), status=200, mimetype="application/json")
    return response



def book_detail():
    return render_template('book-detail.html')