from __future__ import absolute_import, print_function, unicode_literals

from flask import Flask, request
from flask_restful import Api, Resource

from audicus.resources.orders_by_sub import GetSubscriptions, OrdersBySub
from audicus.models.db import db


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)

    api.add_resource(OrdersBySub, "/sub/<int:sub_id>/order/<int:order_id>")
    api.add_resource(GetSubscriptions, "/subscriptions/")
    db.init_app(app)

    return app
