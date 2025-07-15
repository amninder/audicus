import factory
from factory.alchemy import SQLAlchemyModelFactory
import factory.fuzzy
from audicus.models.order import Order
from tests import session
from tests.factories.subscription_factory import SubscriptionFactory


class OrderFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Order
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "flush"

    id = factory.Sequence(lambda n: n + 1)

    closedate = factory.fuzzy.FuzzyInteger(1, 1000)
    total_order_value = factory.fuzzy.FuzzyInteger(1, 1000)

    subscription = factory.RelatedFactory(SubscriptionFactory)
