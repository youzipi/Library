# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'

import os
import sys
import urllib2, urllib, re
from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding('utf-8')


def get_info(book, description, item):
    try:
        pattern_link = re.compile(u'(http://[\S]*)(?=<)'.encode('utf-8'))
        pattern_id = re.compile(u'(?<=索书号:)([T]?P[\S]*)'.encode('utf-8'))
        pattern_pub = re.compile(u'(?<=出版信息:)(.*)'.encode('utf-8'))

        link = re.search(pattern_link, str(item))
        book_id = re.search(pattern_id, description)
        pub = re.search(pattern_pub, description)
        #z = 1
        #print(book_id)
        #print(pub)
        #print(z)
        book['link'] = link.group().encode('utf-8')
        book['id'] = book_id.group().encode('utf-8')  # if book_id else ""
        book['pub'] = pub.group().encode('utf-8')  # if pub else "
        del book_id
        del pub
    except AttributeError, Argument:
        print"Error=" + str(Argument)
        #print(book_id)
        #print(pub)
        print"description=" + (description).encode('utf-8')
        # get_info(book, description, item)


def query_by_keyword(url):
    # soup = BeautifulSoup(xml, from_encoding='GB18030')
    xml = urllib2.urlopen(url).read()
    soup = BeautifulSoup(xml)
    items = soup.channel.find_all('item')  # 每个item为一本书
    # result_size = len(items)
    book_list = []
    for item in items:
        title_node = str(item.title.string)
        index = title_node.split('.')[0]
        title = title_node.split('.')[1]
        description = str(item.description.string)


        book = {}
        book['index'] = index
        book['title'] = title
        # book['id'] =book_id.group('id')

        get_info(book, description, item)
        # print (book['title']).encode('utf-8')
        book_list.insert(int(book['index']) - 1, book)
        if int(book['index']) >= 50:
            #print index
            break
    # print len(book_list)
    # print book_list
    return book_list


if __name__ == '__main__':
    keyword = "python"
    url = "http://lib2.nuist.edu.cn/opac/search_rss.php?title=" + keyword
    query_by_keyword(url)