from __future__ import absolute_import, print_function, unicode_literals

import factory
import factory.fuzzy
from factory.alchemy import SQLAlchemyModelFactory

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD
from audicus.models.db import db
from audicus.models.subscription import Subscription


class SubscriptionFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Subscription
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    id = factory.Sequence(lambda n: n + 1)

    end_date = factory.fuzzy.FuzzyInteger(1, 1000)
    start_date = factory.fuzzy.FuzzyInteger(1, 1000)

    billing_interval = factory.fuzzy.FuzzyText(length=12)
    next_payment_date = factory.fuzzy.FuzzyInteger(1, 1000)
    recurring_amount = factory.fuzzy.FuzzyInteger(1, 1000)
    status = factory.fuzzy.FuzzyChoice([
        STATUS_ACTIVE,
        STATUS_CANCELLED,
        STATUS_ON_HOLD,
    ])
