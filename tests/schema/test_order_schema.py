from __future__ import absolute_import, print_function, unicode_literals

from tests import BaseTest
from tests.factories.order_factory import OrderFactory
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.models.order import Order
from audicus.schema.order_schema import OrderSchema


class OrderSchemaTest(BaseTest):

    def test_searialize(self):
        """Test Serializing order"""
        schema = OrderSchema()
        subscription = SubscriptionFactory()
        data = {
            "closedate": 123,
            "id": 1,
            "parent_subscription_id__c": subscription.id,
            "total_order_value__c": 2,
        }
        actual_value = schema.load(data, session=self.db.session)
        self.db.session.add(actual_value)
        self.db.session.commit()

        expected_order = self.db.session.query(Order).where(
            Order.id == 1).one()
        self.assertEqual(expected_order.subscription_id, subscription.id)

    def test_de_serialize(self):
        """Test deserializing order"""
        schema = OrderSchema()
        subscription = SubscriptionFactory(
            billing_interval="b interval",
            end_date=3434,
            next_payment_date=3434,
            recurring_amount=2323,
            start_date=3434,
            status="cancelled",
        )
        actual_data = OrderFactory(subscription=subscription)
        expected_data = {
            'id': 1,
            'closedate': actual_data.closedate,
            'total_order_value__c': actual_data.total_order_value,
            'parent_subscription_id__c': subscription.id
        }
        self.assertDictEqual(expected_data, schema.dump(actual_data))
