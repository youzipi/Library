# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'

import re,sys
from bs4 import UnicodeDammit
reload(sys)
sys.setdefaultencoding('utf-8')
# 将正则表达式编译成Pattern对象
pattern = re.compile(u'TP[\d./]*')

str = '责任者:Liang, Y. Daniel. 索书号:TP312PY/W3 出版信息:China Machine Press,2013.'
print str
match = re.search(pattern, str)
t = re.search(u'出版信息:(?P<pub>.*)'.encode('utf-8'), str)
if t:
    print t.group('pub')
if match:
    print match.group()




#dammit = UnicodeDammit(str)
#print(dammit.unicode_markup)
#print dammit.original_encoding#utf-8