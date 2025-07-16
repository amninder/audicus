from __future__ import absolute_import, print_function, unicode_literals

from sqlalchemy.exc import IntegrityError
from tests import BaseTest
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.models.subscription import Subscription
from audicus.schema.subscription_schema import SubscriptionSchema


class SubscriptionSchemaTest(BaseTest):

    def test_de_searialize(self):
        """Test case to deserialize"""
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
        """Test case to serialize"""
        schema = SubscriptionSchema()
        data = {
            "billing_interval__c": "b interval",
            "end_date__c": 3434,
            "id": 2,
            "next_payment_date__c": 3434,
            "start_date__c": 3434,
            "status__c": "cancelled",
        }
        actual_value = schema.load(data, session=self.db.session)
        self.db.session.add(actual_value)
        self.db.session.flush()

        expected_value = self.db.session.query(Subscription).where(Subscription.id == 2).one()
        self.assertEqual(expected_value.billing_interval, actual_value.billing_interval)
        self.assertEqual(expected_value.billing_interval, "b interval")
        self.assertFalse(expected_value.is_recurring)

    def test_id_is_unique(self):
        """id field is a unique field"""
        schema = SubscriptionSchema()
        data = {
            "billing_interval__c": "b interval",
            "end_date__c": 3434,
            "id": 2,
            "next_payment_date__c": 3434,
            "start_date__c": 3434,
            "status__c": "cancelled",
        }
        actual_value = schema.load(data, session=self.db.session)
        data_2 = {
            "billing_interval__c": "some interval",
            "end_date__c": 34,
            "id": 2,
            "next_payment_date__c": 94,
            "start_date__c": 23,
            "status__c": "on-hold",
        }
        schema2 = SubscriptionSchema()
        duplicate_value = schema2.load(data_2, session=self.db.session)

        with self.assertRaises(IntegrityError):
            self.db.session.add_all([duplicate_value, actual_value])
            self.db.session.flush()
