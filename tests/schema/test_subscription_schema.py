from tests import BaseTest
from audicus.schema.subscription_schema import SubscriptionSchema
from audicus.models.subscription import Subscription
from tests.factories.subscription_factory import SubscriptionFactory


class SubscriptionSchemaTest(BaseTest):

    def test_de_searialize(self):
        schema = SubscriptionSchema()
        data = SubscriptionFactory(
            billing_interval="b interval",
            end_date=3434,
            next_payment_date=3434,
            recurring_amount=2323,
            start_date=3434,
            status="cancelled",
        )
        self.db.session.flush()
        expected_data = {
            "billing_interval__c": "b interval",
            "end_date__c": 3434,
            "id": data.id,
            "next_payment_date__c": 3434,
            "recurring_amount__c": 2323,
            "start_date__c": 3434,
            "status__c": "cancelled",
        }
        self.assertEqual(expected_data, schema.dump(data))

    def test_serialize(self):
        schema = SubscriptionSchema()
        data = {
            "billing_interval__c": "b interval",
            "end_date__c": 3434,
            "id": 2,
            "next_payment_date__c": 3434,
            "recurring_amount__c": 2323,
            "start_date__c": 3434,
            "status__c": "cancelled",
        }
        actual_value = schema.load(data, session=self.db.session)
        self.db.session.add(actual_value)
        self.db.session.flush()

        expected_value = self.db.session.query(Subscription).where(Subscription.id == 2).one()
        self.assertEqual(expected_value.billing_interval, actual_value.billing_interval)
        self.assertEqual(expected_value.billing_interval, "b interval")
