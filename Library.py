# coding=utf-8
from flask import Flask, request
from flask.ext.restful import Api, Resource
from app import views


class todo(Resource):
    def get(self, todo_id):
        if todo_id in todos.keys():
            result = {todo_id: todos[todo_id]}
        else:
            result = {"msg": "not found"}
        return result, 201, {'Etag': 'some-opaque-string'}

    def post(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

app = Flask(__name__)
api = Api(prefix='/api/v1')
# api = Api(app)
# Flask-Restful, like all properly implemented Flask extensions, supports two methods of registering itself:
# With the app at instantiation (as you are trying to do with Api(current_app))
# At a later point using api.init_app(app)
todos = {}


# restful API配置
api.add_resource(todo, '/<string:todo_id>')
api.add_resource(views.q, '/q')
api.add_resource(views.d, '/d/<string:id>')
api.add_resource(views.api_detail, '/detail/<string:id>')

# 将函数映射到 URLs
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/index/', view_func=views.index)
app.add_url_rule('/query/', methods=['POST'], view_func=views.query)
app.add_url_rule('/detail/<string:id>', methods=['GET'], view_func=views.detail)
app.add_url_rule('/book-detail', methods=['GET'], view_func=views.book_detail)
app.add_url_rule('/result/', view_func=views.result)
app.secret_key = 'some_secret'

if __name__ == '__main__':
    api.init_app(app)
    app.debug = True
    # app.run(host='0.0.0.0', port=8080)
    app.run()

