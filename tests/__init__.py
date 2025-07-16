import unittest
from audicus.models.order import Order
from audicus.models.subscription import Subscription
from audicus.models.db import (db)
from audicus.app import create_app



class TestConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_ECHO = False
    TESTING = True

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.client = cls.app.test_client()
        cls._ctx = cls.app.test_request_context()
        cls._ctx.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.session.begin(nested=False)

    def tearDown(self):
        db.session.rollback()
        db.session.close()
        self._ctx.pop()
