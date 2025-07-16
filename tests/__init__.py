import unittest
from audicus.models.order import Order
from audicus.models.subscription import Subscription
from audicus.models.db import (db)
from audicus.app import app


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        self.app.config["SQLALCHEMY_ECHO"] = False
        self.app.config["TESTING"] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.db = db
        self.db.init_app(self.app)
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        self.db.drop_all()
        self.app_context.pop()
