# Library

使用flask框架开发的南信大图书馆查询系统

解析图书馆提供的rss，提取图书信息（书名，作者，ISBN，馆藏地）



restful 接口
GET：
- /q?keyword=python 按关键字返回
- /d?marc_no=0000515353 返回图书信息（html格式）
- /detail/0000515353 返回图书信息（json格式） 待完善

目前只实现了关键字查询
#todo
- 修改为restful服务
- 接入豆瓣书评
- 实现登陆功能（验证码一直过不去。。。）
