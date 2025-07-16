from __future__ import absolute_import, print_function, unicode_literals

from flask import Flask, request
from flask_restful import Api, Resource

from audicus.resources.orders_by_sub import OrdersBySub


app = Flask(__name__)
api = Api(app)


class ToDo(Resource):
    def get(self):
        return {"key": "value"}

api.add_resource(ToDo, "/todo")
api.add_resource(OrdersBySub, "/sub/<int:sub_id>/order/<int:order_id>")

if __name__ == "__main__":
    app.run(debug=True)
