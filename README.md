# Library

使用flask框架开发的南信大图书馆查询系统
##主要实现功能
- 按书名关键字查询图书
- 解析图书馆提供的rss，提取图书信息（书名，作者，ISBN，馆藏地）
- 按照图书的`marc_no`访问图书馆相应页面，返回图书详细信息


##restful 接口
提供给Android作业用

GET：
- /api/v1/q?keyword=python 按关键字返回
- /api/v1/d/0000515353 返回图书信息(html格式)
- /api/v1/detail/0000515353 返回图书信息(json格式)


#todo
- ~~修改为restful服务~~
- 接入豆瓣书评
- 分页
- 实现登陆功能（验证码一直过不去。。。）
