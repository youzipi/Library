# coding=utf-8
from flask import Flask, request
from flask.ext.restful import Api, Resource
from app import views

app = Flask(__name__)
api = Api(app)

todos = {}


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

# restful API配置
api.add_resource(todo, '/<string:todo_id>')
api.add_resource(views.q, '/q')

# 将函数映射到 URLs
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/index/', view_func=views.index)
# app.add_url_rule('/query/', view_func=views.query)
app.add_url_rule('/query/', methods=['POST'], view_func=views.query)
# app.add_url_rule('/result_temp/', view_func=views.result_temp)
app.add_url_rule('/result/', view_func=views.result)
app.secret_key = 'some_secret'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    # app.run()

