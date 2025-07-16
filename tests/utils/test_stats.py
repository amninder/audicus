from __future__ import absolute_import, print_function, unicode_literals

from tests import BaseTest
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD
from audicus.schema.subscription_schema import SubscriptionSchema
from audicus.utils.stats import DF


class TestStats(BaseTest):

    def test_desrialize_subscription(self):
        """Test case to deserialize subscriptions"""

        sub1 = SubscriptionFactory(status=STATUS_ACTIVE)
        sub2 = SubscriptionFactory(status=STATUS_ACTIVE)
        sub3 = SubscriptionFactory(status=STATUS_ACTIVE)

        sub4 = SubscriptionFactory(status=STATUS_CANCELLED)
        sub5 = SubscriptionFactory(status=STATUS_CANCELLED)

        sub6 = SubscriptionFactory(status=STATUS_ON_HOLD)
        sub7 = SubscriptionFactory(status=STATUS_ON_HOLD)
        sub8 = SubscriptionFactory(status=STATUS_ON_HOLD)
        sub9 = SubscriptionFactory(status=STATUS_ON_HOLD)

        schema = SubscriptionSchema()
        data = [
            schema.dump(sub1),
            schema.dump(sub2),
            schema.dump(sub3),
            schema.dump(sub4),
            schema.dump(sub5),
            schema.dump(sub6),
            schema.dump(sub7),
            schema.dump(sub8),
            schema.dump(sub9),
        ]
        df = DF(data)
        self.assertEqual(3, df.get_size_by_category("status__c")[STATUS_ACTIVE])
        self.assertEqual(2, df.get_size_by_category("status__c")[STATUS_CANCELLED])
        self.assertEqual(4, df.get_size_by_category("status__c")[STATUS_ON_HOLD])
