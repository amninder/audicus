from __future__ import absolute_import, print_function, unicode_literals

import factory
import factory.fuzzy
from factory.alchemy import SQLAlchemyModelFactory
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.models.db import db
from audicus.models.order import Order


class OrderFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Order
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    id = factory.Sequence(lambda n: n + 1)

    closedate = factory.fuzzy.FuzzyInteger(1, 1000)
    total_order_value = factory.fuzzy.FuzzyInteger(1, 1000)

    subscription = factory.SubFactory(SubscriptionFactory)
