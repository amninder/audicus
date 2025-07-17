from __future__ import absolute_import, print_function, unicode_literals

from dotenv import dotenv_values
from flask import Flask
from flask_restful import Api

from audicus.models.db import db
from audicus.resources.orders_by_sub import (
    AllSubscriptions,
    GetSubscriptions,
    OrdersBySub,
)


config = dotenv_values(".env")


class Config:
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI",
                                         "sqlite://")
    SQLALCHEMY_ECHO = False
    TESTING = True
    FLASK_RUN_PORT = int(config.get("FLASK_RUN_PORT", "6000"))
    FLASK_RUN_HOST = config.get("FLASK_RUN_HOST", "0.0.0.0")


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)

    api.add_resource(OrdersBySub, "/sub/<int:sub_id>/order/<int:order_id>")
    api.add_resource(GetSubscriptions, "/subscriptions/")
    api.add_resource(AllSubscriptions, "/")
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app(Config)
    app.run(debug=True, port=6000, host="0.0.0.0")
